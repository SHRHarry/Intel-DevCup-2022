# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:01:48 2022

@author: ms024
"""

import os
import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment

def parser():
    parser = argparse.ArgumentParser(description='youtube downloader')
    parser.add_argument('--url', default='https://www.youtube.com/watch?v=9OQBDdNHmXo', type=str, help='youtube music url')
    parser.add_argument('mp3_dir', metavar='DIR', help='path to mp3')
    return parser.parse_args()

# def download_mp3(url, save_path):
#     yt = YouTube(url)
#     mp3_path = os.path.join(save_path, yt.title+".mp3")
#     yt.streams.get_audio_only().download(filename=mp3_path)
#     return mp3_path

def download_mp3(url, save_path):
    yt = YouTube(url, on_progress_callback = on_progress)
    mp3_path = os.path.join(save_path, yt.title)
    ys = yt.streams.get_audio_only()
    ys.download(mp3=True, filename=mp3_path)
    return mp3_path

def mp3_to_wav(mp3_path, wav_path):
    try:
        sound = AudioSegment.from_file(mp3_path)
        sound.export(wav_path, format="wav")
        os.remove(mp3_path)
        return True
    except:
        return False

if __name__ == "__main__":
    args = parser()
    mp3_path = download_mp3(args.url, args.mp3_dir)
    wav_path = mp3_path.replace(".mp3", ".wav")
    mp3_to_wav(mp3_path, wav_path)