# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
import os
from asr import asrer

# 开启声音输入
pa = PyAudio()
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True,
                 frames_per_buffer=NUM_SAMPLES)

save_count = 0
save_buffer = []

asr_ = asrer()

while True:
    # 读入NUM_SAMPLES个取样
    string_audio_data = stream.read(NUM_SAMPLES, exception_on_overflow=False)
    # 将读入的数据转换为数组
    audio_data = np.fromstring(string_audio_data, dtype=np.short)
    # 计算大于LEVEL的取样的个数
    large_sample_count = np.sum( audio_data > LEVEL )
    print np.max(audio_data), np.min(audio_data)