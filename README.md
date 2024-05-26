# video_sleep_recognition


動画データを使用して体の動きから起床、睡眠を分類。

(1)mediapipeを使用して、上半身のlandmarkを取得。
    lstmに入力し、slidingwindow方式で分類。
    失敗（実験.ipynbに記載）

### 起床
![無題の動画 ‐ Clipchampで作成](https://github.com/Yuhei-Handa/video_sleep_recognition/assets/135846516/d5f3611e-e2f5-4ae5-8181-95f67e56acaf)

### 睡眠
![無題の動画 ‐ Clipchampで作成 (1)](https://github.com/Yuhei-Handa/video_sleep_recognition/assets/135846516/41c35e12-79ce-46c4-8be0-d7a4631696e6)
