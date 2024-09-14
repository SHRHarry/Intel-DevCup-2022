import youtube_downloader as downloader
import music_source_separation.umx_openvino.run_umx_openvino as separater
import music_transcription.basic_pitch.openvino_inference as transcripter
import midi_merge as merge

import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
download_status = False
sep_progress = 0
transcript_stat = False
convert_stat = False
merge_stat = False

@app.route('/')
def index():
    return 'hello!!'

@app.route('/youtube_download', methods=['POST'])
def post_youtube_download():
    global download_status
    insert_val = request.get_json()
    url = insert_val['url']
    mp3_dir = insert_val['mp3_dir']

    mp3_path = downloader.download_mp3(url, mp3_dir)
    download_status = downloader.mp3_to_wav(mp3_path+".mp3", mp3_path+".wav")

    return jsonify({'download_status': str(download_status)})

@app.route('/run_separate', methods=['POST'])
def post_separate_music():
    global sep_progress
    
    insert_val = request.get_json()
    input_file = insert_val['input_file']
    output_dir = insert_val['output_dir']
    
    sep_stat = False
    try:
        separater.music_source_separation(input_file, output_dir, None)
        sep_stat = True
    except Exception as e:
        print(e)
        sep_stat = False
    
    return jsonify({'sep_status': str(sep_stat)})

@app.route('/run_transcript', methods=['POST'])
def post_transcript_music():
    global transcript_stat
    insert_val = request.get_json()
    input_file = insert_val['input_file']
    output_dir = insert_val['output_dir']
    transcript_stat = False
    try:
        transcripter.music_transcription(input_audio=input_file, model_onnx='./music_transcription/models/basic_pitch_43844_model.onnx', save_dictionary=output_dir)
        transcript_stat = True
    except Exception as e:
        print(e)
        transcript_stat = False
    
    return jsonify({'transcript_status': str(transcript_stat)})

@app.route('/vocal_other_merge', methods=['POST'])
def vocal_other_merge():
    global merge_stat
    insert_val = request.get_json()
    background_midi_path = insert_val['background_midi_path']
    vocal_midi_path = insert_val['vocal_midi_path']
    out_midi_path = insert_val['out_midi_path']
    merge_stat = False
    try:
        merge.merge(background_midi_path, vocal_midi_path, out_midi_path)
        merge_stat = True
    except:
        merge_stat = False
    
    return jsonify({'merge_status': str(merge_stat)})

@app.route('/run_midi_to_imgs', methods=['POST'])
def post_convert_midi_to_imgs():
    global convert_stat
    request.charset = "utf-8"
    insert_val = request.get_json()
    img_path = insert_val['img_path']
    midi_path = insert_val['midi_path']
    convert_stat = False
    try:
        print("MuseScore3.exe -o \"" + img_path + "\" " + midi_path + "\"")
        os.system(f"MuseScore3.exe -o \"{img_path}\" \"{midi_path}\"")
        convert_stat = True
    except:
        convert_stat = False
    
    return jsonify({'convert_stat': str(convert_stat)})

@app.route('/get_status', methods=['GET'])
def get_status():
    global download_status, sep_progress, transcript_stat, merge_stat
    sep_progress = separater.get_separate_progress()
    return jsonify({'download_status': str(download_status),
                    'sep_progress': str(sep_progress),
                    'transcript_status': str(transcript_stat),
                    'merge_status': str(merge_stat),
                    'convert_stat': str(convert_stat)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True,)