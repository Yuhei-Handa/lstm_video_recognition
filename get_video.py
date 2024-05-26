import rtsp
import cv2
#from onvif import ONVIFCamera
import time
import requests
#from requests.auth import HTTPDigestAuth
import time
#import PySimpleGUI as sg
from glob import glob
import os
import json
import shutil

def get_output_video_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #既存の動画ファイルを取得
    files = glob(output_dir + "/*.mp4")
    if len(files) == 0:
        new_number = str(0).zfill(2)
    else:
        newest_number = files[-1][-6:-4]

        #新しいファイル名を作成
        new_number = int(newest_number) + 1
        new_number = str(new_number).zfill(2)
    output_video_dir = output_dir + "/output" + new_number + ".mp4"
    return output_video_dir

def get_output_json_dir(output_dir):

    #既存のjsonファイルを取得
    files = glob(output_dir + "/*.json")
    if len(files) == 1:
        new_number = str(0).zfill(2)
    else:
        print(files[-1])
        newest_number = files[-1][-7:-5]
        new_number = int(newest_number) + 1
        new_number = str(new_number).zfill(2)

    output_json_dir = output_dir + "/output" + new_number + ".json"
    
    return output_json_dir

# レイアウトの定義
# layout = [
#     [sg.Text('長押しボタンのサンプル')],
#     [sg.Button('長押しボタン', key='-LONG_PRESS-', size=(150, 50))],
#     [sg.Text('', size=(1, 1), key='-OUTPUT-')],
# ]

# ウィンドウの作成
#window = sg.Window('長押しボタン', layout)

# 長押しボタンのステータス
button_pressed_time = None
long_press_threshold = 2  # 長押しの閾値（秒）

# RTSP URL
url = "your_key"
drive = "D:"
directory = "output"

# パスを結合
output_dir = directory
is_neoti = 1
is_neoti_list = []
is_neoti_dict = {}
frame_list = []
#最高録画時間は4時間
over_time = 60*5

#cap = cv2.VideoCapture(url)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
original_fps = int(cap.get(cv2.CAP_PROP_FPS))
desired_fps = 15
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video_dir = get_output_video_dir(output_dir)
out = cv2.VideoWriter(output_video_dir, fourcc, original_fps, (width, height), isColor=True)

outputed_json_dir = "output.json"
output_json_dir = get_output_json_dir(output_dir)

print(output_video_dir)
print(output_json_dir)

start_time = time.time()

frame_interval = int(original_fps / desired_fps)
frame_count = 0

while True:

    current_time = time.time()  # 現在時刻を取得
    elapsed_time = current_time - start_time  # 経過時間を計算
    


    ret, frame = cap.read()

    if not ret:
        break

    is_neoti_list.append(is_neoti)
    frame_list.append(frame)
    #out.write(frame)

    if elapsed_time > over_time:
        break


for frame in frame_list:
    out.write(frame)

print(len(frame_list))
print(len(is_neoti_list))

is_neoti_dict["is_neoti_list"] = is_neoti_list
is_neoti_dict["output_video_dir"] = output_video_dir

with open(output_json_dir, 'w') as f:
    json.dump(is_neoti_dict, f, indent=4)

shutil.copy(output_json_dir, outputed_json_dir)

cap.release()
out.release()
