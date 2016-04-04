Title: Processing audio files (with Praat)
Date: 2013-06-24 17:10
Author: Kristine Yu
Tags: ldc-kiy, fieldwork, coding, shell, praat, audio, tutorial
Slug: processing-audio-files-praat

This tutorial introduces how to process audio files from fieldwork
recordings with [Praat](http://www.praat.org). See the tutorial
[Processing audio (with SoX)](processing-audio-files-sox.html) for
the sister tutorial using [SoX](http://sox.sourceforge.net) command line utilities.

<!-- PELICAN_END_SUMMARY -->

Following an <a href = "#intro">introductory section</a>, the tutorial shows how to use <a href =
"http://www.praat.org/">Praat</a> 
information about a soundfile and make two different modifications to
the soundfile:[^1]

+ <a href="#display">Displaying information about the audio file</a>
+ <a href="#channel">Extracting a single channel from the file</a>
+ <a href="#downsample">Downsampling the audio file</a>

##<a id="intro"></a> Introduction ##

Praat is powerful cross-platform, free and
[open source](http://www.fon.hum.uva.nl/praat/download_sources.html) software created and maintained by Paul Boersma and David
Weenink at the University of Amsterdam. It is widely used in phonetics
and phonology and beyond. You can download for your platform at the
following links:

+ [Mac](http://www.fon.hum.uva.nl/praat/download_mac.html)
+ [Windows](http://www.fon.hum.uva.nl/praat/download_win.html)
+ [Linux](http://www.fon.hum.uva.nl/praat/download_linux.html)

It is regularly updated, so if you haven't downloaded a new version in
a few months, you might take a look and see if there's a newer version available.
The help files are extensive and include a set of
[introductory tutorials](http://www.fon.hum.uva.nl/praat/manual/Intro.html). There
is also a helpful [Praat Users group](http://uk.groups.yahoo.com/group/praat-users/).

### Instructions for tutorials ###

The files for the tutorials can be found
[this directory](http://media.krisyu.org/ldc-kiy) under
`tutorials/processing-audio-files`
([here](http://media.krisyu.org/ldc-kiy/tutorials/processing-audio-files/)). Once
you've downloaded the `ldc-kiy` repository, you can navigate to the
`tutorials/processing-audio-files/your-turn/20111213/` sub-directory to access
all the files used in the tutorial. Ignore the other sub-directory in
`your-turn` called `batch-demo`, which is only for the [SoX tutorial](../processing-audio-files-praat). 

The `tutorials/processing-audio-files/demo/` directory contains all the files used and generated during the
tutorial for your reference (again, ignore the `batch-demo` directory). The `your-turn/` directory is for you to
play in and contains only the raw audio files the tutorial works with,
and not any of the generated files from the tutorial. 


---------------------------------------------------------

## <a id="display"></a>Displaying audio file information ##

1. Launch `Praat`. 
2. Select `Open > Open long sound...` from the menu at the top of
the `Praat Objects` window, as shown below. 

    <div align = "center">
    <figure>
   	<img src="/img/2013/06/praat-long-sound.jpg"
    alt = "Open long sound in Praat"
    width = "400">
    <figcaption> <tt>Open long sound</tt> command.</figcaption>
    </figure>
    </div><p></p>

    A `LongSound` is distinct from a `Sound` object type in Praat. As
    it says in the [manual](http://www.fon.hum.uva.nl/praat/manual/LongSound.html):
	
    > A LongSound object gives you the ability to view and label a
    > sound file that resides on disk. You will want to use it for
    > sounds that are too long to read into memory as a Sound object
    > (typically, a few minutes).
	
3. In the `your-turn/` directory, select
    `20111213/raw/20111213-1-kiy-ap-framedwordlist.wav` to be
    opened. Now there should be a `LongSound
    20111213/raw/20111213-1-kiy-ap-framedwordlist` object listed in
    your object window. Note that it is highlighted in light blue. That
    means that it is selected. You can select an object by clicking on
    it in the object window.

      <div align = "center">
      <figure>
	  <img src="/img/2013/06/praat-longsound-obj.jpg"
      alt = "LongSound object in object window"
       width = "400">
      <figcaption> LongSound object
      <tt>20111213/raw/20111213-1-kiy-ap-framedwordlist</tt> in object window.</figcaption>
      </figure>
      </div><p></p>
4. With `LongSound 20111213/raw/20111213-1-kiy-ap-framedwordlist`
   selected, click on the `Info` button at the bottom of the object
   window, as shown below. This will pop up the `Praat Info` window
   with information about the audio file displayed, including the file
   format, duration of the file, sampling rate, and bit depth.[^2]

    <div align = "center">
    <figure>
	<img src="/img/2013/06/praat-info.jpg"
    alt = "Display info about the LongSound object"
    width = "500">
    <figcaption> Display info about the LongSound object.</figcaption>
    </figure>
    </div><p></p>

Here's what it says in the `Praat Info` window:

```bash
Object id: 1
Object type: Sound
Object name: 20111213-1-kiy-ap-framedwordlist
Date: Thu Jun 27 16:45:21 2013

Duration: 347.832 seconds
File name: /Users/amoebe/Documents/mind/proj/kiy-ldc/tutorials/processing-audio-files/your-turn/20111213/raw/20111213-1-kiy-ap-framedwordlist.wav
File type: WAV
Number of channels: 2
Encoding: linear 16 bit little-endian
Sampling frequency: 48000 Hz
Size: 16695936 samples
Start of sample data: 44 bytes from the start of the file
```

Some highlights:

+ `Object name` lists the basename of the file, without the file
  extension.
+  `Duration` tells us that the file is 347.832 seconds in total.  
+ `File name` lists the full path of the file on the hard drive.
+ `File type` lists that the file format is a WAV file, a lossless file format.
+ `Number of channels` indicates that there are 2 channels in the file
  (Channel 1 was for the consultant; Channel 2 for the
  translator/elicitor).
+ `Encoding` indicates that the bit depth is 16 bit. (`little-endian`
  indicates the byte ordering in the file.)  
+ `Sampling frequency` indicates the audio file was sampled at 48000 Hz (or equivalently, 48 kHz)

The sample rate of 48kHz is much higher than needed for working with
speech so we can [downsample](#downsample) the file to keep the file
size down. We also want to
extract just one of the 2 channels, the channel reserved for the
consultant (Channel 1), for further data analysis.

---------------------------------------------------------

## <a id="channel"></a>Extracting a channel ##

None of the file modification steps we show next can be performed on a
`LongSound` object, so you'll need to open
`20111213-1-kiy-ap-framedwordlist.wav` again using the `Open > Read
from file...` command to open the file as a `Sound` object.

<div align = "center">
	<figure>
	<img src="/img/2013/06/praat-read.jpg"
	alt = "Read from file in Praat"
	width = "400">
	<figcaption> <tt>Read from file</tt> command.</figcaption>
	</figure>
	</div><p></p>


You can
also remove the `LongSound` object by selecting it (click on it so
it's highlighted in blue) and clicking the `Remove` button at the
bottom of the object window.

We recorded the elicitation session with two channels,

+ Channel 1 (left channel): consultant
+ Channel 2 (right channel): elicitor/translator

To extract a channel from the stereo audio file, we do the following:

1. With `Sound 20111213/raw/20111213-1-kiy-ap-framedwordlist` selected
   in the Object Window (so that it is highlighted in blue), click on
   the `Convert` menu at the bottom right of the Object window and
   select `Extract one channel...`. 

    <div align = "center">
	<figure>
	<img src="/img/2013/06/praat-extract.jpg"
	alt = "Read from file in Praat"
	width = "500">
	<figcaption> <tt>Extract one channel</tt> command.</figcaption>
	</figure>
	</div><p></p>

2. In the `Sound: Extract channel` dialog box, type `1` in `Channel
   (number, Left, or Right)` to extract the Left Channel, which is the
   consultant's channel for the file and click `OK`. A new `Sound
   20111213/raw/20111213-1-kiy-ap-framedwordlist` object will appear
   immediately under the original one and will be already selected.

3. If you'd like to save this new file, you can do so with the top
   menu command `Save > Save as WAV file...` in a new folder you
   create in `your-turn/20111213/` called `data/`.

4. You can also click on the `View and Edit` button near the top righthand
   corner in the Object Window (with the new Sound object selected) to
   examine the extracted channel. 

---------------------------------------------------------

## <a id="downsample"></a>Downsampling ##

 Below, we downsample the sampling rate of the file
 `20111213-1-kiy-ap-framedwordlist.wav` from 48kHz to 16kHz and write
 the downsampled file to a new file
 `20111213-1-kiy-ap-framedwordlist-stereo.wav` in a new directory in
 `your-turn/20111213/1` we call `data/`. We give the new filename a
 `-stereo` suffix to remind ourselves that this file still has 2
 channels. It's good to keep the stereo (2-channel) file around for
 reference, since it includes information about how items were
 elicited if we need to check those details later.

**Warning: I've had Praat crash on me rather consistently trying to
  resample large files, including when I tried to downsample the
  original audio file `20111213-1-kiy-ap-framedwordlist.wav`. Try
  downsampling *after extracting the consultant's channel*, as
  described [above](#channel).**

1. With the new, single-channel `Sound 20111213/raw/20111213-1-kiy-ap-framedwordlist`
   selected, click on the `Convert` menu at the bottom right of the
   Object window and select `Resample`.

     <div align = "center">
     <figure>
    	<img src="/img/2013/06/praat-resample.jpg"
     alt = "Click on `Resample` command"
     width = "500">
     <figcaption> <tt>Resample</tt> command.</figcaption>
     </figure>
     </div>
	 
2. In the `Sound:Resample` dialog box, type in `16000` in `New
   sampling frequency (Hz)` to resample to 16kHz. You can leave
   `Precision` at the default of `50`. This determines the
   [quality of the interpolation](http://www.fon.hum.uva.nl/praat/manual/Sound__Resample___.html)
   used to reconstruct the signal in resampling. Click `OK`. You may
   have to wait a bit, but a new `Sound
   20111213-1-kiy-ap-framedwordlist` object will appear below the
   original, selected (highlighted in blue).
   
3. If you'd like to save this new file, you can do so with the top
   menu command `Save > Save as WAV file...` in a new folder you
   create in `your-turn/20111213/` called `data/`.

4. You can also check that the sampling rate is indeed 16kHz by
   re-opening the newly saved file as a `LongSound` object and
   displaying information about the audio file, as described in the
   [first section](#display).

[^1]: I don't know of a way to reduce bit depth in Praat. See the
[SoX tutorial](../processing-audio-files-sox/#bit) for a way to do it
with SoX. There is also a way to do it in Audacity by setting `Default
Sample Format` in `Preferences > Quality >` before opening the sound
file in the program, as described in the
[manual](http://manual.audacityteam.org/man/Quality_Preferences).

[^2]: It's critical to open the file as a `LongSound` to get this
information. If you open the file as a `Sound` object using `Open >
Read from file...`, clicking on the `Info` button will display (after
a bit of a wait) properties of the signal like average, min, and max amplitude and will
not display file format or bit depth.
