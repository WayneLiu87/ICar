# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
import os
from asr import asrer


import json
from watson_developer_cloud import ConversationV1
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='f46aa9c7-10df-4493-a79f-3fdf3e1c66ca',
    password='qwGs7PCwneNx',
    x_watson_learning_opt_out=True)  # Optional flag




#conversation
conversation = ConversationV1(
    username='34eaf574-d06a-417c-bd8f-dffa66fb456f',
    password='EEbG0SQa8Vdh',
    version='2016-09-20')

# replace with your own workspace_id
workspace_id = '17fb5025-7d39-4b21-a6e8-711e7ef57308'

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': 'Hi'})

context = response['context']

robot_say = response["output"]["text"][0]
print robot_say

with open('data/output.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(robot_say, accept='audio/wav',
                                  voice="en-US_AllisonVoice"))

f = wave.open("data/output.wav","rb")
chunk = 1024
pr = PyAudio()
streamr = pr.open(format = pr.get_format_from_width(f.getsampwidth()),
                  channels = f.getnchannels(),
                  rate = f.getframerate(),
                  output = True)
data = f.readframes(chunk)
while data !="":
    streamr.write(data)
    data = f.readframes(chunk)
streamr.stop_stream()
streamr.close()
pr.terminate()

# 将data中的数据保存到名为filename的WAV文件中
def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLING_RATE)
    wf.writeframes("".join(data))
    wf.close()



NUM_SAMPLES = 8000      # pyAudio内部缓存的块的大小
SAMPLING_RATE = 16000    # 取样频率
LEVEL = 1100            # 声音保存的阈值
COUNT_NUM = 6          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 8         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样

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
    print np.max(audio_data)
    # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
    if large_sample_count > COUNT_NUM:
        save_count = SAVE_LENGTH
    else:
        save_count -= 1

    if save_count < 0:
        save_count = 0

    if save_count > 0:
        # 将要保存的数据存放到save_buffer中
        save_buffer.append( string_audio_data)
    else:
        # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻
        if len(save_buffer) > 0:
            filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
            save_wave_file(os.path.join("data", filename), save_buffer)
            save_buffer = []
            print filename, "saved"
            #say = asr_.recongnize(os.path.join("data", filename))
            say = asr_.ibm_recongnize(os.path.join("data", filename))
            print say


            response = conversation.message(workspace_id=workspace_id, message_input={
                'text': say}, context=context)

            try:
                robot_say = response["output"]["text"][0]
            except:
                robot_say = ""
            print robot_say
            context = response['context']

            with open('data/output.wav', 'wb') as audio_file:
                audio_file.write(
                    text_to_speech.synthesize(robot_say, accept='audio/wav',
                                          voice="en-US_AllisonVoice"))

            f = wave.open("data/output.wav","rb")
            chunk = 1024
            pr = PyAudio()
            streamr = pr.open(format = pr.get_format_from_width(f.getsampwidth()),
                            channels = f.getnchannels(),
                            rate = f.getframerate(),
                            output = True)
            data = f.readframes(chunk)
            while data !="":
                streamr.write(data)
                data = f.readframes(chunk)
            streamr.stop_stream()
            streamr.close()
            pr.terminate()



