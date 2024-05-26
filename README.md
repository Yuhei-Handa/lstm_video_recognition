# video_sleep_recognition


動画データを使用して体の動きから起床、睡眠を分類。

(1)mediapipeを使用して、上半身のlandmarkを取得。
    lstmに入力し、slidingwindow方式で分類。
    失敗（実験.ipynbに記載）

