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

    chunk = 4410 # three seconds is 3 * 44100, but it doesn't look good.

    # create AudioScape object
    ascape = audioscape.AudioScape(infile, chunk)
    print("Audio File:", infile)

    ascape.analyze()
    ascape.trim(14000) # the film audio seems to by lowpassed at 14000, so I trimmed everything above that
    ascape.resize((3000, 500)) # we might want to use an even smaller size, stretched out
    ascape.smooth() # opencv bilateral filter, can take parameters
    ascape.write_obj()
    ascape.write_spectrogram() # this mutates the data for speed trade-off, use after obj writing

    ascape.close()
    root.quit()
    return 0

main()