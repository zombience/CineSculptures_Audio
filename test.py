
import sys
import argparse


def main(args):
	print('python ran with args: ', args.file)

#main(sys.argv)

parser = argparse.ArgumentParser(description='CineSculptures arguments')
parser.add_argument('-file', metavar='file', required=True, help='file to read: FOO .wav for now')
parser.add_argument('-chunk', metavar='chunksize', default=4020, help='fft process size: larger sizez = higher frequency precision, lower time domain accuracy (i.e. time smearing)')
args = parser.parse_args()
main(args)