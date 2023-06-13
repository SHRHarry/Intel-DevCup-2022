# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 18:00:48 2022

@author: ms024
"""

import midi

def merge(background_midi_path, vocal_midi_path, out_midi_path):
    pattern1 = midi.read_midifile(background_midi_path)
    pattern2 = midi.read_midifile(vocal_midi_path)

    pattern = midi.Pattern()

    for track in pattern1:
        pattern.append(track)

    for track in pattern2:
        pattern.append(track)

    midi.write_midifile(out_midi_path, pattern)

if __name__ == "__main__":
    background_midi_path = r"E:\Job\ASUS\Intel_Research\DevCup\test_music_data\output_result\TAEYANG - 'RINGA LINGA' Dance Performance Video\other_result_midi.mid"
    vocal_midi_path = r"E:\Job\ASUS\Intel_Research\DevCup\test_music_data\output_result\TAEYANG - 'RINGA LINGA' Dance Performance Video\vocals_result_midi.mid"
    out_midi_path = r"E:\Job\ASUS\Intel_Research\DevCup\test_music_data\output_result\TAEYANG - 'RINGA LINGA' Dance Performance Video\mix.mid"
    merge(background_midi_path, vocal_midi_path, out_midi_path)