import colorsys
import time
import cv2 as cv
import numpy as np
import audioscape


class Spectro:

    im = None

    def __init__(self, audioscapein):

        self.ascape = audioscapein
        self.im = []

        self.freq = self.ascape.freq

        self.color = ""

    def create_spectrogram(self, color=False):
        self.color = color
        t = time.time()  # timestamp for image creation time

        for c in range(self.ascape.number_channels):

            if color:
                np.multiply(
                    self.ascape.fourier[c], 360.0 / self.ascape.max_amp, out=self.ascape.fourier[c], casting='unsafe')
                self.ascape.fourier[c] -= 360
                self.ascape.fourier[c] *= -1

                self.imval = np.ones_like(self.ascape.fourier[c]) * 255

                self.imval = self.imval.astype(np.uint8)

                self.im.append(cv.merge((self.ascape.fourier[c].astype(np.uint8), self.imval, self.imval)))
                self.im[c] = cv.cvtColor(self.im[c], cv.COLOR_HSV2BGR, self.im[c])

            else:
                np.multiply(
                    self.ascape.fourier[c], 255.0 / self.ascape.max_amp, out=self.ascape.fourier[c], casting='unsafe')
                self.im.append(self.ascape.fourier[c].astype(np.uint8))

                self.im[c] = np.rot90(self.im[c])

        print("Image creation took {} seconds".format(time.time() - t))

    def save_spectrogram(self, channel=0, id=""):
        # build filename
        if self.color:
            cmode = 'color'
        else:
            cmode = 'bw'

        filename_out = self.ascape.filename_out + "_{}".format(cmode) + id
        filename_out += ".png"

        cv.imwrite(filename_out, self.im[channel])
        print("Wrote {}!".format(filename_out))

    def show(self):
        cv.imshow("Spectrogram", self.im)