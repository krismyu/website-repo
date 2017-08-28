Title: Preparing data for the LD&C paper
Date: 2013-10-31 11:12
Author: Kristine Yu
Tags: ldc-kiy, fieldwork, praat, tutorial
Slug: preparing-data-for-ldc-paper
Summary: Tutorial for LDC paper: preparing data presented in paper

This is supplemental material for *The experimental state of mind in
elicitation: illustrations from tonal fieldwork* that describes how
the fundamental frequency contours were extracted and plotted in the
paper for the sections illustrating toneme discovery in Kiriri
(Sections 2.2.1 and 2.3.3).

<!-- PELICAN_END_SUMMARY -->

As a starting point, I assume that the raw audio has been
processed as described in the tutorials
[Processing audio (with Praat)](processing-audio-files-praat.html) and
[Processing audio (with SoX)](processing-audio-files-sox.html),
i.e. downsampled to 16 kHz, with Channel 1 (the consultant's channel)
extracted.

Processing and segmenting of the soundfile was done with the free
and open source sound file analysis software
[Praat](http://www.praat.org), and f0 extraction was done using the
RAPT algorithm <code>get_f0</code> (Talkin 1995). 

The procedure for processing the data for each elicitation session
described in the paper is given in the following sections:

1. [20111207-1-kiy-ap-wordlist and 20111207-1-kiy-ap-wordlist](#20111207)
2. [20111208-6-kiy-ap-nps-vps](#20111208)
3. [20111213-1-kiy-ap-framedwordlist](#20111213)

A [references](#references) section follows.

All files used in analysis are available for download in the
<code>preparing-data-for-ldc-paper/</code> [sub-directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/) in the
<code>tutorials/</code>
[directory](http://media.krisyu.org/ldc-kiy/tutorials/).


##<a id="20111207">20111207-1-kiy-ap-wordlist and 20111207-1-kiy-ap-wordlist</a> ##

Data from the elicitation sessions 20111207-1-kiy-ap-wordlist and
20111207-1-kiy-ap-wordlist appears in the paper in Figure 5 in Section
2.2.1. All files used in analysis are available for download
[here](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/). I
detail the procedure for audio file segmenting and annotation and f0
extraction for only 20111207-1-kiy-ap-wordlist below. The procedure
for 20111207-2-kiy-ap-wordlist was identical.

### Initial audio file segmenting and annotation

First, I annotated the audio recording file
[20111207-1-kiy-ap-wordlist.wav](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/data/20111207-1-kiy-ap-wordlist.wav)
and produced the TextGrid
[20111207-1-kiy-ap-wordlist.TextGrid](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/data/20111207-1-kiy-ap-wordlist.TextGrid),
following procedures in the tutorial on
[annotating sound files](www.krisyu.org/blog/posts/2013/06/annotating-audio-files/). 

Some of the annotation was automated. First, I marked empty intervals,
i.e. intervals without recorded material of interest, with
<code>XXX</code>, so that scripts would ignore those intervals. Then, using the text file
[20111207-1-kiy-ap-wordlist-kiy.txt](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/info/20111207-1-kiy-ap-wordlist-kiy.txt),
I automatically populated TextGrid intervals with labels using a
[Praat script](http://www.fon.hum.uva.nl/praat/manual/Scripting.html)
originally authored by Mietta Lennes,
[label_from_text_file](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/label_from_text_file.praat). I
then used another Lennes script,
[save_intervals_to_wav_sound_files](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/save_intervals_to_wav_sound_files.praat),
to save each of the intervals to separate, short WAV files, one per
elicitation item. These files were automatically named with
incrementing integers, e.g. 20111207-1-kiy-ap-wordlist-kiy-1 for item 1; the file name for each of these individual files
refers to the item code, which can be found in [the dictionary file](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/info/20111207-1-kiy-ap-wordlist.txt). All of these files are in the
<code>tokens</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/data/tokens/).

Finally, I trimmed each of these files with the assistance of a script
[trim_ends](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/trim_ends.praat).
For each file, I manually indicated boundaries to cut off silence at
the beginning and end of the file; the script than moved these
boundaries to the nearest zero crossing (where the audio amplitude was
0) and trimmed the files accordingly. These trimmed files are in the
<code>trimmed</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/data/trimmed/).

### f0 extraction with RAPT (get_f0)

I performed f0 extraction with the following scripts:

1. <code>run_rapt.sh</code> [[script](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/run_rapt.sh)]
2. <code>calc_f0_rapt.sh</code> [[script](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/calc_f0_rapt.sh)]
3. <code>proc_esps_files.py</code> [[script](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/proc_esps_files.py)]

The shell script <code>run_rapt.sh</code> called the shell script
<code>calc_f0_rapt.sh</code> to perform f0 extraction and then the
Python script
<code>proc_esps_files.py</code> to aggregate the f0 data into a single
file and to assign time stamps to f0 values.[^1]

F0 extraction was done at 10ms increments with
[get_f0](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/get_f0);
The [parameter file](http://speechtechie.wordpress.com/2010/05/20/using-an-esps-parameter-file-for-get_f0/) used for extraction was [Pget_f0](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/Pget_f0). Output files have <code>.f0</code> file extensions and are located in the <code>f0</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/f0/). These files were converted
into plain text files with [pplain](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/scripts/pplain), producing output files with <code>.f0.p</code> file extensions, also located in the <code>f0</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/f0/). The aggregated f0 data produced by <code>proc_esps_files.py</code> is <code>espsData.txt</code>, located [here](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/1/analysis/f0/espsData.txt).

### Plot of f0 contours in R

I used the free and open-source statistical software
[R](http://www.r-project.org/) for further data processing---in
particular, Hadley Wickham's [ggplot2](http://ggplot2.org/) package for plotting.

The scripts for generating the plots are available as:

1. <code>plot-20111207-knitr.R</code>: pure R code [[file](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/analysis/plot-20111207-knitr.R)]
2. <code>plot-20111207-knitr.Rnw</code>: Sweave file
   [[file](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/analysis/plot-20111207-knitr.Rnw)],
   with interspersed $\LaTeX$ code and R code, compiled with the R
   package [knitr](http://yihui.name/knitr/) using the
   Makefile [here](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/analysis/Makefile)
3. <code>plot-20111207-knitr.pdf</code>: Output from Sweave file
   [[file](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111207/analysis/plot-20111207-knitr.pdf)]

##<a id="20111208"> 20111208-6-kiy-ap-nps-vps</a>

Data from the elicitation session 20111208-6-kiy-ap-nps-vps appears in
the paper in Tables 2 and 3 and Figures 6 and 7 in Section 2.2.1, as
well as in Table A.1 in the Appendix. All files used in analysis are
available for download [here](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/).

The procedure for analyzing data for 20111208-6-kiy-ap-nps-vps follows
the procedure for 20111207 detailed above. Files from analysis are:

1. Dictionary file: [20111208-6-kiy-ap-nps-vps-hash.txt](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/info/20111208-6-kiy-ap-nps-vps-hash.txt)
2. Original wav file: [20111208-6-kiy-ap-nps-vps.wav](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/data/20111208-6-kiy-ap-nps-vps.wav)
3. Textgrid: [20111208-6-kiy-ap-nps-vps.TextGrid.trim](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/data/20111208-6-kiy-ap-nps-vps.TextGrid.trim)
4. Individual item files: <code>tokens/</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/data/tokens/)
4. Trimmed individual files: <code>trimmed/</code>
   [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/data/trimmed/)
5. f0 output files: <code>f0/</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/analysis/f0/)   
5. Code for plotting figures:
   [[R code](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/analysis/plot-20111208-knitr.R),
   [Sweave](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/analysis/plot-20111208-knitr.Rnw),
   [Makefile](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/analysis/Makefile), [pdf](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111208-6/analysis/plot-20111208-knitr.Rnw)]


##<a id="20111213"> 20111213-1-kiy-ap-framedwordlist</a>

Data from the elicitation session 20111213-1-kiy-ap-framedwordlist appears in
the paper in Tables 5-7 and Figures 9-11 in Section 2.3.3, as
well as in Table A.2 in the Appendix. All files used in analysis are
available for download [here](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/):

1. Dictionary file: [20111213-1-kiy-ap-framedwordlist.txt](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/info/20111213-1-kiy-ap-framedwordlist.txt)
2. Original wav file: [20111213-1-kiy-ap-framedwordlist.wav](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/data/20111213-1-kiy-ap-framedwordlist.wav)
3. Textgrid file: [20111213-1-kiy-ap-framedwordlist.TextGrid](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/data/20111213-1-kiy-ap-framedwordlist.TextGrid)
4. Individual item files: <code>tokens/</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/data/tokens/)
5. f0 output files: <code>f0/</code> [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/analysis/f0/)   
5. Code for plotting figures:
   [[R code](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/analysis/plot-20111213-knitr.R),
   [Sweave](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/analysis/plot-20111213-knitr.Rnw),
   [Makefile](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/analysis/Makefile), [pdf](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/analysis/plot-20111213-knitr.Rnw)]

The analysis procedure for 20111213-1-kiy-ap-framedwordlist closely
followed the procedures given above, except that no trimming
occurred. Instead, timestamps for the beginning and end of the
intervals corresponding to the first and second words in the
disyllabic items were collected with a shell script
<code>get_timestamps.sh</code> 
[here](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/analysis/scripts/get_timestamps.sh). This
script extracted the timepoints marking the boundaries of the
segmented words from the TextGrid file
[20111213-1-kiy-ap-framedwordlist.TextGrid](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/data/20111213-1-kiy-ap-framedwordlist.TextGrid). The
output from the script was <code>word-timestamps.txt</code>
[here](http://media.krisyu.org/ldc-kiy/tutorials/preparing-data-for-ldc-paper/20111213-1/analysis/word-timestamps.txt). These
timestamps were used to split extracted f0 contours into the f0
contour over word 1 and the f0 contour over word 2 in each disyllabic
utterance in R. 

Also, time-normalized f0 plots were produced: mean f0 calculated over
each of 30 frames of equal duration over each word. The functions in the
R code that performed this were <code>extract.samples</code>,
<code>extract.rapt.mean.f0.samp</code>, and
<code>cast.f0</code>. Warning: these functions are not written to work
efficiently and I'm sure they could be improved!! See the R code files
for details on the functions.


[^1]: There is a [known round-off error for get_f0](http://harris.sas.upenn.edu/pipermail/splunch/2010-March/000240.html) which is not
accounted for in the script, but the error happens to not occur for
the sampling rate of the recorded file and the timestep for f0
extraction chosen here.

##<a id="references">References</a> ##

1. Talkin, David. 1995. A robust algorithm for pitch tracking
   (RAPT). In Speech coding and synthesis, ed. W. B. Kleijn and
   K. K. Paliwal, 495–518. Elsevier Science Inc.


