import colorsys
import time
import cv2 as cv
import numpy as np
import audioscape


class Spectro:

    im = None

    def __init__(self, audioscapein):

        self.ascape = audioscapein
        self.im = None

        self.freq = self.ascape.freq
        self.amp = self.ascape.fourier

        self.max_amp = 100
        self.max_frequency = self.ascape.samplerate
        self.fullsize = (len(self.ascape.fourier), len(self.ascape.freq))

        self.color = ""

    def close(self, instance):
        del self.im

    def create_spectrogram(self, size="", color=False):
        self.color = color

        t = time.time()  # timestamp for image creation time
        self.im = self.amp

        if color:
            self.im = (self.im - np.ones_like(self.im) * 120)
            self.im *= (179 / -120.0)

            self.imval = np.ones_like(self.im) * 255

            self.im = self.im.astype(np.uint8)
            self.imval = self.imval.astype(np.uint8)

            self.im = cv.merge((self.im, self.imval, self.imval))
            self.im = cv.cvtColor(self.im, cv.COLOR_HSV2BGR)
        else:
            self.im *= (200 / 120.0)

        self.im = cv.rotate(self.im, cv.ROTATE_90_COUNTERCLOCKWISE)
        print("Image creation took {} seconds".format(time.time() - t))

    def save_spectrogram(self):
        # build filename
        if self.color:
            cmode = 'color'
        else:
            cmode = 'bw'

        filename_out = self.ascape.filename_out + "_{}".format(cmode)
        filename_out += ".png"

        if self.im.any:
            cv.imwrite(filename_out, self.im.astype(int))
            print("Wrote {}!".format(filename_out))
        else:
            print("No spectrogram has been created!")

    def show(self):
        cv.imshow("Spectrogram", self.im)

