import wave
import numpy as np
import time
import audioscape

class AudioAnalysis:

    def __init__(self, audioscapein):

        # initialize
        self.ascape = audioscapein

        # make references for easier code reading
        self.chunk = self.ascape.chunk
        self.wf = self.ascape.wf

        self.bitdepth = self.ascape.bitdepth
        self.samplerate = self.ascape.samplerate
        self.max_frequency = self.ascape.max_frequency
        self.number_samples = self.ascape.number_samples


    def analyze(self):

        # reference / source: https://stackoverflow.com/questions/2648151/python-frequency-detection

        print("Chunk Size:", self.chunk)
        print("Sample rate:", self.ascape.samplerate)
        print("Number of frames:", self.ascape.number_samples)

        window = np.blackman(self.chunk)
        data = self.wf.readframes(self.chunk)

        print("Analyzing...")
        t = time.time()
        indata = []

        # read samples into 'data' buffer until you run out
        #while (len(data) == self.chunk * self.bitdepth):
        for i in range(self.ascape.width):
            # unpack data and multiply by window with numpy magic
            indata = np.array(wave.struct.unpack("%dh" % (len(data)/self.bitdepth), data)) * window

            # take fft, use "ortho" scaling, and square values
            self.ascape.fourier[i] = 6*np.log2(np.abs(np.fft.rfft(indata)))

            # continue with more data
            data = self.wf.readframes(self.chunk)

        print("Number of chunks:", len(self.ascape.fourier))

        # get frequencies sampled
        self.ascape.freq = np.fft.rfftfreq(len(indata), d=1. / self.samplerate)
        print("Number of freqs:", len(self.ascape.freq))
        print("FFT took {} seconds".format(time.time() - t))