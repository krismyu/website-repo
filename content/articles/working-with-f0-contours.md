Title: Working with f0 contours
Date: 2013-10-31 11:12
Author: Kristine Yu
status: draft
Tags: ldc-kiy, fieldwork, praat, tutorial
Slug: working-with-f0-contours

This is supplemental material for *The experimental state of mind in
elicitation: illustrations from tonal fieldwork* that follows up on
Section 2.4, which recast Hyman (2007)'s work on tonotactics in
Thlantlang Lai in terms of experimental design. It introduces additional examples of using 
experimental design principles to generalize to elicitation methods
beyond Pike's toneme discovery procedure.

<!-- PELICAN_END_SUMMARY -->


The rest of the tutorial discusses headphones for listening to
speech sound files and how to annotate sound files in Praat and has
the following sections: 

1. [Introduction](#intro)
2. [Headphones](#headphones)
3. [Marking timepoints in sound files](#mark)
4. [Annotating timepoints in sound files](#annot)
 
##<a id="intro"></a> Introduction ##

A soundfile is hard to access data from when it is an undifferentiated
blob. It's really helpful to have timestamps marking relevant events
so that one can easily go right to the part in the recording corresponding to
these events. One might keep a running list of timepoints during the
elicitation session when crucial bits happen. Or one might modify the
soundfile itself to indicate landmarks.

The solution one can implement
in Praat is to keep timepoints and associated events in a text file
called a
[TextGrid](http://www.fon.hum.uva.nl/praat/manual/TextGrid.html),
separate from the audio file. The sound file and the TextGrid can be
opened together to link them via the timepoints (which serve as
[dictionary keys](../organizing-elicitation-items/#hash) so that one
can easily access any given annotated timepoint and/or labeled
event. The advantage of this solution over keeping a running list of
timepoints in a journal is that the annotations can be directly linked
up with the sound file. The advantage of this solution over modifying
the original sound file is that the annotation file is extremely
lightweight and portable (as it is just a plain text file, as shown below) and can be readily
processed with any text processing scripts for efficient batch
processing and modifications to annotations have nothing to do with
the soundfile so there's no potential for accidental changes to the
actual recording or opportunities to corrupt it.

```bash
# The first bit of 20111213-2-kiy-ap-framedwordlist.TextGrid
# I've added some comments to explain what the text means.
# For more on what tiers are, read on in the tutorial.
File type = "ooTextFile"
Object class = "TextGrid"

xmin = 0 # this is a timestamp for the start of the file
xmax = 256.4826875 # timestamp for end of file
tiers? <exists> 
size = 4 # number of tiers
item []: 
    item [1]: # first tier
        class = "IntervalTier" # Tier 1 is an Interval Tier
        name = "target" # name of Tier 1
        xmin = 0 # timestamp for start of Tier 1 
        xmax = 256.4826875 # timestamp for end of Tier 1
        intervals: size = 81 # number of intervals in Tier 1
        intervals [1]: # first interval in Tier 1
            xmin = 0 # timestamp for start of Interval 1 in Tier 1
            xmax = 24.747999999999998 # timestamp: end of Interval 1,Tier 1
            text = "xxx" # the text label for Interval 1, Tier 1
        intervals [2]: # second interval in Tier 1
            xmin = 24.747999999999998 
            xmax = 25.492 
            text = "xxx" 
        intervals [3]: # third interval in Tier 1
            xmin = 25.492 
            xmax = 38.252 
            text = "xxx" 
        intervals [4]:
            xmin = 38.252 
            xmax = 40.17475333677905 
            text = "xxx" 
        intervals [5]:
            xmin = 40.17475333677905 
            xmax = 46.708 
            text = "xxx" 
        intervals [6]:
            xmin = 46.708 
            xmax = 53.724 
            text = "xxx" 
        intervals [7]:
            xmin = 53.724 
            xmax = 54.08763090207048 
            text = "paRai-li:1" 
        intervals [8]:
            xmin = 54.08763090207048 
            xmax = 54.476 
            text = "li-paRai:R" 
```

### Instructions for tutorials ###

The files for the tutorials can be found in my
[here](http://media.krisyu.org/ldc-kiy/tutorials) in
`annotating-audio-files/`
([here](http://media.krisyu.org/ldc-kiy/tutorials/annotating-audio-files/)). If
you download the whole
[annotating-audio-files directory](http://media.krisyu.org/ldc-kiy/tutorials/annotating-audio-files/),
you can navigate to the `your-turn/` sub-directory to access all the files used in the tutorial. 

The `tutorials/annotating-audio-files/demo/` directory contains all
the files used and generated during the tutorial for your
reference. The `your-turn/` directory is for you to play in and
contains only the raw audio file the tutorial works with and one
"blank" TextGrid file.


##<a id="text"></a>Headphones ##

For analyzing sound files, it's helpful to be able to listen to them
through headphones, especially if the signal is weak. Headphones help
isolate the speech signal from the ambient sounds in the external
environment and help make details of the sound more apparent. It's
important to use headphones that have a **flat frequency response** so
that they don't alter the sound quality. Headphones for listening to
music sometimes have bass and/or treble emphasis.

Below, we show a
frequency response comparison from
[www.headphone.com/buildAGraph.php](www.headphone.com/buildAGraph.php)
for four headphones: [Sony MDR-7506][1] (blue),
[Sennheiser HD280 Pro][2] (red), [Superlux HD 668B][3] (green), and
[Sennheiser Momentum][4] (orange). The Superlux HD 668B has bass emphasis with a large plateau
below 100 Hz, and the Sennheiser Momentum has some bass emphasis with
a large dip in frequency response in the treble region around 5000
Hz, and the Superlux HD 668B has a peak for
emphasis in the higher treble range for "higher highs". In contrast,
the Sony MDR-7506 and Sennheiser HD280 Pro both have quite flat
frequency responses: this is what we want for phonetic data analysis. 

[1]: http://pro.sony.com/bbsc/ssr/product-MDR7506
[2]: http://en-us.sennheiser.com/professional-dj-headphones-noise-cancelling-hd-280-pro
[3]: http://avlex.com/products/hd-668b/
[4]: http://en-us.sennheiser.com/over-ear-headphone-momentum-stereo

<div align = "center">
<figure>
<img
src="/static/blog/img/2013/06/freqresponse.png"
alt = "Frequency response comparison for Sony MDR-7506, Sennheiser
HD280 Pro, Superlux HD 668B, and Sennheiser Momentum." width = "1000">
<figcaption>Frequency response comparison for Sony MDR-7506, Sennheiser
HD280 Pro, Superlux HD 668B, and Sennheiser Momentum. [<a href = "http://www.headphone.com/buildAGraph.php">www.headphone.com/buildAGraph.php</a>]</figcaption>
</figure>
</div><p></p>

--------------------------------------------------------

##<a id="mark"></a>Marking timepoints in sound files ##

In this section, we explain how to perform **segmentation** of the
sound file, i.e. how to set down timepoints marking relevant
events. We'll be working with `20111213-2-kiy-ap-framedwordlist.wav`
in `ldc-kiy/tutorials/annotating-audio-files/your-turn/`, which is
already downsampled and includes only the consultant's channel.

### Creating a new TextGrid ###

1. Launch `Praat`.

2. Select `Open > Open long sound file...` from the menu at the top of
the `Praat Objects` window, as shown below.

    <div align = "center">
    <figure>
   	<img src="/static/blog/img/2013/06/praat-long-sound.jpg"
    alt = "Open long sound file in Praat"
    width = "400">
    <figcaption> <tt>Open long sound file</tt> command.</figcaption>
    </figure>
    </div><p></p>
	
3. Select `20111213-2-kiy-ap-framedwordlist.wav` in the directory
   `ldc-kiy/tutorials/annotating-audio-files/your-turn/` and click on
   `Choose`. There should now be a `LongSound
   20111213-2-kiy-ap-framedwordlist.wav` object listed in the Object Window.
   
4. You can [display the audio file information](../processing-audio-files-praat/#display) to confirm that the
   sampling rate is 16kHz, the bit depth is 16-bit, and that there is
   a single channel.

5. The `LongSound 20111213-2-kiy-ap-framedwordlist.wav` object should
   be selected, i.e., highlighted in blue, already. With it selected,
   click on the `Annotate > To Text Grid...` command on the right, as
   shown below:

    <div align = "center">
    <figure>
   	<img src="/static/blog/img/2013/06/praat-annotate.jpg"
    alt = "The <tt>To Text Grid...</tt> command"
    width = "450"><br>
    <figcaption> The <tt>To Text Grid...</tt> command.</figcaption>
    </figure>
    </div><p></p>

6. In the `LongSound: To TextGrid...` dialog box, there are two
   fields: `Tier names` and `Point tiers`. Praat distinguishes between
   two types of timestamps and separates annotation for them into
   different *tiers*:
   
      + **Interval tiers** are for marking events that span some
	    duration, like a vowel, a word, a sentence.
      + **Point tiers** are for marking events that occur
	    instantaneously at a single point in time, like the midpoint
	    of a vowel, the pitch peak in a word, the right edge of a
	    prosodic phrase.
		 
   Include tier names for both interval and point tiers in `Tier
   names`, separated by spaces, and in order from the topmost
   tier (closest to the bottom of the waveform/spectrogram) to
   the bottomost bier (at the bottom of the window). Type in the
   tiernames for any point tiers again in `Point tiers`.

   For our file, we'll start with just an `item` tier, to set
   boundaries for each of the elicitation items, which are listed in
   `20111213-2-kiy-ap-framedwordlist.txt` in `your-turn`. So type
   `item` in the field `Tier names` and leave `Point tiers` blank, and
   click `OK`:

<div align = "center">
<figure>
<img src="/static/blog/img/2013/06/praat-tier-dialog.jpg"
alt = "The LongSound: To Text Grid...dialog box" width = "450"><br>
<figcaption> The <code>LongSound: To TextGrid...</code> dialog box.</figcaption>
</figure>
</div><p></p>

### Editing the TextGrid ###

1. Now there should be a new `TextGrid
   20111213-2-kiy-ap-framedwordlist` object listed under `LongSound
   20111213-2-kiy-ap-framedwordlist.wav` in the Object window. It
   should already be selected. To annotate the sound file in the
   TextGrid, we select both of the objects together. Hit `Shift` and
   left-click on `LongSound 20111213-2-kiy-ap-framedwordlist.wav` to
   select that as well. Then click on `View & Edit`:

    <div align = "center">
    <figure>
   	<img src="/static/blog/img/2013/06/praat-select-objects.jpg"
    alt = "Select the LongSound and TextGrid objects"
    width = "450"><br>
    <figcaption> Select the <tt>LongSound</tt> and <tt>TextGrid</tt> objects.</figcaption>
    </figure>
    </div><p></p>

2. Now the sound file and TextGrid are linked up in a way that you can
   annotate the sound file "directly" and have your annotations stored in the
   TextGrid file! Perhaps the most important thing about working with TextGrids is to
   **remember to save your work**. You can do this with the `File >
   Save TextGrid as text file...` command, shown below:

    <div align = "center">
    <figure>
   	<img src="/static/blog/img/2013/06/praat-save-textgrid.jpg"
    alt = "Save TextGrid as text file... command"
    width = "450"><br>
    <figcaption> <tt>Save TextGrid as text file...</tt> command.</figcaption>
    </figure>
    </div><p></p>

3. The screencast below gives an introduction to
   marking interval boundaries in the textgrid and labeling the
   intervals, including:
   
      + [Creating new tiers and intervals and playing intervals](http://www.fon.hum.uva.nl/praat/manual/TextGridEditor.html)
      + [Navigating the soundfile and textgrid with keyboard shortcuts](http://www.fon.hum.uva.nl/praat/manual/Keyboard_shortcuts.html)

   The files used in the tutorial are in `tutorials/annotating-audio-files/your_turn/`:

   + `20111213-2-kiy-ap-framedwordlist.wav` is the sound file
   + `20111213-2-kiy-ap-framedwordlist.txt` lists the elicitation items elicited
	   
<p align = "center">
<video controls>
  <source src="/static/blog/videos/2013/06/marking-timepoints.mp4" type="video/mp4">
  <source src="/static/blog/videos/2013/06/marking-timepoints.ogv" type="video/ogg">
  Your browser does not support the video tag.
</video>
Screencast: Marking interval boundary timepoints in the TextGrid.
</p>

--------------------------------------------------------

##<a id="annot"></a>Annotating timepoints in sound files ##

We'll finish up with showing how to add textual labels to intervals, and show how to use a script to efficiently do this. 

### Adding text labels to intervals ###

In the screencast below, we show how to add textual annotations to a
TextGrid file. The files used are in `tutorials/annotating-audio-filex/your_turn/`:

+ `20111213-2-kiy-ap-framedwordlist.wav` is the sound file
+ `20111213-2-kiy-ap-framedwordlist.txt` lists the elicitation items elicited
+ `20111213-2-kiy-ap-framedwordlist_item_newlines_blank.TextGrid` is
  the TextGrid we start with, which has boundaries set down already in
  the appropriate places to mark elicitation items.

The screencast includes:

+ Adding textual annotations to label intervals
+ [Using phonetic symbols in textgrid labelling](http://www.fon.hum.uva.nl/praat/manual/Phonetic_symbols.html)		


<p align = "center">
<video controls>
  <source src="/static/blog/videos/2013/06/annotating-timepoints.mp4" type="video/mp4">
  <source src="/static/blog/videos/2013/06/annotating-timepoints.ogv" type="video/ogg">
  Your browser does not support the video tag.
</video>
Screencast: Annotating interval boundary timepoints in the TextGrid.
</p>

### Using a script to semi-automatically label intervals ###

Wait a minute---why are we typing all these labels out again in the
TextGrids when they are already in our textfile
`20111213-2-kiy-ap-framedwordlist.txt`(http://media.krisyu.org/ldc-kiy/tutorials/annotating-audio-files/20111213-2-kiy-ap-framedwordlist.txt)
and spreadsheet `20111213-2-kiy-ap-framedwordlist.xlsx`(http://media.krisyo.org/ldc-kiy/tutorials/annotating-audio-files/20111213-2-kiy-ap-framedwordlist.xlsx)?

Good question! We can save some time and reduce the change of
introducing errors from typos by extracting the labels from the
textfile or spreadsheet and then using a [Praat script](http://www.fon.hum.uva.nl/praat/manual/Scripting.html) to populate the
TextGrid intervals with the labels. We'll show how to extract labels from a
spreadsheet in Excel in the section
[Creating files for semi-automatic TextGrid annotation from Excel](#excel-labels) and how to extract labels from a
textfile using command-line utilities in the section [Extracting labels for TextGrids from text files in the shell](#shell-labels). Then we'll show how to use a Praat script to use these labels to
annotate the intervals in the TextGrid in [Semi-automatic TextGrid annotation with a script](#praat-script).


#### <a id = "excel-labels"></a> Creating files for semi-automatic TextGrid annotation from Excel ####

1. Launch Excel and open `20111213-2-kiy-ap-framedwordlist.xlsx`[here](http://media.krisyu.org/ldc-kiy/tutorials/annotating-audio-files/20111213-2-kiy-ap-framedwordlist.xlsx)
2. Let's say we want to annotate the intervals in the `item` tier in
   the TextGrid file with the orthographic representations for
   Kirikiri. Then we can select the column of Kirikiri (not including
   the header row) and hit `Edit > Copy`:

    <div align = "center">
    <figure>
    <img src="/static/blog/img/2013/06/excel-copy.jpg"
    alt = "Copying the Kirikiri labels from the spreadsheet." width = "450"><br>
    <figcaption>Copying the Kirikiri labels from the spreadsheet.</figcaption>
    </figure>
    </div><p></p>
3. Now we can launch some text-editing application, for instance
   Notepad on Windows or TextEdit for Mac and invoke a Paste
   command. The important thing is to make sure that you are working
   in **plain text**. For instance, if you do an `Edit > Paste`
   command without first invoking `Format > Make Plain Text` in
   TextEdit, you get strange table-like formatting, as shown below.   

    <div align = "center">
    <figure>
    <img src="/static/blog/img/2013/06/textedit-plain.jpg"
    alt = "Make Plain Text in TextEdit." width = "450"><br>
    <figcaption>`Make Plain Text` command in TextEdit.</figcaption>
    </figure>
    </div><p></p>
4. Save your text file. The text files we'll use further on in the
   tutorials are in `tutorials/annotating-audio-files/your_turn/`:
   
	   + [`numeric-labels.txt`](http://media.krisyu.org/ldc-kiy/tutorials/annotating-audio-files/numeric-labels.txt): item numbers
	   + [`kiy-labels.txt`](http://media.krisyu.org/ldc-kiy/tutorials/annotating-audio-files/kiy-labels.txt): Kirikiri orthographic representations


<!--<p align = "center">
<video controls>
  <source src="/static/blog/videos/2013/06/label-from-excel.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
Screencast: Extracting labels for TextGrid annotation from a spreadsheet.
</p>-->

####<a id="shell-labels"></a> Extracting labels for TextGrids from text files in the shell ####

We start with the tab-delimited text file `20111213-2-kiy-ap-framedwordlist.txt`[here](http://media.krisyu.org/ldc-kiy/tutorials/annotating-audio-files/20111213-2-kiy-ap-framedwordlist.txt), which looks like this:

```bash
item    gloss   kirikiri        tone1   tone2   suffix  word1   word2
1       for the bandicoot       paRai li        1       R       benefactive     paRai   li
2       for the bat     torii li        1       R       benefactive     torii   li
3       for the pigeon  maRuu li        1       R       benefactive     maRuu   li
4       for the dog     nabii li        2       R       benefactive     nabii   li
5       for the gecko   kaza li 2       R       benefactive     kaza    li
```

Let's say we want to label the intervals in the TextGrid with the
   Kirikiri orthographic representations. We can extract the
   `kirikiri` column and write it to a new text file `kiy-labels.txt`
   using `cut`:

```bash
cut -f3 20111213-2-kiy-ap-framedwordlist.txt | sed '1d' > kiy-labels.txt
```

The `-f3` says to extract the 3rd field. `sed '1d'` removes the
first line, which is the header `kirikiri`. Here's an extract from
the new file:
	
```bash
amoebe@moebius :: more kiy-labels.txt
paRai li
torii li
maRuu li
nabii li
kaza li
fivaa li
fO li
```

We can do the same to extract the `item` column if we want to label
  the intervals in the TextGrid with numeric item IDs, but another
  way we could create `item` labels is to simply create a new text
  file with the integers 1-24, using `jot`:

```bash
jot 24 1 >> numeric-labels.txt
```
The first 10 lines in the file look like this:

```bash
amoebe@moebius :: more numeric-labels.txt 
1
2
3
4
5
6
7
8
9
10
```
	
It turns out, as we'll see in the [next section](#praat-script),
that it can also be helpful to have blank lines between each
label. These commands do the trick, with some help from `sed
G`; the `sed '$d'` command is for stripping the trailing newline at
the end of the file:

```bash
jot 24 1 | sed G | sed '$d' > numeric-labels-newlines.txt
cut -f3 20111213-2-kiy-ap-framedwordlist.txt | sed '1d' | sed G |
sed '$d' >  kiy-labels-newlines.txt
```

The file `kiy-labels-newlines.txt` looks like this:

```bash
amoebe@moebius :: more kiy-labels-newlines.txt
paRai li

torii li

maRuu li

nabii li

kaza li

fivaa li
```



####<a id="praat-script"></a> Semi-automatic TextGrid annotation with a script ####

In the screencast below, we show how to add textual annotations to a
TextGrid file semi-automatically using a script. First we demonstrate
how to annotated with the `kiy-labels.txt` file and then we annotate
with the `numeric-labels.txt` file. The files used are in `tutorials/annotating-audio-filex/your_turn/`:

+ `20111213-2-kiy-ap-framedwordlist.wav` is the sound file
+ `label_from_text_file2.praat` is the Praat script (which is just a
  text file)
  
+ `20111213-2-kiy-ap-framedwordlist_item_blank.TextGrid` is
  the TextGrid we start with, which has boundaries set down already in
  the appropriate places to mark elicitation items. It also contains
  `xxx` annotations in the intervals between the intervals for
  elicitation items.
+ `kiy-labels.txt` and `numeric-labels.txt` contain the labels that go
  in `20111213-2-kiy-ap-framedwordlist_item_blank.TextGrid`

<p align = "center">
<video controls>
  <source src="/static/blog/videos/2013/06/praat-scripting.mp4" type="video/mp4">
  <source src="/static/blog/videos/2013/06/praat-scripting.ogv" type="video/ogg">
  Your browser does not support the video tag.
</video>
Screencast: Semi-automatic annotation of interval labels in the
TextGrid using a Praat script.
</p>

If you'd like, you can also repeat the procedure with a TextGrid which
has not had `xxx` annotated in the intervals to be ignored. In this
case, the text files with the labels have blank lines between each
label so that the script will skip the intervals to be ignored between
each elicitation item interval (there's only one such junk interval
between each elicitation item interval).

+ `20111213-2-kiy-ap-framedwordlist_item_newlines_blank.TextGrid` is
  another TextGrid we start with, which has boundaries set down already in
  the appropriate places to mark elicitation items. It contains empty
  intervals (no annotations) in the intervals between the intervals for
  elicitation items.
+ `kiy-labels-newlines.txt` and `numeric-labels-newlines.txt` contain the labels that go
  in `20111213-2-kiy-ap-framedwordlist_item_newlines_blank.TextGrid`  

Perhaps the trickiest thing when one is starting out working with
Praat scripts is figuring out how to specify file and directory paths
in the script. 

For Mac OS X, one way to do this is in `Finder`. Right click on the
file of interest (here: `kiy-labels.txt`) and click on `Get info`. The
directory the file is in will come up in `Where` in the
`kiy-labels.txt Info` window, as shown below and you can select and
copy it. You just need to tack on the file name at the end. So on my machine, the path to `kiy-labels.txt` is `/Users/amoebe/Documents/mind/proj/kiy-ldc/tutorials/annotating-audio-files/your-turn/kiy-labels.txt`.

<div align = "center">
<figure>
<img src="/static/blog/img/2013/06/path-mac.jpg"
alt = "Using Get Info to get the file path in Finder." width = "500"><br>
<figcaption>Using <tt>Get Info</tt> to get the file path in <tt>Finder</tt>.</figcaption>
</figure>
</div><p></p>

In Windows, you can copy the file path too in Explorer using the
command `Copy as path`, as described
[here](http://www.pcworld.com/article/251406/windows_tips_copy_a_file_path_show_or_hide_extensions.html). Supposedly
this works in Windows Vista, Windows 7, and Windows 8.

In the shell, the `pwd` command will tell print the working directory:

```bash
[~/ldc/tutorials/annotating-audio-files/your-turn](master *)
amoebe@moebius :: ls
20111213-2-kiy-ap-framedwordlist.TextGrid.blank		       kiy-labels (Autosaved).txt
20111213-2-kiy-ap-framedwordlist.txt			       kiy-labels-newlines.txt
20111213-2-kiy-ap-framedwordlist.wav			       kiy-labels.txt
20111213-2-kiy-ap-framedwordlist_item.TextGrid		       label_from_text_file2.praat
20111213-2-kiy-ap-framedwordlist_item_blank.TextGrid	       numeric-labels-newlines.txt
20111213-2-kiy-ap-framedwordlist_item_newlines_blank.TextGrid  numeric-labels.txt

[~/ldc/tutorials/annotating-audio-files/your-turn](master *)
amoebe@moebius :: pwd
/Users/amoebe/ldc/tutorials/annotating-audio-files/your-turn
```
You can also print the working directory in your command prompt [as I've done](http://www.brudenossg.com/tip2.php). 
