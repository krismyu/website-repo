Title: Processing audio files (with SoX)
Date: 2013-06-23 16:45
Author: Kristine Yu
Tags: ldc-kiy, fieldwork, coding, shell, sox, audio
Slug: processing-audio-files-sox

This tutorial introduces how to process audio files from fieldwork
recordings with [SoX](http://sox.sourceforge.net/), a command-line
utility for working with soundfiles.[^1] See the tutorial
[Processing audio (with Praat)](processing-audio-files-praat.html) for
the sister tutorial using Praat.

<!-- PELICAN_END_SUMMARY -->

Following an <a href = "#intro">introductory section</a>, the tutorial
shows how to use [SoX](http://sox.sourceforge.net/) command utilities to view information about a
soundfile, make three different modifications to the soundfile, and
batch process audio files:

+ <a href="#display">Displaying information about the audio file</a>
+ <a href="#downsample">Downsampling the audio file</a>
+ <a href="#bit">Reducing the bit depth of the file</a>
+ <a href="#channel">Extracting a single channel from the file</a>
+ <a href="#batch">Batch processing</a>

##<a id="intro"></a> Introduction ##

What is SoX? The [homepage for SoX](http://sox.sourceforge.net/) calls it "the Swiss Army knife of
sound processing programs" and gives the following description:

> SoX is a cross-platform (Windows, Linux, MacOS X, etc.) command line utility that can convert various formats of computer audio files in to other formats. It can also apply various effects to these sound files, and, as an added bonus, SoX can play and record audio files on most platforms.

Why [use][1] [the][2] [command line][3] for processing audio files?
As a set of command line utilities, SoX is especially fast for batch processing of audio
files. SoX commands can also be strung together with each other as
well as any other shell command on the command line as part of a
script. We'll get a flavor of this in the tutorial section on <a href="#batch">batch
processing</a>. 

[1]: http://www.computerhope.com/issues/ch000619.htm "Computer Hope general comparison"
[2]: http://www.linuxdevcenter.com/pub/a/linux/2001/11/15/learnunixos.html "Linux Dev Center"
[3]: http://www.linfo.org/command_line.html


Some materials to help get started with SoX include:

+ [The official SoX documentation](http://sox.sourceforge.net/Docs/Documentation)
+ [Bill Poser's SoX tutorial](http://billposer.org/Linguistics/Computation/SoxTutorial.html)
+ [Geek Stuff tutorial](http://www.thegeekstuff.com/2009/05/sound-exchange-sox-15-examples-to-manipulate-audio-files/)

Check the official SoX website for the most up-to-date documentation. The two tutorials listed are a bit outdated, but still useful for getting started.

### The command line ###

For a command-line interface, Mac users can use the built-in [Terminal application](http://guides.macrumors.com/Terminal). Linux users have built-in [terminal emulators](http://linuxcommand.org/lts0010.php#xterm) as well. PC Users need to install a terminal emulator like [cygwin](http://www.cygwin.com/).

We're not going to review using the command line here, but here is a list of some introductory tutorials.

+ [Lifehacker: A command line primer for beginners](http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything)
+ [mactuts: navigating the terminal](http://mac.tutsplus.com/tutorials/terminal/navigating-the-terminal-a-gentle-introduction/)
+ [Lifehacker: introduction to cygwin](http://lifehacker.com/179514/geek-to-live--introduction-to-cygwin-part-i)

And here are a few more in-depth tutorials that are on-line:

+ [Software Carpentry: The shell](http://software-carpentry.org/4_0/shell/index.html)
+ [University of Surrey](http://www.ee.surrey.ac.uk/Teaching/Unix/)

For a book-length treatment, you might try the
[O'Reilly](http://oreilly.com/) series book, [Learning the Unix Operating System](http://shop.oreilly.com/product/9780596002619.do).


### Instructions for tutorials ###

The files for the tutorials can be found in
[this directory](http://media.krisyu.org/ldc-kiy) under
`tutorials/processing-audio-files` ([here](http://media.krisyu.org/ldc-kiy/tutorials/processing-audio-files/)). Once you've downloaded the ldc-kiy repository, you can enter commands yourself to follow along with the tutorial.

In the ldc-kiy directory, change the working directory to the `tutorials/processing-audio-files` directory with the `cd` command and list the directory contents with `ls`:

```bash
#change working directory to tutorial directory
cd tutorials/processing-audio-files
ls # list directory contents
```

You should see something like this in your terminal:

```bash
amoebe@moebius :: ls
demo/      your-turn/
```

The `demo/` directory contains all the files used and generated during the tutorial for your reference. The `your-turn/` directory is for you to play in and contains only the raw audio files the tutorial works with, and not any of the generated files from the tutorial. The rest of the tutorial will assume that the user starts in the directory `ldc-kiy/tutorials/processing-audio-files/your-turn/`.

---------------------------------------------------------

## <a id="display"></a>Displaying audio file information ##

In the `your-turn/` directory, navigate to `20111213/raw/` and see
what's in there:

```bash
cd 20111213/raw/ # navigate from the your-turn directory
ls # display directory contents
```

You'll see that there is a wav file in `your-turn/20111213/raw`:

```
amoebe@moebius :: ls
20111213-1-kiy-ap-framedwordlist.wav
```

We can use sox to display information about the wav file as follows:

```bash
sox --i 20111213-1-kiy-ap-framedwordlist.wav # display audio file header info
```

The output from the `sox --i` command is given below. 

```bash
Input File     : '20111213-1-kiy-ap-framedwordlist.wav'
Channels       : 2
Sample Rate    : 48000
Precision      : 16-bit
Duration       : 00:05:47.83 = 16695936 samples ~ 26087.4 CDDA sectors
File Size      : 66.8M
Bit Rate       : 1.54M
Sample Encoding: 16-bit Signed Integer PCM
```

+ `Input File` lists the file name.
+ `Channels` indicates that there are 2 channels in the file (Channel 1 was for the consultant; Channel 2 for the translator/elicitor)
+ `Sample rate` indicates the audio file was sampled at 48000 Hz (or equivalently, 48 kHz)
+ `Precision` tells us the precision or bit depth of the file, 16-bit.
+  Note that the `file size` is 66.8 megabytes for a recording with a `duration` of just `00:05.47.83`, i.e., just under 6 minutes!

The sample rate of 48kHz is much higher than needed for working with
speech so we can [downsample](#downsample) the file to keep the file
size down. We also want to
extract just one of the 2 channels, the channel reserved for the
consultant (Channel 1), for further data analysis.

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

Starting in `your-turn/20111213/1/raw/`:

```bash
# create new data sub-directory in parent directory 1/
mkdir ../data 

# downsample to 16kHz and write to file in data/
# '-r 16k' specifies resampling at a 16kHz sampling rate
sox 20111213-1-kiy-ap-framedwordlist.wav -r 16k ../data/20111213-1-kiy-ap-framedwordlist-stereo.wav
```

We can change the working directory to the directory with the new downsampled file and display the audio file information:

```bash
cd ../data/ # change working directory to directory with downsampled file
sox --i 20111213-1-kiy-ap-framedwordlist-stereo.wav
```

Note in the displayed info below that the the sample rate of this new file is 16000 Hz (16kHz), as desired. Moreover, the file size has dropped from 66.8 MB to 22.3MB.

```bash
Input File     : '20111213-1-kiy-ap-framedwordlist-stereo.wav'
Channels       : 2
Sample Rate    : 16000
Precision      : 16-bit
Duration       : 00:05:47.83 = 5565312 samples ~ 26087.4 CDDA sectors
File Size      : 22.3M
Bit Rate       : 512k
Sample Encoding: 16-bit Signed Integer PCM
```

---------------------------------------------------------

## <a id="bit"></a>Reducing bit depth ##

We can tweak the downsampling command slightly to get the command
needed to reduce the [bit depth](http://wiki.audacityteam.org/wiki/Bit_Depth) of an audio file:

```bash
cd ../raw/ # change back to the raw/ directory

# '-b 16' specifies reducing bit depth to 16 bit
sox 20111213-1-kiy-ap-framedwordlist.wav -b 16 ../data/20111213-1-kiy-ap-framedwordlist-stereo.wav 
```

Since the original file precision was already `16-bit`, there is no
change to the precision so the output from `sox --i` in `data/` would remain the same
as before. 

It is also possible to combine the commands for downsampling and
changing precision, as follows (starting in the `raw/` directory):

```bash
# '-b 16' specifies converting to a bit depth of 16 and 'r 16k' indicates converting to a sampling rate of 16kHz.
sox 20111213-1-kiy-ap-framedwordlist.wav -b 16 -r 16k ../data/20111213-1-kiy-ap-framedwordlist-stereo.wav
```
---------------------------------------------------------

## <a id="channel"></a>Extracting a channel ##

We recorded the elicitation session with two channels,

+ Channel 1 (left channel): consultant
+ Channel 2 (right channel): elicitor/translator

To extract a channel from the stereo audio file, we use the `remix`
effect: for an input file with 2 channels, `remix 1 0` selects Channel
1, while `remix 0 1` selects Channel 2.[^2] Here, we select Channel 1
using `remix 1 0` to extract the consultant's channel from the
downsampled stereo file `20111213-1-kiy-ap-framedwordlist-stereo.wav`
in `data/` and write to a new file in `data/` we call
`20111213-1-kiy-ap-framedwordlist.wav`. Starting from the `raw/`
directory where we left off:

```bash
# change directory to data/ sub-directory from raw/ sub-directory
cd ../data/
sox 20111213-1-kiy-ap-framedwordlist-stereo.wav 20111213-1-kiy-ap-framedwordlist.wav remix 1
```

Alternatively, this command is less terse and does the same thing:

```bash
# '-c 1' specifies the output file to have 1 channel
# 'remix' selects and mixes input audio channels into output audio channels
sox 20111213-1-kiy-ap-framedwordlist-stereo.wav -c 1 20111213-1-kiy-ap-framedwordlist.wav remix 1 0

```

Putting all 3 changes together, we can also combine all of them as one
command as follows, sidestepping the creation of the downsampled
stereo file in `data/`:

```bash
cd ../raw
sox 20111213-1-kiy-ap-framedwordlist.wav -b 16 -r 16k ../data/20111213-1-kiy-ap-framedwordlist-stereo.wav remix 1
```
---------------------------------------------------------

## <a id="batch"></a>Batch processing ##

The real power of SoX comes when you're trying to perform the same
operation on a bunch of audio files at once. We present an example of
batch processing audio files with SoX below to give you a flavor.

The relevant files for this demo are in `your-turn/batch-demo/`.

```bash
# Change the working directory to batch-demo/ from 20111213/1/data/ or 20111213/1/raw/
cd ../../batch-demo

ls # list directory contents
```

You'll see there are 11 wav files in the directory:

```bash
amoebe@moebius :: ls
20111213-1-kiy-ap-framedwordlist-1.wav   20111213-1-kiy-ap-framedwordlist-15.wav
20111213-1-kiy-ap-framedwordlist-10.wav  20111213-1-kiy-ap-framedwordlist-16.wav
20111213-1-kiy-ap-framedwordlist-11.wav  20111213-1-kiy-ap-framedwordlist-17.wav
20111213-1-kiy-ap-framedwordlist-12.wav  20111213-1-kiy-ap-framedwordlist-18.wav
20111213-1-kiy-ap-framedwordlist-13.wav  20111213-1-kiy-ap-framedwordlist-19.wav
20111213-1-kiy-ap-framedwordlist-14.wav
```
Suppose we'd like to find out the duration of each of these 11 wav
files. We can do this with an additional option for `sox --i`, say,
for the file `20111213-1-kiy-ap-framedwordlist-1.wav`:

```bash
sox --i -D 20111213-1-kiy-ap-framedwordlist-1.wav
```
and we find out that `20111213-1-kiy-ap-framedwordlist-1.wav` has a
duration of 0.804 seconds:

```bash
amoebe@moebius :: sox --i -D 20111213-1-kiy-ap-framedwordlist-1.wav
0.804000
```
We can do this for each of the 11 wav files with a single command,
using
[file globbing](http://www.tldp.org/LDP/abs/html/globbingref.html),
which allows use of the wildcard `*` to perform filename expansion:

```bash
# The wildcard * allows any string of characters between - and .wav
# (with some hedges for `any', see
# http://www.tldp.org/LDP/abs/html/globbingref.html for details)

sox --i -D 20111213-1-kiy-ap-framedwordlist-*.wav

# This is equivalent to a sequence of sox --i -D commands, one for
# each of the 11 files with filenames matching 20111213-1-kiy-ap-framedwordlist-*.wav
```
which gives us the output:

```bash
amoebe@moebius :: sox --i -D 20111213-1-kiy-ap-framedwordlist-*.wav
0.804000
0.863500
0.832625
0.827750
0.793188
0.869062
0.903687
0.996812
0.922500
0.796438
0.933625
```
This is a lot faster than opening each audio file in some program and
checking how long each one is.

We can also chain together shell commands. Suppose we want to save
these durations to a log file called `durations.txt`. We can easily
create such a file, with the first column indicating which filenumber 1-11
the duration corresponds to.

```bash
paste -d'\t' <(jot 11 1) <(sox --i -D 20111213-1-kiy-ap-framedwordlist-*.wav) > durations.txt
```

We can use the `more` command to view the content of the text file `durations.txt`:

```bash
amoebe@moebius :: more durations.txt
1       0.804000
2       0.863500
3       0.832625
4       0.827750
5       0.793188
6       0.869062
7       0.903687
8       0.996812
9       0.922500
10      0.796438
11      0.933625
```

[^1]: SoX is used in the backend of
[Toney](https://github.com/langtech/toney), the tone classification
software developed by Haejoong Lee and Steven Bird as part of the NSF project [Prosodic Systems in New Guinea](http://www.prosodicsystems.org/).

[^2]: SoX used to have an `avg` effect you could use for this, which
is still listed in various SoX tutorials. The
`avg` effect is now deprecated. Use `remix` instead.
