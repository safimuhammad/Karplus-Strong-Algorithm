#This project will use karplus strong algorithm to generate musical overtones.
import wave, math 
import numpy as np

sRate = 44100
nSamples = sRate * 5
x = np.arange(nSamples)/float(sRate)
vals = np.sin(2.0*math.pi*220.0*x)
data = np.array(vals*32767, 'int16').tostring()dd
file = wave.open('sine220.wav','wb')
file.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed'))
file.writeframes(data)
file.close() 

# we will now how sound is simulated using karplus-strong algorithm

def generateNote (freq):
    nSamples = 44100
    sampleRate = 44100
    N = int(sampleRate/freq)
    #starting the ring buffer 
    samples = np.array([0]*nSamples, 'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.966*0.5*(buf[0] + bud[1])
        buf.append(avg)
        buf.popleft()

    #converting to 16 bit
    smaples = np.array(samples*32767, 'int16')
    return samples.tostring()