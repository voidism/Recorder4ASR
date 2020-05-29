# Recorder4ASR

## Requirements
- Python3
- pyAudio  


Windows:  
  - `python3 -m pip install pyaudio`  

Mac:  
  - `brew install portaudio`  
  - `python3 -m pip install pyaudio`  

## Usage

```
python3 record.py transcripts.txt [start number]
```

會從`transcripts.txt`檔案裡的第`[start number]`行開始錄

- 一開始會顯示預估完成時間
- 每句開始之前有一秒鐘的準備時間

![image](https://user-images.githubusercontent.com/26344602/82901128-1387df00-9f90-11ea-99af-f8a13b5bb53b.png)

- 錄製的長度與句子長度相關 (第一個字0.7s, 第二個字0.5s, 第三個字0.4s, 之後每加一個字+0.3s)
- 每10句會有一次5秒鐘的吞口水時間

![image](https://user-images.githubusercontent.com/26344602/82901473-8a24dc80-9f90-11ea-8f6f-e9a7752e68b8.png)

錄完的檔案會存到`wavs/`資料夾
