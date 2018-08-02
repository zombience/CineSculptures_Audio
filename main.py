import spectro
import writeobj
import audioanalysis
#import tkinter as tk
#from tkinter import filedialog
import audioscape
import argparse

def main(args):
    print(args.file)
    # set a default input file
    infile = args.file

    # setup dialog window
    #root = tk.Tk()
    #root.withdraw()
    #root.update()

    # get audio file
    #while (infile[-3:] != "wav"):
    #    infile = filedialog.askopenfilename()

    #root.quit()

    chunk = args.chunk#4020 # three seconds is 3 * 44100, but it doesn't look good.



    # create AudioScape object
    ascape = audioscape.AudioScape(infile, int(chunk))
    print("running analysis on audio File:", infile, 'with chunksize: ', chunk)

    ascape.analyze()
    ascape.trim(14000) # the film audio seems to by lowpassed at 14000, so I trimmed everything above that
    #ascape.resize((0.5, 1.0)) # we might want to use an even smaller size, stretched out
    #ascape.smooth(params=(9, 75, 75)) # opencv bilateral filter, can take parameters
    #ascape.write_obj() # STEREO FILES NOT YET IMPLEMENTED
    #ascape.write_spectrogram(colorIn=False) # this mutates the data for speed trade-off, use after obj writing
    ascape.write_dualspectrogram()

    ascape.close()
    return 0

parser = argparse.ArgumentParser(description='CineSculptures arguments')
parser.add_argument('-file', metavar='file', required=True, help='file to read: must be .wav for now')
parser.add_argument('-chunk', metavar='chunksize', default=4020, help='fft process size: larger sizez = higher frequency precision, lower time domain accuracy (i.e. time smearing)')
args = parser.parse_args()
main(args)