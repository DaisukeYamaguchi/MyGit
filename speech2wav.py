Logo
Posts
About
Pythonでマイクからの音を録音(pyaudio使用)
2015-12-02
もくてき
FFTがしたいのだけど、その前にマイクからちゃんと音が拾えているのか確認する。メインのループとは別に音を取り出して処理したい。

とりあえず録音
ソースコードは基本的にネットで拾ってきて所々自分用に修正。

音を取ってくるためのライブラリはpyaudioを使う。まず最初に、音声入力に使うデバイスのインデックス番号を確認する。使えるデバイスのインデックス番号とそのデバイス名が出力されるので確認する。


# -*- coding: utf-8 -*-
import sys
import pyaudio

#インデックス番号の確認

p = pyaudio.PyAudio()
count = p.get_device_count()
devices = []
for i in range(count):
    devices.append(p.get_device_info_by_index(i))

for i, dev in enumerate(devices):
    print (i, dev['name'])

                              
録音する。さっき確認したインデックス番号はinput_device_indexのパラメータへ設定する。


# -*- coding: utf-8 -*-
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1        #モノラル
RATE = 44100        #サンプルレート
CHUNK = 2**11       #データ点数
RECORD_SECONDS = 10 #録音する時間の長さ
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index=4,   #デバイスのインデックス番号
        frames_per_buffer=CHUNK)
print ("recording...")

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

                              
実行すると、　音声サーバへの接続に失敗しました　みたいなエラーがでるけど、file.wavという音ファイルができあがるのでそれを再生してみて問題なければよし。

別のスレッドで音をとって処理
音をとりつつ何かをするために、別スレッドで音をとる。コールバック関数というのが使えるらしいのでやってみる。


# -*- coding: utf-8 -*-
import pyaudio
import wave
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2**11
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file2.wav"

audio = pyaudio.PyAudio()
frames = []
def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)          #この中で別スレッドの処理
    return(None, pyaudio.paContinue)

stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index=4,
        frames_per_buffer=CHUNK,
        stream_callback=callback)

print ("recording...")
stream.start_stream()
time.sleep(RECORD_SECONDS)
print ("finished recording")

stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

                              
callback関数の中のin_dataが、pyaudioでとった音データなので、それをどんどん配列に入れていく。file2.wavという音ファイルができるので再生してみて問題なければよし。

おわり
たまに　入力オーバーフローしました　みたいなエラーがでたけど、データ点数を少し上げると解消した。データ点数上げてもオーバーフローするときは一度USBマイクを抜き差しすると復活した。

USBマイクを使えば、Raspberry Pi B, Pi2でも実行できた。

SPONSORED LINK

 
プライバシー・ポリシー
2015-2017 www.ningendesu.net