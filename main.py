import spectro
import writeobj
import audioanalysis
import tkinter as tk
from tkinter import filedialog
import audioscape

def main():

    # set a default input file
    infile = ""

    # setup dialog window
    root = tk.Tk()
    root.withdraw()

    # get audio file
    while (infile[-3:] != "wav"):
        infile = filedialog.askopenfilename()

    chunk = 800 # three seconds is 3 * 44100, but it doesn't look good.

    # create AudioScape object
    ascape = audioscape.AudioScape(infile, chunk)
    print("Audio File:", infile)

    ascape.analyze()
    #ascape.trim(14000) # the film audio seems to by lowpassed at 14000, so I trimmed everything above that
    #ascape.resize((0.5, 1.0)) # we might want to use an even smaller size, stretched out
    #ascape.smooth(params=(9, 75, 75)) # opencv bilateral filter, can take parameters
    #ascape.write_obj() # STEREO FILES NOT YET IMPLEMENTED
    #ascape.write_spectrogram(colorIn=False) # this mutates the data for speed trade-off, use after obj writing
    ascape.write_dualspectrogram()

    ascape.close()
    root.quit()
    return 0

main()