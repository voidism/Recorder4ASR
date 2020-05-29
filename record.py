import pyaudio
import wave
import time

framerate = 16000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 10

interval = [0.7, 0.5, 0.4] + [0.3]*20

def save_wave_file(filename, data):
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()


def record(f, t=5):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=framerate,
        input=True,
        frames_per_buffer=NUM_SAMPLES,
    )
    my_buf = []
    count = 0
    while count < TIME * t:
        string_audio_data = stream.read(NUM_SAMPLES)
        if count == 0:
            print("錄音中 (%.1f s)"%float(t))
        my_buf.append(string_audio_data)
        count += 1
        print(".", end="", flush=True)

    save_wave_file(f, my_buf)
    stream.close()

if __name__ == '__main__':
    import sys, os
    os.makedirs('wavs', exist_ok=True)
    if len(sys.argv)>2:
        start = int(sys.argv[2])
    else:
        start = 0
    f = open(sys.argv[1]).readlines()
    estimate = 0.0
    for line in f:
        i, line = line.strip().split('. ')
        i = int(i)
        if i<start:
            continue
        estimate += 1.0 + float(len(line))*0.7 + (5.0 if i%10==0 else 0.0)
    print("預估完成時間: %.1f s"%estimate)
    f = open(sys.argv[1]).readlines()
    for line in f:
        i, line = line.strip().split('. ')
        i = int(i)
        if i<start:
            continue
        print('\n<%d> '%i, line)
        print("預備中 (1.0 s) ", end="")
        for _ in range(5):
            print("=", end="", flush=True)
            time.sleep(0.2)
        print('>')
        t = sum(interval[:len(line)])#float(len(line))*0.7
        record('wavs/%d.wav'%i, t=t)
        print("")
        if i%10==0:
            print("\n吞口水時間 (5.0 s)")
            for j in range(50):
                print(".", end="", flush=True)
                time.sleep(0.1)
            print('')
