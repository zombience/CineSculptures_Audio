# CineSculptures Landscape Generator

Inspired by Frederic Brodbeck's "cinemetrics" project, the goal of CineSculptures is to visualize a film as a static, unique 3D identity with its audio track projected as the landscape and its frame-by-frame color palette as its texture. This python project takes an audio file and texture image as its input, and generates the 3D landscape.


### Prerequisites

This project requires the follwoing packages:

numpy
opencv-python

Both can be installed via pip in your command line of choice as the following:

pip install [pkg name]

Make sure this is installed for the version of Python you intend on interpreting the project with.
For example, if you're intepreting with Python 3.5 make sure you install packages on 3.5, not 2.7.


### Running

Simply run the "main.py" file via a command line:

python main.py

or in your Python IDE.


```

Right now there is no GUI or command line options. To change parameters you can change the method calls in the "main" method of the "main.py" file.


- If you want to set an input, you can edit the "infile" variable to be the path of your file. By default, the program will prompt you with an open file dialogue.

- The next line sets up the analysis and can accept the following parameters:
	- "chunk" - size of the analysis window. Bigger sizes are slower gives better frequency precision at the cost of time domain precision. 
	   Smaller sizes have more accurate time precision, but less accurate frequency precision.
	   Frequency resolution is dependent on this as the resolution is equal to (sampling rate) / (chunk size)

	- "ascape" AudioScape object holds all the information related to the input audio file and will initiate the FFT, spectrogram, and OBJ creation.
	- "analyze" will create the Fourier analysis.
	- "trim" imposes a low pass filter, and takes in a number in hertz.
	- "resize" accepts "False" or a tuple. Resizes the output after image generation and uses linear interpolation. 
	   The size can be a direct size like: (4000, 3000) or it can contain a float where it is a ratio of the original size like (0.5, 2.0) or even (4000, 1.5)
	- "write_obj" will export an OBJ file. Currently, faces are not drawn correctly.
	- "write_spectrogram" will create a spectrogram of the audio input. Takes a "colorIn" parameter, false by default:
		- "colorIn" - if set to "True" the output will be in color with Red light indicating stronger frequency amplitudes and Blue light as weaker amplitudes.
	  	 If "False", spectrogram will be in black and white, with white indiciating stronger frequency amplitudes.

```


## Information

The code was written with Python 3.6 in Pycharm Community Edition 2017.2.3


## Version

2018/03/02
0.2:
 - Added OBJ writing, and direct smoothing, resizing, and trimming (previously only for spectrograms)
 - Using OpenCV instead of Pillow (image writing is ridiculously faster!)
 - Made code easier to use / easier to change preferences

2018/01/20
0.1:
 - Initial release

## TODO
 - GUI and pre-export display
 - Open video file and extract audio
 - Separate multichannel tracks into audio
 - Fix face drawing in OBJ
 - Add textures
 - Adaptive 3D smoothing
 - Much more

## Authors

Vincenzo Sicurella, with cited examples from stackoverflow in code.
Project led by Kirill Mazor, inspired by Frederic Broderick's "cinemetrics"