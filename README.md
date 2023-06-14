# Intel-DevCup-2022-Cyber-Audio

[![Competition](https://img.shields.io/badge/Intel--DevCup-Competition-blue)](https://makerpro.cc/intel-devcup/)
[![OpenVINO](https://img.shields.io/badge/Intel-OpenVINO-blue)](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)
## Introduction

This repo is a service built based on [Competition-2022-OpenVINO-Devcup](https://github.com/FanChiMao/Competition-2022-OpenVINO-Devcup) (thanks to my teammates for their contributions), with additional functions of downloading audio sources from youtube, mixing midi, and export music sheet by calling MuseScore.

## Installation

 - For downloading audio sources from youtube, please install the dependencies with:
```sh
pip install pytube==12.1.3 pytube3==9.6.4
```

 - For mixing midi, please install the dependencies with:
 ```sh
pip install git+https://github.com/vishnubob/python-midi@feature/python3
```

 - For export music sheet as image (.png), please install [MuseScore3](https://ftp.osuosl.org/pub/musescore/releases/MuseScore-3.2/Musescore-3.2.0-x86_64.msi)
 

## Run without environment (pyinstaller)

 - To package it into an exe file, please install the dependencies with:
```sh
pip install Flask Flask-Cors pyinstaller
```

 - Modify the path in binary, data, and hiddenimports in [build.spec](https://github.com/SHRHarry/Intel-DevCup-2022-Cyber-Audio/blob/main/build.spec):
 ```sh
 binaries=[('<path-to-openvino-package-in-env>\\libs\\*', '.\\openvino\\libs')],
 datas=[('<path-to-music_source_separation-model>\\*', '.\\music_source_separation\\model'),
        ('<path-to-librosa-package-in-env>\\util\\example_data\\*', '.\\librosa\\util\\example_data'),
        ('<path-to-music_transcription-model>\\basic_pitch_43844_model.onnx', '.\\music_transcription')],
 hiddenimports=['openvino.pyopenvino', 'openvino.inference_engine.constants'],
 ```
 
 - Run the following command to build the service:
 ```sh
 pyinstaller --distpath <path-to-exe-file> build.spec
 ```
 
 - Run the following command to execute the service:
  ```sh
 cd <path-to-exe-file>\CyberAudio
 CyberAudio.exe
 ```

## TODO
 - UI for the service

## References

+ https://github.com/FanChiMao/Competition-2022-OpenVINO-Devcup

+ https://musescore.org/zh-hant
