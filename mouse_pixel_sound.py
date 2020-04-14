#! python3
#
# On Windows 7:
# pip install pyautogui
# pip install pipwin
# pipwin install pyaudio

from time import sleep
import pyautogui, sys
import colorsys
import pyaudio
import math

    
def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    #restframes = n_samples % sample_rate
    
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in range(n_samples))
    stream.write(bytes(bytearray(samples)))


print('Press Ctrl-C to quit.')
try:
    sample_rate=22050
    threshold = 0.1
    PyAudio = pyaudio.PyAudio
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
    
    while True:
        x, y = pyautogui.position()
        pixRGB = pyautogui.pixel(x, y)
        pixHLS = colorsys.rgb_to_hls(pixRGB[0]/255, pixRGB[1]/255, pixRGB[2]/255)
        positionStr = 'X: %4d Y: %4d  H: %1.3f L: %1.3f S: %1.3f' % (x, y, \
                        pixHLS[0], pixHLS[1], pixHLS[2])
        print(positionStr, end='\n')
        #print('\b' * len(positionStr), end='', flush=True)
        sine_tone(200+pixHLS[0]*200,0.05,(max(0,pixHLS[1]-threshold))*0.05)

        
except KeyboardInterrupt:
    print('\nOK, all done.\n')
    stream.stop_stream()
    stream.close()
    p.terminate()



