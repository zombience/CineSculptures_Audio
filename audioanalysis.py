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
        self.buffer_size = self.ascape.buffer_size
        self.wf = self.ascape.wf

        self.bitdepth = self.ascape.bitdepth
        self.samplerate = self.ascape.samplerate
        self.max_frequency = self.ascape.max_frequency
        self.number_samples = self.ascape.number_samples
        self.number_channels = self.ascape.number_channels


    def analyze(self):

        # reference / source: https://stackoverflow.com/questions/2648151/python-frequency-detection

        print("Chunk Size:", self.chunk)
        print("Sample rate:", self.ascape.samplerate)
        print("Number of frames:", self.ascape.number_samples)

        window = np.hanning(self.chunk)

        unpacked = []

        print("Analyzing...")
        t = time.time()
        data = self.wf.readframes(self.chunk)

        # get frequencies sampled
        self.ascape.freq = np.fft.rfftfreq(self.chunk, d=1. / self.samplerate)

        # read samples into 'data' buffer until you run out
        for i in range(self.ascape.width):
            # unpack data
            unpacked = np.fromstring(data, self.ascape.dtype) # faster! :)
            unpacked.shape = (self.chunk, self.number_channels)
            unpacked = unpacked.T

            for c in range(self.number_channels):
                # get a channel and multiply by window
                unpacked[c] = unpacked[c] * window

                # take fft, use "ortho" scaling, and square values
                self.ascape.fourier[c][i] = np.power(np.abs(np.fft.rfft(unpacked[c])), 0.28)

            # continue with more data
            data = self.wf.readframes(self.chunk)

        t_delta = time.time() - t
        self.ascape.max_amp = np.amax(self.ascape.fourier)
        print("FFT took {} seconds".format(t_delta))
        print("Number of chunks:", len(self.ascape.fourier[0]))
        print("Number of freqs:", len(self.ascape.freq))