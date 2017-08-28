Title: Recording in the field
Date: 2013-06-23 16:45
Author: Kristine Yu
Tags: ldc-kiy, fieldwork, tutorial
Slug: recording-in-the-field
Summary: Tutorial for LDC paper: notes on recording in the field

This tutorial sketches some suggestions for recording equipment, for
recording practices, and for
audio file specifications of recorded data in the field. The outline
for the tutorial is as follows:

+ [Notes on recording practices](#practices)
+ [Notes on recording equipment](#equipment)
    + [Microphones and accessories](#mics)
    + [Audio recording devices](#recording)
+ [Audio file specifications](#audio)

## <a id = "practices"></a>Notes on recording practices ##

+ **Maximize the consultant's comfort.** Be culturally sensitive
   during recording and respect your consultant. For instance, your consultant might feel
   uncomfortable if you adjust recording equipment attached to his/her
   body. Walk them through everything you're doing and make sure they
   are okay with it. Try to keep the consultant's
   awareness of the recording equipment and procedure fairly low so
   that they can relax as much as possible and speak naturally. If
   possible, try to have some water handy so they can drink if they
   get thirsty. Take breaks.
   
+ **Have your research questions in mind.** What the best recording
  practices are depends on your research questions, so keep those in
  mind. For instance, if you are interested in studying the acoustic
  realization of obstruents, it would be imperative to record in a
  quiet environment, a sound-attenuated booth if possible. This is
  because any background noise could easily swamp release bursts. However,
  if your research question only involves studying fundamental
  frequency, having a pristinely quiet environment isn't as crucial. It's more
  important to insure that the speech signal has a healthy amplitude
  in the recording. Low amplitude signals can make it difficult to
  identify repeating patterns for f0 estimation algorithms.
  
+ **Don't forget to record the elicitor, too.** If the elicitation
  session involves back-and-forth between the elicitor and consultant,
  then a recording can be fairly useless without including what the
  elicitor said. For instance, I've done blick testing (Could this be
  a word in your language?) where I didn't pay attention to recording
  myself and ended up incomprehensible recordings of "Yes. No. Yes."
  etc. Fortunately, the recording just barely picked up what was being
  elicited, but it's better to purposely set up a recording environment to
  record both the consultant and the elicitor. One can do this either
  by miking up both the consultant and the elicitor and making a
  stereo recording with separate channels for the consultant and
  elicitor, or by using a separate recorder for recording both the
  consultant and the elicitor and whatever else is going on in the
  surrounding environment with the recorder's internal mics.
  
+ **Maximize
  [signal to noise ratio](http://www.dspguide.com/ch25/3.htm).** Even
  if the speech signal is high amplitude, that's not enough for good
  signal quality. If the speech signal is high amplitude but there's
  torrential rain pouring down a few feet away, signal quality will be
  compromised. If the speech signal is low-level, but you're in a
  quiet room, signal quality could still be fine for analysis. The
  higher level the speech signal, the higher the signal to noise
  ratio. The higher the background noise level, the lower the signal
  to noise ratio.
  
+ **Keep background noise to a minimum.** It's generally a good idea
  to try to record in a quiet environment. A quiet back room is good
  if available. Try to avoid overhead fans, construction, animal
  noises, etc. Sometimes it could be worth waiting out weather-related
  noise if practical.

+ **Maximize amplitude of speech signal (but avoid
  [clipping](http://avp.stackexchange.com/questions/446/what-is-clipping-distortion-what-causes-it-and-how-to-avoid-it-when-recordin)).**
  You want your recording setup (including distance from mic to
  speaker, preamp(lifier) setup, recorder setup) to maximize the speech signal
  level without causing signal distortion. The mic should be close to
  the consultant's mouth, a little off to the side to avoid pops from
  noise bursts. Having a [preamp](http://www.sweetwater.com/insync/mic-preamp-buying-guide/) in
  your recording setup is essential both to boost the signal level and
  to allow for easy adjustment of input levels during recording. But if you overload the mic
  preamplifier, you can get signal distortion, including clipping,
  which occurs when the amplitude of the signal exceeds the capacity
  of the preamplifier, as shown below, when the recorded signal
  exceeds the maximum range ([-1.0, 1.0] for Audacity, as shown below). If clipping occurs, it
  introduces the artifact of high frequency components to the signal,
  which is particularly problematic if you're interested in any kind
  of spectral analysis of the speech.

<div align = "center">
  <figure>
	<img
  src="/img/2013/06/clipping-audacity.gif"
  alt = "Demonstration of clipping during recording in an audio file in Audacity"
  width = "1000">
  <figcaption> Demonstration of clipping during recording in an audio file in Audacity</figcaption>
</figure>
</div><p></p>

 Audio recording software and devices usually have a meter you can
 observe to monitor the input level to maximize the input level
 without clipping. We show an example of a
 [meter tool](http://manual.audacityteam.org/man/Meter_Toolbar) from
 Audacity below. The red bar to the right shows the recording level. If it
 goes past the blue line, we get clipping. In other recording software
 and for other recording devices, sometimes the meter tool will change
 color from green to red when the input level is too high.
 
<div align = "center">
  <figure>
	<img
  src="/img/2013/06/meter-audacity.jpg"
  alt = "Meter tool in Audacity"
  width = "400">
  <figcaption> <a href="http://manual.audacityteam.org/man/Meter_Toolbar">Meter tool</a> in Audacity for monitoring input levels. </figcaption>
</figure>
</div><p></p>

+ **Keep recordings on the shorter side and consider making summary recordings.** Consider breaking up a
  recording of a longish elicitation session into several audio
  files. This keeps file sizes smaller and if for any reason the file
  is damaged in any way or some technical difficulties occur, those
  issues will be localized to a smaller portion of the elicitation
  session. I generally try to keep recordings no longer than 10-15
  minutes. The downtime between the recordings also gives you and the
  consultant the chance to take a break and perhaps change batteries
  or the memory card if needed.

  It's a good idea to record
  entire elicitation sessions, but it may also be helpful to record
  "summary sessions", where you consolidate the elicitation items into
  a densely packed session. Such shorter densely packed sessions allow high
  quality recording with lossless file formats without having gigantic
  file sizes.
  
+ **Keep your audio files organized and backed up.** Copy your
  recorded audio files to additional storage devices as soon as
  possible after an elicitation session. Name your audio files [systematically](../organizing-elicitation-items#files).

--------------------------------------------

## <a id="equipment"></a>Notes on recording equipment ##

Now that we have an idea of the issues involved in thinking about a
recording setup, we'll consider recording equipment:

+ [Microphones and accessories](#mics)
+ [Audio recording devices](#recording)

### <a id="mics"></a> Microphones and accessories ###

Some general properties that are desirable for mics in the field are that they:

+ **Are comfortable.** This helps reduce the consultant's awareness of
  the recording procedure and makes a potentially unfamiliar process
  more friendly.
  
+ **Reject background noise.** To maximize signal to noise ratio
  especially in potentially unavoidably noisy field conditions.
  
+ **Rugged.** To withstand wear and tear.

An example of a mic that fits the bill is the
<a
href="http://www.shure.com/americas/products/microphones/sm/sm10a-headworn-microphone"
title="Shure SM10A" target="_blank">Shure SM10A</a> headworn mic,
pictured below (left).

<div align = "center">
  <figure>
    <img
  src="http://cdn.shure.com/product/main_image/3566/prod_img_sm10a_l.jpg"
  alt="http://cdn.shure.com/product/main_image/3566/prod_img_sm10a_l.jpg"
  width="300">
    <img
  src="http://cdn.shure.com/product/main_image/3751/prod_img_x2u_l.jpg"
  alt="http://cdn.shure.com/product/main_image/3751/prod_img_x2u_l.jpg"
  width="300">
    <figcaption>Sample recording equipment for fieldwork:<br> (l-r) Shure SM10A
  microphone
  [<a href = "http://cdn.shure.com/product/main_image/3566/prod_img_sm10a_l.jpg">Shure</a>];
  Shure X2u XLR to USB adapter [<a href = "http://cdn.shure.com/product/main_image/3751/prod_img_x2u_l.jpg">Shure</a>]</figcaption>
  </figure>
</div><p></p>

It's headworn and lightweight and adjustable, and it is pretty comfortable for long periods of time. Another nice
property of headworn mics is that the distance from the mic to the
sound source is quite easy to keep constant. To keep the distance from
a tabletop mic to the sound source constant, you have to be careful
about exactly where the consultant is sitting and where his/her mouth
is, etc. and be strict about the consultant holding still. If the
distance between the mic and the soundsource fluctuates, the input level also fluctuates.

One other nice property of the Shure SM10A is that it is a
[*dynamic*](http://homerecording.about.com/od/microphones101/a/mic_types.htm)
[rather than](http://shure.custhelp.com/app/answers/detail/a_id/742/) [a condenser microphone](http://www.sweetwater.com/insync/studio-microphone-buying-guide/)
and requires no power supply for the generation of the audio
signal. Dynamic mics tend to be more rugged and are
moisture-resistant---good properties for the field.

The Shure SM10A is also *unidirectional*, which makes it great at
rejecting background noise and indispensible for working in
unavoidably noisy field environments. One drawback as a consequence is that there
is a [proximity effect](http://shure.custhelp.com/app/answers/detail/a_id/2844),
a boost in bass frequencies when the microphone is very close to the
sound source. This proximity effect means that one should be cautious
about directly comparing absolute values of acoustic spectral
properties of the speech signal between recordings when different
recording equipment is used, but this is not something that is
typically done anyway, since it's the relative acoustic properties in
speech sound contrasts that is most often of interest.

A more significant drawback because of the small size of the mic, in
particular, because of its
[small magnet](http://shure.custhelp.com/app/answers/detail/a_id/1867/),
the signal from the mic is usually
[fairly weak](http://www.sweetwater.com/sweetcare/articles/what-nominal-level-of-shure-sm10a-headworn-microphone-little/),
even if the mic is very close to the mouth as it should be, but this
is acceptable as long as the signal to noise ratio is high.

For recording directly to computer, an additional valuable mic
accessory is an external A/D converter and preamp, as we discussed in
[Notes on recording practices](#practices). One such device is the <a
href="http://www.shure.com/americas/products/accessories/microphones/microphone-problem-solvers/x2u-xlr-to-usb-signal-adapter"
title="Shure X2u XLR-to-USB" target="_blank">Shure X2u</a> (see
picture above right), which
accepts a male XLR connector (shown below) and plugs into a USB
port. You may also want
[a cable to connect two XLR outputs to one XLR input](http://www.amazon.com/dp/B000068O58) if you want to record two
channels at once, e.g. one for the consultant and one for the elicitor. 


<div align = "center">
  <figure>
	<img
  src="http://upload.wikimedia.org/wikipedia/commons/1/15/Xlr-connectors.jpg"
  alt = "XLR connectors, from http://commons.wikimedia.org/wiki/File:Xlr-connectors.jpg"
  width = "300">
  <figcaption>XLR connectors, (l-r) female and male [<a href="http://upload.wikimedia.org/wikipedia/commons/1/15/Xlr-connectors.jpg">wikimedia</a>]</figcaption>
</figure>
</div></p></p>

### <a id="recording"></a> Audio recording devices ###

<div align = "center">
  <figure>
    <img
  src="http://www.samsontech.com/site_media/cms/images/product/zoom/handheld-audio-recorders/handheld-audio-recorders/h4n/H4n_slant-display.jpg"
  alt = "http://www.samsontech.com/site_media/cms/images/product/zoom/handheld-audio-recorders/handheld-audio-recorders/h4n/H4n_slant-display.jpg
" width="350">
    <img src="http://www.roland.com/products/en/R-44/images/top_L.jpg"
  alt = "http://www.roland.com/products/en/R-44/images/top_L.jpg" width="350">
    <figcaption>Sample audio recording devices for fieldwork:<br>
  (l-r) Zoom H4n handheld recorder
  [<a href = "http://www.samsontech.com/site_media/cms/images/product/zoom/handheld-audio-recorders/handheld-audio-recorders/h4n/H4n_slant-display.jpg">Samsontech</a>]; Roland R-44 field recorder [<a href = "http://www.roland.com/products/en/R-44/images/top_L.jpg">Roland</a>]</figcaption>
  </figure>
</div><p></p>

For audio recording devices, some general desirable properties for
recording in the field are that they:

+ **Are portable and robust to mechanical stress.** To withstand the rigors of
  field environment. Portable recorders currently on the market generally accept
  [SD cards](http://www.howstuffworks.com/secure-digital-memory-cards.htm),
  which use
  [flash memory](http://computer.howstuffworks.com/flash-memory.htm)
  for disk storage. Flash memory is great for the field since it uses
  no moving parts, and is thus noiseless as well as robust to mechanical stress.
  
+ **Allow multichannel recording.** So you can record a dyad of two or
  more consultants or record the consultant and the elicitor.
  
+ **Have good quality built-in preamps.** You can have separate
  preamps, but it's nice to have them built into your recorder.
  
+ **Support lossless audio file formats and high-quality recording.**
  It's a very bad idea to perform phonetic analysis with lossy audio
  file formats like MP3s. But lossy audio file formats might be the
  only practical choice for recordings of hours of recording
  sessions. More on settings for audio files in the
  [next section](#audio).
  
+ **Have inputs appropriate for your mic setup without any adaptors.**
  You want your recording device to work seamlessly with your mic
  setup. Each interface between devices can introduce noise into the signal.

Two examples of audio recorders with these properties that I've had good experiences with are the [Zoom H4n handheld recorder][1] and the [Roland R-44 field recorder][2], pictured above,
with specs listed below.

[1]: http://www.samsontech.com/zoom/products/handheld-audio-recorders/h4n/
[2]: http://www.roland.com/products/en/R-44/

<table>
	<thead>
		<tr>
			<td>Device</td>
			<td>Precision/bit depth (bit)</td>
			<td>Sampling rate (kHz)</td>
			<td>Input</td>
			<td>Memory storage</td>
			<td>Power supply</td>
			<td>Size/weight</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><a href="http://www.samsontech.com/zoom/products/handheld-audio-recorders/h4n/" title="Zoom H4n" target="_blank">Zoom H4n</a>
</td>
			<td>16, 24</td>
			<td>44.1, 48, 96</td>
			<td>4 XLR inputs with phantom power </td>
			<td>SD, SDHC, up to 32GB cards</td>
			<td>AC adaptor (DC5V/1A/center plus) <br> AA size (LR6) battery x 2</td>
			<td>70(W) x 156.3(D) x 35(H)mm <br> 280g (without batteries)</td>
		</tr>
		<tr>
			<td><a href = "http://www.roland.com/products/en/R-44/", title="Roland R-44" target="_blank">Roland R-44</a></td>
			<td>16, 24</td>
			<td>44.1, 48, 88.2, 96, 192</td>
			<td>4 XLR inputs with phantom power </td>
			<td>SD, SDHC, 64MB-32GB</td>
			<td>AC adaptor (PSB-1U) <br> AA type battery x 4 (Alkaline or NiMH)</td>
			<td>157(W) x 183(D) x 61(H) mm <br> 1.3 kg with batteries</td>
		</tr>
	</tbody>
</table>

These recorders both have the properties listed above, including XLR
inputs which work with the Shure SM10A headworn mic. Both can record
WAV files at least up to 24-bit/96kHz, which is overkill
for the recording quality necessary in recording speech (most
recorders are designed for the music market). The Zoom H4n is small
but still accepts 2 channels. The Roland R-44 is bigger, but still
easily portable, and accepts 4 channels; it's overall higher-end, but
is rather pricey.

### Recording directly to the computer ###

An alternative to dedicated audio recording devices is to **record
directly to a computer**, i.e. a laptop can also serve as an audio
recording device in the field, especially if you're bringing it along
anyway for other reasons. A couple caveats for recording
directly to a computer are that:

+ **You need to be careful about running other processes simultaneously
while you're recording.** If you have an anti-virus program
continually scanning your hard disk or your computer is backing up
tons of new audio files while you're recording, the system resources
allocated to the audio recording could be affected. This could affect
the fidelity of your recording in unpredictable ways.

+ **You should have a device to perform analog-to-digital conversion
  external to the computer's sound card and to serve as a preamp.** 
[Analog-to-digital conversion](http://www.hardwaresecrets.com/article/317)
  (A/D conversion) 
  converts the continuously varying analog voltage output from a mic into a quantized
  digital signal for the computer. If the A/D conversion is performed
  by a sound card internal to the computer, it can also pick up
  computer-internal noise. A
  [preamp](http://www.sweetwater.com/insync/mic-preamp-buying-guide/)
  boosts the microphone signal and is important to get the speech
  signal to level useable for signal processing like pitch tracking.

+ **You may need to be more careful about mechanical stress.** Many
laptops nowadays still come with spinning hard drives, which are
vulnerable to damage from mechanical stress like bumpy truck rides and
falling. If you record directly to the computer without backing up
somewhere else, you leave your recorded files vulnerable to being lost
from hard disk
failure. [Solid state drives](http://www.pcmag.com/article2/0,2817,2404258,00.asp)
are becoming more and more common and more affordable and are more reliable under
significant mechanical insult.

There is versatile and powerful
[free and open source](http://freeopensourcesoftware.org/index.php?title=Main_Page),
cross-platform (Windows/Mac OS X/Linux) audio recording/editing
software such as [Audacity](http://audacity.sourceforge.net/) and
[Praat](http://www.praat.org) available to use if you record directly to the
computer. I've also gotten and continue to get good use out of a
simple little recording application (Mac OS X only),
[Audio Recorder](http://mac.softpedia.com/get/Audio/Audio-Recorder.shtml),
developed by Ben Shanfelder, but it hasn't been updated
since 2008. See a more extended list of free and open source audio
recording/editing software
[here](http://en.wikipedia.org/wiki/List_of_free_software_for_audio).

--------------------------------------------

## <a id = "audio"></a>Audio file specifications ##

For audio recording devices and software, there's a plethora of
options available for setting properties of the digital audio file. A good review of
digital audio is
[here](http://www.jiscdigitalmedia.ac.uk/guide/an-introduction-to-digital-audio/). We'll
sketch some
guidelines for the most important properties here. 

### Lossless and lossy file formats ###
 There are a
   [variety](http://www.digitalpreservation.gov/formats/fdd/sound_fdd.shtml)
   of digital file formats for sound. The most common file formats
   you'll see in software and recording devices are WAV and MP3. The
   main consideration for recording speech is whether the file format
   is *lossless* or *lossy*. Lossless file formats, e.g. WAV, AIFF,
   FLAC, ALAC may be
   [compressed or uncompressed](http://www.jiscdigitalmedia.ac.uk/guide/uncompressed-audio-file-formats),
   but preserve the original audio in the most accurate digital
   representation possible given the recording settings. Lossy file
   formats, e.g. MP3, MP4, AAC, OGG are all compressed and involve the
   removal of audio data such that the original audio is irrecoverable
   from the file.

   For phonetic data analysis, it's imperative to record with lossless
   file formats like WAV since lossy file formats alter the sound. If
   a recording is done purely for keeping a record of what happened in
   an elicitation, lossy file formats can be appropriate and can yield
   smaller file sizes than compressed lossless file formats. However,
   since space is cheap and ever cheaper, it's likely that file size
   won't be a limiting factor at some point in the forseeable
   future. In addition, someone else may be able to use your recorded
   material as well, who wants to do phonetic analysis, so it's always
   worth considering using lossless file formats when possible.    

### Sampling rate ###

 The sample or sampling rate for an audio file is
   a property of the analog-to-digital conversion of the sound and
   determines the temporal resolution of the recorded signal. In the
   figure below from <a href="http://www.jiscdigitalmedia.ac.uk/images/ITDA-02-sampling1.jpg">JISC
   Digital Media</a>, the sine wave in (a) is sampled at the indicated
   points, giving the digital representation in (b) and (c). (The plot
   in (d) shows the digital representation after some postprocessing).  

<div align = "center">
  <figure>
	<img
  src="http://www.jiscdigitalmedia.ac.uk/images/ITDA-02-sampling1.jpg"
  alt = "Sampling of a sine wave"
  width = "1000">
  <figcaption> The sampling rate of a sine wave controls the temporal
  resolution of its digital representation.
  [<a href="http://www.jiscdigitalmedia.ac.uk/images/ITDA-02-sampling1.jpg">JISC Digital Media</a>]</figcaption>
</figure>
</div><p></p>

  The main consideration for the sampling rate is what the highest
  frequency of interest is; the sampling rate needs to be at least
  twice this frequency to avoid
  [aliasing](http://www.jiscdigitalmedia.ac.uk/guide/an-introduction-to-digital-audio/),
  in which higher frequencies are indistinguishable from lower
  ones. The highest frequencies in speech generally aren't higher than
  5000-6000 Hz, so a sampling rate of 16 000, i.e. 16 kHz is
  sufficient for recording speech, and even 11 kHz can be acceptable,
  depending on the research question.

  However, since recorders are marketed for musicians, the lowest sample rate
  option offered for an audio recorder may be CD quality 44.1kHz. You
  may choose to *downsample* the file later, after recording (see
  [Sox][3] and [Praat][4] tutorials), in order to reduce file size. 

[3]: ../processing-audio-files-sox/#downsample
[4]: ../processing-audio-files-praat/#downsample

### Precision/bit depth ###
  Another property of the analog-to-digital
   audio conversion is the *precision* or *bit depth*. This regulates
   not temporal resolution, like sample rate, but the resolution in
   the *quantization* of the amplitude of the speech signal, as shown
   below. The higher the bit depth is, the less grainy the
   representation of changes in the amplitude of the speech signal.

<div align = "center">
  <figure>
	<img
  src="http://www.jiscdigitalmedia.ac.uk/images/ITDA-05-bitdepth.jpg"
  alt = "Precision/bit depth"
  width = "500">
  <figcaption> Comparison of 2-bit (3 levels) with 5-bit (32 levels)
  of quantization.
  [<a href="http://www.jiscdigitalmedia.ac.uk/images/ITDA-05-bitdepth.jpg">JISC Digital Media</a>]</figcaption>
</figure>
</div><p></p>

The options for precision/bit depth offered in software and recorders
are usually 16 or 24 bit. 16 bit is generally sufficient for recording
speech.
