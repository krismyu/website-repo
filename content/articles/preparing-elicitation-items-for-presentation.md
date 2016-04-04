Title: Preparing elicitation items for presentation
Date: 2013-06-23 9:33
Author: Kristine Yu
Tags: ldc-kiy, fieldwork, tutorial
Slug: preparing-elicitation-items-for-presentation
Summary: Tutorial for LDC paper: preparing elicitation items for presentation.

For elicitation sessions designed to confirm hypotheses, the
elicitation items may be known in advance. In such cases, it can be
helpful to prepare a set of slides for elicitation in advance and to
run a "canned" elicitation session.

+ **Why canned?** For blocking and randomizing stimuli (see Section
  2.3 of the paper), it's necessary
  to prepare stimulus presentation order in advance.
  
+ **Why slides?** Slides can be beneficial relative to a list of words
  since they clearly separate one elicitation item from another for
  both the elicitor and the consultant. This can help with ordering
  effects, especially at the end of an elicitation session. With a
  list, the consultant is very aware of the impending end of the
  session and this awareness can induce changes in their pronunciation
  such as discourse/utterance-final prosody. The isolation of one
  elicitation from another can also help emphasize the sense of each
  elicitation item being in its own discourse context and help prevent
  list intonation. 

In this tutorial, we illustrate how to go from a spreadsheet of
elicitation items to slides for presentation during an elicitation
session. We use Microsoft Excel and Microsoft Word, but other
spreadsheet and word processing software programs can be used in a
similar way.

All files referenced in the tutorial are in [this directory](http://media.krisyu.org/ldc-kiy/) in
the `tutorials/preparing-stimuli/` [sub-directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-elicitation-items/).

We start with our spreadsheet for `20111215-kiy-2-framedwordlist`.
To get from this spreadsheet to preparing stimuli for presentation in
an elicitation session, we need to:

+ [Set and document an order for eliciting the stimulus set](#order)
+ [Format the stimuli for visual presentation](#format)
 
## <a id="order"></a>Set and document an order for eliciting the stimulus set ##

You can follow along with the tutorial by starting with the file
`20111215-2-kiy-ap-framedwordlist.xlsx` in the `tutorials/preparing-elicitation-items/` [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-elicitation-items/).

The simplest kind of randomization of stimulus order you can do is a
pure randomization without any constraints, e.g. "no items of both
Tone 2 one after another". Here's a quick way to do this in
spreadsheets:

1. In a new column, type a column header label "**rand**". We'll fill
this column with randomly generated numbers.

2. In the first cell in the column, enter the <a href="http://office.microsoft.com/en-us/excel-help/rand-function-HP010342816.aspx">`RAND()`</a>
command to fill the cell with a randomly generated number between 0 and 1:

3. Then double-click the right-bottom corner of this cell to have the `RAND()` command be filled down the column. Now you've got a random number in each row of the hash table!

	<p align="center">
	<a href="/img/2013/05/20111215-2-kiy-ap-rand1.png"><img
    class="size-full"  alt="Use RAND() to generate a column of random
    numbers for sorting stimulus order."
    src="/img/2013/05/20111215-2-kiy-ap-rand1.png"
	width="700"/></a><br>
    *Use `RAND()` to generate a column of random numbers for sorting stimulus order.*
	</p>

4. A problem: Excel will recalculate the column of random numbers any time you do anything with them, include sorting with them. There are two ways to fix this:

    + #### Method 1
	
	  Change the calculation mode to `Manually` in `Excel >
      Preferences` under the preference settings for `Calculation`. Also
      make sure that `Always calculate before saving workbook` is **not
      checked**

      <p align="center">
      <a href="/img/2013/05/excel-calc.jpg"><img
	  class="size-full"  alt="The Calculation preference pane."
	  src="/img/2013/05/excel-calc.jpg" width="300"
	  /></a><br>*The Calculation preference pane.*
	  </p>

      <p align="center">
      <a href="/img/2013/05/excel-calculate-manual.png"><img
	  class="size-full"  alt="Setting calculation mode to manually."
	  src="/img/2013/05/excel-calculate-manual.png"
      width="300" /></a><br>*Setting calculation mode to manually.*
     </p>
	 
    + #### Method 2
	
	  Copy the column of random numbers and use `Edit > Paste
      Special` to paste just the `Values`. Use this column to do
	  the sorting in the next step.

5. Now we'll **sort** the hash table by these random
	numbers. Double-click on the icon with a triangle on the right
	corner of the **rand** column header cell to pop up a dialogue box
	for sorting. (If you don't see such an icon, then make sure that
	`Data > Filter` is checked:

    <p align = "center">
	<a href="/img/2013/05/excel-filter.png"><img
	class="size-medium wp-image-133" alt="Make sure that Filter is
	checked so that the filter icons show up in the table header
	cells." src="/img/2013/05/excel-filter.png" width="500"
	height="183" /></a><br>
	*Make sure that `Filter` is checked so that the filter icons show
	up in the table header cells.*
	</p>
 
6. Click on `Ascending` (or `Descending`, it doesn't matter) and then
close the dialogue box. Now your items are sorted by the random
numbers from least to greatest, i.e., your item order has been
randomized! Note that if we sort in ascending order by the **item**
column, we'll get our original spreadsheet order back. So it's really
important that we have the elicitation item key (ID/barcode), as
discussed in
[Organizing elicitation items](../organizing-elicitation-items/), so
we always can keep tabs on an elicitation item, even if we randomize
the elicitation item order.

    <p align = "center">
 	<a href="/img/2013/05/20111215-2-kiy-ap-rand-sorted.png"><img
    class="size-full wp-image-135" alt="Items in hash table sorted by
    the random numbers in Column M in ascending order"
    src="/img/2013/05/20111215-2-kiy-ap-rand-sorted.png"
    width="700" /></a><br> *Items in spreadsheet sorted by the
    random numbers in Column M in ascending order*
	</p>

7. Make sure you **save** your stimuli in randomized order, e.g. as a
   new file `20111215-2-kiy-ap-framedwordlist-rand.xlsx`. Note that
   your final spreadsheet may look different from the file
   `20111215-2-kiy-ap-framedwordlist-rand.xlsx` in the
   `tutorials/preparing-elicitation-items/`
   [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-elicitation-items/)
   since your randomized order will be different.


------------------------------------

## <a id="format"></a>Format the stimuli for visual presentation ##

Now you can copy your stimuli from Excel into Word to generate a slideshow for your elicitation session! Since the spreadsheet `20111215-2-kiy-ap-framedwordlist-rand.xlsx` preserves the association of each stimulus item to its properties, e.g. `word.1`, `word.2`, `verb`, etc., we don't need to worry about keeping track about these properties in creating the slideshow---all we need to copy over is, minimally, the English free translations in the `sent.eng` column, since we need a prompt to elicit each item during the elicitation session. 

We might also want to copy over the Kirikiri sentences in `sent.kiy` and the targeted tonal patterns in `bitone` so we have an idea of what we're expecting the consultant to utter for each elicitation item, to help check as we go along in the elicitation session that we're actually eliciting what we intend to elicit.

Here's how to turn your Excel data into slides to present in
elicitation in Word, in two steps:

1. [Copy the stimuli from the Excel spreadsheet into Word](#copy)
2. [Re-formatting the Word document to create slides](#word)

### <a id="copy"></a> Copy the stimuli from the Excel spreadsheet into Word ###

1. Select the columns you want in your slides and copy them to the system clipboard by clicking on `Copy` in the `Edit` menu:

    <p align = "center">
	<a href="/img/2013/05/excel-copy1.jpg"><img
    src="/img/2013/05/excel-copy1.jpg" alt="Select the
    columns you want  to appear in your slides for presentation and
    copy." width ="625" height="267" class="size-large
    wp-image-187"/></a><br>
	*Select the columns you want  to appear in your slides for
	presentation and copy.*
	</p>

2. Open Microsoft Word and select `Paste Special...` in the `Edit` menu.

	<p align = "center">
	<a href="/img/2013/05/word-paste-special.jpg"><img
	src="/img/2013/05/word-paste-special.jpg" alt="Paste the copied Excel
	data as unformatted text" width="366" height="326" class="size-full
	wp-image-196" /></a><br>
	*Paste the copied Excel data as unformatted text*
	</p>

3. Now you should have a bunch of text in your Word document, with one item per line, in your randomized order from `20111215-2-kiy-ap-framedwordlist-rand.xlsx`. Note that the original column breaks in Excel are preserved here with *tab-delimited* formatting: in each row, tab characters separate the original Excel columns. Also, each line ends in a *newline* (paragraph symbol) which indicates a line break. If you don't see any of these special characters, make sure that you have set the option `Show all non-printing characters`.

<p align = "center">
<a href="/img/2013/05/word-stims-unformatted.jpg"><img src="/img/2013/05/word-stims-unformatted.jpg" alt="Pasted text from Excel. Pay special attention to the special characters separating columns (tabs) and lines (newline/paragraph symbol)." width="560" height="229" class="size-full wp-image-201" /></a><br>
<i>Pasted text from Excel. Pay special attention to the special characters separating columns (tabs) and lines (newline/paragraph symbol).</i>
</p>

<p align = "center">
<a href="/img/2013/05/word-special-char.jpg"><img src="/img/2013/05/word-special-char.jpg" alt="Click on the paragraph
symbol icon to show the special characters." width="482" height="175"
class="size-full wp-image-204" /></a><br>
Click on the paragraph symbol icon to show the special characters.
</p>

### <a id="word"></a> Re-formatting the Word document to create slides ###

Now we're all set to start re-formatting the Word document,
`20111215-2-kiy-ap-framedwordlist-slides0.docx` (in the `tutorials/preparing-elicitation-items/` [directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-elicitation-items/).
) to create slides. We'll be making PDF slides that look like the figure below:

<p align = "center">
<a href="/img/2013/06/slide-for-elicitor.jpg"><img
src="/img/2013/06/slides-for-elicitor.jpg"
alt="Slides for elicitor." width="560" /></a><br>
<i>Slides for the elicitor, including the bitone, Kirikiri sentence,
and English translation.</i>
</p>

The slides are for the elicitor and/or translator and thus include
information beyond the Kirikiri sentence or the English
translation. 

The screencast below illustrates the steps for creating the slides
`20111215-2-kiy-ap-framedwordlist-slides.pdf` and
`20111215-2-kiy-ap-framedwordlist-slides.docx` from
`20111215-2-kiy-ap-framedwordlist-slides0.docx`. All files are in the
`tutorials/preparing-elicitation-items/`
[directory](http://media.krisyu.org/ldc-kiy/tutorials/preparing-elicitation-times/). The
steps are also outlined below in the tutorial body.

<p align = "center">
<video controls>
  <source src="http://media.krisyu.org/ldc-kiy/videos/20111215-2-kiy-ap-framedwordlist-slides.mp4" type="video/mp4">
  <source src="http://media.krisyu.org/ldc-kiy/videos/20111215-2-kiy-ap-framedwordlist-slides.ogv" type="video/ogg">
  Your browser does not support the video tag.
</video>
Screencast:creating slides for presentation of elicitation items to consultant.
</p>

1. We'll use the [special characters](http://support.microsoft.com/kb/214204) to help us format the slides using the `Find and Replace` command. Make sure the cursor is set at the beginning of the document. Now click on `Edit > Find > Replace`:

    <p align = "center">
	<a href="/img/2013/05/word-find-replace.jpg"><img
    src="/img/2013/05/word-find-replace.jpg"
	alt="Select Edit &gt; Find &gt;Replace." width="466" height="337"
	class="size-full wp-image-206" /></a><br> 
    <i>Select `Edit > Find > Replace`.</i>
    </p>

2. Use `Find > Replace` to make the following replacements, in the stated order (order matters!):

	1. Replace *carriage return/paragraph mark* `^p` with *pagebreak*
       `^m` followed by a few *carriage return/paragraph marks*
       `^p^p`, i.e., with `^m^p^p`. (The carriage return/paragraph
       mark `^p` behaves effectively like a newline/line break character.)
    2. Replace *tab* `^t` with *carriage return/paragraph mark* `^p` 
<p></p>


	This replaces: (1) the carriage returns with page breaks, plus a few
	extra carriage returns to help vertically center the text on the slide,
	and (2) the tabs with carriage returns, so that each different field
	(bitone, sent.kiy, sent.eng) ends up on a different line. So now
	each elicitation item gets its own slide.
	
3. Increase the font size of the text in the document. Go to `Edit >
   Select all` and then change the font size to something that easily
   readable but also not so gigantic that it's hard to fit much text
   into a line. Something like 24 or 36 might work well.
   
4. Change the orientation of the document from portrait to
   landscape. Go to `Format > Document > Page Setup` and click on
   the *landscape* orientation icon. Now your slides will be in
   landscape mode.

5. Finally, make sure you save your Word document. You might also save
   the slides in a PDF file.
   
6. If you want your **consultant** to be looking at your slides for
   elicitation, you might just want each slide to show the
   sentence/word written in the language to be elicited or the
   sentence/word in the contact language. In this case, you would copy
   only the relevant column, e.g. *sent.kiy*, over from the spreadsheet
   to Word and repeat the steps 1-5 above.
