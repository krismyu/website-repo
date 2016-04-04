Title: Organizing elicitation items
Date: 2013-06-23 16:45
Author: Kristine Yu
Tags: ldc-kiy, fieldwork, tutorial
Slug: organizing-elicitation-items

In this tutorial, we cover strategies for organizing data within an
elicitation session as well as across elicitation sessions, including:

1. [Using dictionaries as data structures](#hash)
2. [Working with spreadsheets](#spreadsheet)
2. [Working with text files in the shell](#text)
3. [Organizing files](#files)

<!-- PELICAN_END_SUMMARY -->

The section [Working with text files in the shell](#text) can be
skipped for users that want to stick with working with spreadsheets
rather than working with command-line utilities.

The files referred to in the tutorial can be found in
[this directory](http://media.krisyu.org/ldc-kiy/) in
the `tutorials/organizing-elicitation-items/` [sub-directory](http://media.krisyu.org/ldc-kiy/tutorials/organizing-elicitation-items/).

## <a id="hash"></a>Using dictionaries as data structures ##

Dictionaries are abstract data structures in widespread use in
computer science that associate unique, immutable **keys** with
**values**. The idea of a dictionary is useful not only for practical
concerns in organizing a body of elicitation items and sessions, but
also as a way of guiding thinking in fieldwork from elicitation design
to statistical analysis of data.

Consider as an example the elicitation session represented by
`20111213-1-kiy-ap-framedwordlist.txt`. How might we identify each
elicitation item in our corpus of fieldwork data? For instance, take
*paRai giRu* \`bandicoot's elbow'. During our elicitation session, our
orthographic representation for this was *paRai giRu*. It might be
transparent to simply identify this elicitation item as `paRai giRu`
and name the soundfile for this item `paRai giRu.wav`,[^1] but this strategy for
nomenclature could be problematic for the following reasons:

+ **One-to-many mappings** If we elicited *paRai giRu* in another
  elicitation session, what would we call it? If we identified it as
  *paRai giRu*, we would have trouble distinguishing the two different
  elicitaiton items (elicited in different elicitation sessions). Or
  what if we elicited *paRai giRu* multiple times in a single session?
  One idea would be to include elicitation session and repetition
  information in the identifier,
  e.g. `20111213-1-kiy-ap-framedwordlist- paRai giRu - rep 1`. 

+ **Mutability.** What if later down the road, we changed our
  transcription of the item, e.g. if we decided to
  exclusively use IPA transcriptions or to develop a different
  practical orthography? Then we'd have to change our identifier for
  the item everywhere it is referenced. We might also later completely
  change our system for naming files. Changing filenames in either
  case could be a potentially tedious and error-prone process. 
  
+ **Character encoding.** If we decided to change our transcription to include
  IPA symbols or any other
  non-[ASCII](http://computer.howstuffworks.com/bytes2.htm)
  characters, the character encoding of the filename might get garbled
  [across platforms](http://scripts.sil.org/cms/scripts/page.php?item_id=FontFAQ_CrossPlatform).
  It's safer to restrict characters in filenames to be drawn from the
  [ASCII character set](http://www.w3schools.com/tags/ref_ascii.asp). 

+ **Association of additional information about elicitation item.** As we explore the dimensions of tonal
  contrast, there are a number of different variables we might want to
  keep track of for each elicitation item. For instance, for this
  item, we might want to associate the following:
	  + elicitation session: 201111213-1-kiy-ap-framedwordlist
	  + gloss: \`bandicoot's elbow'
	  + tone of first word: T1
	  + tone of second word: T1
	  + frame: T1-T1

  We could have a elicitation item nomenclature that would give us a
  identifier like `201111213-1-kiy-ap-framedwordlist - paRai giRu -
  bandicoot's elbow - T1 - T1`.
  Later on, as we learn more about Kirikiri, there might be still
  additional information we'd like to associate. We could encode this
  information in the filename, but the filename could get very long,
  and we'd have to change the filename if we decided to change what
  information we wanted to associate. We might also change the values
  for the individual fields of association, e.g. perhaps we might
  hypothesize later that T1 actually should be split into two distinct
  tonemes, T1a and T1b. Then we'd need to change the values of *tone
  of first word*, *tone of second word*, and *frame* for many
  elicitation items, another instance of the problem of mutability.

One good solution to these problems is to use the dictionary data
structure for keeping track of elicitation items. 

### Barcodes for elicitation items ###

<p align="center">
<a href="/img/2013/06/codigobarras.svg"><img style = "float:middle" class="size-full"
alt="Barcode image from http://openclipart.org/detail/81883/codigde-barras--by-asrafil" src="/img/2013/06/codigobarras.svg" width="200" /></a> 
</p>

An alternative to identifiers like `201111213-1-kiy-ap-framedwordlist - paRai giRu -
  bandicoot's elbow - T1 - T1`, is to use **keys**---to assign
a unique, immutable barcode to each elicitation item and keep track of
  elicitation items using the dictionary data structure. Any additional
  information can be associated to the elicitation item via the
  barcode. Even if the additional information associated changes, the
  identifier for the elicitation item remains constant. The associated
  information can be held in a spreadsheet, associated to the unique
  identifiers. The columns in the spreadsheet with the associated
  information may change, but the identifiers and filenames remain constant.

In this section, we give some tips for generating tables with
the **values** associated with the **keys** for elicitation
items. First, we'll discuss generating tables in spreadsheets in Excel. Then
we'll discuss generating tables in text files.

We give two example tables below,[^3] where the keys are listed in the
`item` column as integers 1, 2, 3, 4, 5, .... These keys are really
shorthand for keys like `20111213-1-kiy-ap-framedwordlist-1`,
`20111213-1-kiy-ap-framedwordlist-2`, etc., which are the full keys used for
file naming, e.g. `20111213-1-kiy-ap-framedwordlist-1.wav`.
Table 1 shows an extract from the dictionary for
20111213-1-kiy-ap-framedwordlist, from the text file
`20111213-1-kiy-ap-framedwordlist.txt`
[here](http://media.krisyu.org/ldc-kiy/tutorials/organizing-elicitation-items/20111213-1-kiy-ap-framedwordlist.txt). Table
2 shows an extract from the spreadsheet
`20111215-2-kiy-ap-framedwordlist.xlsx`, available
[here](http://media.krisyu.org/ldc-kiy/tutorials/organizing-elicitation-items/20111215-2-kiy-ap-framedwordlist.xlsx).

We'll use `20111215-2-kiy-ap-framedwordlist.xlsx` to demonstrate some
tips for efficiency and semi-automated entry in working with
spreadsheets. We use Microsoft Excel for demonstration, but similar
approaches are available in other spreadsheet software programs.

### Example tables illustrating dictionary data structures for organizing elicitation items ###

<table>
	<caption>Table 1: Extract from 20111213-1-kiy-ap-framedwordlist dictionary</caption>
	<thead>
    <tr>
        <td>item</td>
        <td>kirikiri</td>
        <td>gloss</td>
        <td>tone1</td>
        <td>tone2</td>
        <td>frame</td>
        <td>word1</td>
        <td>word2</td>
    </tr>
	</thead>
	<tbody>
    <tr>
        <td>1</td>
        <td>paRai giRu</td>
        <td>bandicoot's elbow</td>
        <td>T1</td>
        <td>T1</td>
        <td>11</td>
        <td>paRai</td>
        <td>giRu</td>
    </tr>
    <tr>
        <td>2</td>
        <td>kaza giRu</td>
        <td>gecko's elbow</td>
        <td>T2</td>
        <td>T1</td>
        <td>21</td>
        <td>kaza</td>
        <td>giRu</td>
    </tr>
    <tr>
        <td>3</td>
        <td>fivaa giRu</td>
        <td>snail's elbow</td>
        <td>T3</td>
        <td>T1</td>
        <td>31</td>
        <td>fivaa</td>
        <td>giRu</td>
    </tr>
    <tr>
        <td>4</td>
        <td>naraa giRu</td>
        <td>wasp's elbow</td>
        <td>T4</td>
        <td>T1</td>
        <td>41</td>
        <td>naraa</td>
        <td>giRu</td>
    </tr>
    <tr>
        <td>5</td>
        <td>tava giRu</td>
        <td>catfish's elbow</td>
        <td>T5</td>
        <td>T1</td>
        <td>51</td>
        <td>tava</td>
        <td>giRu</td>
    </tr>
</tbody>
</table>

<table>
	<caption>Table 2: Extract from 20111215-2-kiy-ap-framedwordlist dictionary</caption>
	<thead>
    <tr>
        <td>item</td>
        <td>word.1</td>
        <td>word.2</td>
        <td>verb</td>
        <td>gloss.1</td>
        <td>gloss.2</td>
        <td>gloss.verb</td>
        <td>tone.1</td>
        <td>tone.2</td>
        <td>bitone</td>
        <td>sent.kiy</td>
        <td>sent.eng</td>
    </tr>
</thead>
<tbody>
    <tr>
        <td>1</td>
        <td>kE</td>
        <td>ndE</td>
        <td>fuwa</td>
        <td>ant</td>
        <td>centipede</td>
        <td>sees</td>
        <td>T1</td>
        <td>T1</td>
        <td>T1.T1</td>
        <td>kE ndE fuwa.</td>
        <td>The ant sees the centipede.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>kE</td>
        <td>fa</td>
        <td>fuwa</td>
        <td>ant</td>
        <td>younger.sibling</td>
        <td>sees</td>
        <td>T1</td>
        <td>T2</td>
        <td>T1.T2</td>
        <td>kE fa fuwa.</td>
        <td>The ant sees the younger.sibling.</td>
    </tr>
    <tr>
        <td>3</td>
        <td>kE</td>
        <td>nO</td>
        <td>fuwa</td>
        <td>ant</td>
        <td>meat</td>
        <td>sees</td>
        <td>T1</td>
        <td>T2</td>
        <td>T1.T2</td>
        <td>kE nO fuwa.</td>
        <td>The ant sees the meat.</td>
    </tr>
    <tr>
        <td>4</td>
        <td>kE</td>
        <td>fO</td>
        <td>fuwa</td>
        <td>ant</td>
        <td>wallaby</td>
        <td>sees</td>
        <td>T1</td>
        <td>T3</td>
        <td>T1.T3</td>
        <td>kE fO fuwa.</td>
        <td>The ant sees the wallaby.</td>
    </tr>
    <tr>
        <td>5</td>
        <td>kE</td>
        <td>fO</td>
        <td>fuwa</td>
        <td>ant</td>
        <td>honeybee</td>
        <td>sees</td>
        <td>T1</td>
        <td>T3</td>
        <td>T1.T3</td>
        <td>kE fO fuwa.</td>
        <td>The ant sees the honeybee.</td>
    </tr>
    <tr>
        <td>6</td>
        <td>kE</td>
        <td>ya</td>
        <td>fuwa</td>
        <td>ant</td>
        <td>mother</td>
        <td>sees</td>
        <td>T1</td>
        <td>T5</td>
        <td>T1.T5</td>
        <td>kE ya fuwa.</td>
        <td>The ant sees the mother.</td>
    </tr>
    <tr>
        <td>7</td>
        <td>kE</td>
        <td>fa</td>
        <td>fuwa</td>
        <td>ant</td>
        <td>sago.grub</td>
        <td>sees</td>
        <td>T1</td>
        <td>T5</td>
        <td>T1.T5</td>
        <td>kE fa fuwa.</td>
        <td>The ant sees the sago.grub.</td>
    </tr>
    <tr>
        <td>8</td>
        <td>ndE</td>
        <td>kE</td>
        <td>fuwa</td>
        <td>centipede</td>
        <td>ant</td>
        <td>sees</td>
        <td>T1</td>
        <td>T1</td>
        <td>T1.T1</td>
        <td>ndE kE fuwa.</td>
        <td>The centipede sees the ant.</td>
    </tr>
    <tr>
        <td>9</td>
        <td>ndE</td>
        <td>fa</td>
        <td>fuwa</td>
        <td>centipede</td>
        <td>younger.sibling</td>
        <td>sees</td>
        <td>T1</td>
        <td>T2</td>
        <td>T1.T2</td>
        <td>ndE fa fuwa.</td>
        <td>The centipede sees the younger.sibling.</td>
    </tr>
    <tr>
        <td>10</td>
        <td>ndE</td>
        <td>nO</td>
        <td>fuwa</td>
        <td>centipede</td>
        <td>meat</td>
        <td>sees</td>
        <td>T1</td>
        <td>T2</td>
        <td>T1.T2</td>
        <td>ndE nO fuwa.</td>
        <td>The centipede sees the meat.</td>
    </tr>
</tbody>
</table>

---------------------------------------------------------

## <a id="spreadsheet"></a>Working with spreadsheets ##

For Table 2 above, we only filled in a portion of the columns by
hand. Many of the columns are fully specified by other columns. For
instance, `sent.kiy` entries are simply concatenated from `tone.1` and
`tone.2` entries. Such fully specified columns can be automatically
filled in, as we demonstrate below. 

To follow along, download
`20111215-2-kiy-ap-framedwordlist-initial.xlsx`
[here](http://media.krisyu.org/ldc-kiy/tutorials/organizing-elicitation-items/20111215-2-kiy-ap-framedwordlist-initial.xlsx). We'll
show how the columns `bitone`, `sent.kiy` and `sent.eng` can all be filled in
automatically from other columns using the `CONCATENATE` command.

+ Filling in the **bitone** entries

The `bitone` entry is simply the concatenation of `tone.1` and
`tone.2`. We can generate the bitone entries automatically by clicking
on Cell J2, the first cell in the bitone column, and typing
the following command and hitting `Return`/`Enter`:

```vbscript
# Concatenate the TONE.1 entry, a period, and the TONE.2 entry
=CONCATENATE([@[tone.1]],".",[@[tone.2]])
```
The period serves as a delimiter between the two tones. We can then
*fill down* this command down the entire bitone column by hovering the
mouse at the bottom right hand corner of Cell J2 and double-clicking. We show a screenshot of the command in the spreadsheet below. Click
on the image to open a new window with a larger sized version of the image.

<a href="/img/2013/05/20111215-2-kiy-ap-concat-bitone.png"><img
    class="size-full wp-image-135" alt="Concatenating bitones"
    src="/img/2013/05/20111215-2-kiy-ap-concat-bitone.png" width="800" /></a> 

+ Filling in the **sent.kiy** entries

Similarly, we can generate the `sent.kiy` entries from concatenating
the `word.1`, `word.2`, and `verb` entries, with some space delimiters
and an ending period:

```vbscript
# Concatenate the WORD.1 entry, a space, the WORD.2 entry, a space, the VERB entry, and a period.
=CONCATENATE([@[word.1]]," ",[@[word.2]]," ",[@verb],".")
```

We show a screenshot of the command in the spreadsheet below. Click
on the image to open a new window with a larger sized version of the image.
	
<a href="/img/2013/05/20111215-2-kiy-ap-concat-sent-kiy.png"><img
class="size-full wp-image-135" alt="Concatenating Kirikiri sentences"
src="/img/2013/05/20111215-2-kiy-ap-concat-sent-kiy.png"
width="800" /></a><br>
	

+ Filling in the **sent.eng** entries

Finally, we can fill in the `sent.eng` entries by concatenating
`gloss.1`, `gloss.verb`, and `gloss.2`, plus an additional determiner
"the" and some spaces and an ending period:

```vb
# Concatenate "The ", the GLOSS.1 entry, a space, the GLOSS.VERB entry, a space, "the", the GLOSS.2 entry, and a period.
=CONCATENATE("The ",[@[gloss.1]]," ", [@[gloss.verb]]," ","the ", [@[gloss.2]], ".")
```
We show a screenshot of the command in the spreadsheet below. Click
on the image to open a new window with a larger sized version of the image.

<a href="/img/2013/05/20111215-2-kiy-ap-concat-sent-eng.png"><img
class="size-full wp-image-135" alt="Concatenating English sentences"
src="/img/2013/05/20111215-2-kiy-ap-concat-sent-eng.png"
width="800" /></a> 

The *fill down* trick also works for the `item` column. If you type
the first few rows in (1, 2, 3) and then click and drag to select
those three cells, you can use the same *fill down* trick described
above to fill in the rest of the item entries.


---------------------------------------------------------

## <a id="text"></a>Working with text files in the shell ##

For command line aficionados (see
[the introductory section](..//processing-audio-files-sox/#intro)
of
[Processing audio files (with SoX)](..//processing-audio-files-sox/)
for more on the command line), an alternative to working with
spreadsheet software programs like Excel is to work directly with text
files from the command line. Here we'll show how to do the same steps
as above in Excel at the command line, beginning with converting text
file line endings across platforms.

### Text file formats and line endings ###

A common issue that comes up in dealing with text files is that there
are
[different characters](http://www.rfc-editor.org/EOLstory.txt) [for line endings](http://www.codinghorror.com/blog/2010/01/the-great-newline-schism.html),
i.e. newline characters, across platforms.

The `organizing-elicitation-items/` directory contains three
tab-delimited text files and two CSV (comma separated values) files:

```bash
amoebe@moebius :: ls *.txt*
20111213-1-kiy-ap-framedwordlist.txt       20111215-2-kiy-ap-framedwordlist.txt.unix
20111215-2-kiy-ap-framedwordlist.txt

amoebe@moebius :: ls *.csv*
20111215-2-kiy-ap-framedwordlist.csv       20111215-2-kiy-ap-framedwordlist.csv.unix
```
The files with the `.unix` suffix have been converted to have UNIX
line endings, while the files with just a `.txt` or `.csv` suffix were
generated in Microsoft Excel using `File > Save As` and have Mac line
endings. If we do a simple `cat` command to display
`20111215-2-kiy-ap-framedwordlist.txt`, the output looks funny---it's
a single line (you need to drag the scroll bar at the bottom of the
code snippet window in order to see this!).

```bash
# Extract from output of cat command
amoebe@moebius :: cat 20111215-2-kiy-ap-framedwordlist.txt
1tem	kErd.1	ndEd.2	fuwa	antss.1	centipedeloss.vesees    T1ne.1	T1ne.2	T1.T1e	kE ndE fuwa.    The ant se2s the ckEtipedefa	fuwa	ant	younger.sibling	sees	T1	T2	T1.T2	kE fa fuwa.	The ant se3s the ykEnger.snOling. fuwa	ant	meat	sees	T1	T2	T1.T2	kE nO fuwa.	The ant sees the m4at.    kE	fO	fuwa	ant	wallaby	sees	T1	T3	T1.T3	kE fO fuwa.	The ant sees the w5llaby. kE	fO	fuwa	ant	honeybee	sees	T1	T3	T1.T3	kE fO fuwa.	The ant se6s the hkEeybee.ya	fuwa	ant	mother	sees	T1	T5	T1.T5	kE ya fuwa.	The ant sees the m7ther.  kE	fa	fuwa	ant	sago.grub	sees	T1	T5	T1.T5	kE fa fuwa.	The ant se```
```
If we invoke `cat -v` to display non-printing characters, we can see
that line endings are delimited with `^M`:

```bash
# Extract from output of cat -v command which prints non-printing characters
amoebe@moebius :: cat -v 20111215-2-kiy-ap-framedwordlist.txt
item	word.1	word.2	verb	gloss.1	gloss.2	gloss.verb	tone.1	tone.2	bitone	sent.kiy	sent.eng^M1	kE	ndE	fuwa	ant	centipede	sees	T1	T1	T1.T1	kE ndE fuwa.	The ant sees the centipede.^M2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2	T1.T2	kE fa fuwa.	The ant sees the younger.sibling.^M3	kE	nO	fuwa	ant	meat	sees	T1	T2	T1.T2	kE nO fuwa.	The ant sees the meat.^M4	kE	fO	fuwa	ant	wallaby	sees	T1	TT1.T3	kE fO fuwa.	The ant sees the wallaby.^M5	kE	fO	fuwa	ant	honeybee	sees	TT3	T1.T3	kE fO fuwa.	The ant sees the honeybee.^M
```

These are non-UNIX line endings used for Mac as well as
Windows/DOS. Fortunately, we can convert the line endings using a
variety of command-line utilities, such as the dedicated utility
[flip](https://ccrma.stanford.edu/~craig/utility/flip/),[^3] as well as
[standard](http://kb.iu.edu/data/acux.html)
[command](http://hints.macworld.com/article.php?story=20001206164827794)
[utilities](http://superuser.com/questions/71507/convert-unix-line-endings-to-windows)
like `tr`, `awk`, and `sed`.

Below, we'll demonstrate using `flip`:

```
amoebe@moebius :: flip

Usage: flip [-t|-u|-d|-m] filename[s]
   Converts ASCII files between Unix, MS-DOS/Windows, or Macintosh newline formats

   Options: 
      -u  =  convert file(s) to Unix newline format (newline)
      -d  =  convert file(s) to MS-DOS/Windows newline format (linefeed + newline)
      -m  =  convert file(s) to Macintosh newline format (linefeed)
      -t  =  display current file type, no file modifications
```

**Warning:
`flip` converts files in place, i.e., it overwrites the original file
with the modified file with converted line endings.** You can find the
`flip` executable in the `flip/` directory in
`tutorials/organizing-elicitation-items/`, which I compiled from
[source](https://ccrma.stanford.edu/~craig/utility/flip/flip.cpp)
using the C++ compiler `g++` on Mac OSX:[^4]

```bash
g++ -o flip flip.cpp
```

You can copy the `flip` executable to a directory in your PATH such as
`/usr/local/bin/`, or you can run it from the `flip/` directory by
invoking `./flip`. Below we show using `flip -u` to convert the MAC
line endings to UNIX line endings. Since `flip` converts the line
endings in the orginal file and overwrites it, we first copy the text
files to new text files named with `.unix` suffixes.

```bash
# Convert line endings from Mac to Unix for tab-delimited file
cp 20111215-2-kiy-ap-framedwordlist.txt 20111215-2-kiy-ap-framedwordlist.txt.unix
flip -u 20111215-2-kiy-ap-framedwordlist.txt.unix

# Convert line endings from Mac to Unix for CSV file
cp 20111215-2-kiy-ap-framedwordlist.csv 20111215-2-kiy-ap-framedwordlist.csv.unix
flip -u 20111215-2-kiy-ap-framedwordlist.csv.unix
```

Now the output of `cat` prints with proper line breaks:

```bash
# Extract from output of cat command after flip line ending conversion
amoebe@moebius :: cat 20111215-2-kiy-ap-framedwordlist.txt.unix
item	word.1	word.2	verb	gloss.1	gloss.2	gloss.verb	tone.1	tone.2	bitone	sent.kiy	sent.eng
1	kE	ndE	fuwa	ant	centipede	sees	T1	T1	T1.T1	kE ndE fuwa.	The ant sees the centipede.
2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2	T1.T2	kE fa fuwa.	The ant sees the younger.sibling.
3	kE	nO	fuwa	ant	meat	sees	T1	T2	T1.T2	kE nO fuwa.	The ant sees the meat.
4	kE	fO	fuwa	ant	wallaby	sees	T1	T3	T1.T3	kE fO fuwa.	The ant sees the wallaby.
5	kE	fO	fuwa	ant	honeybee	sees	T1	T3	T1.T3	kE fO fuwa.	The ant sees the honeybee.
```

### Command-line utilities for adding associated information ###

We'll demonstrate using command-line utilities for adding associated
information with `20111215-2-kiy-ap-framedwordlist`.
Let's start with just the first nine columns, `item`, `word.1`,
`word.2`, `verb`, `gloss.1`, `gloss.2`, `gloss.verb`, `tone.1`, and
`tone.2`, which we write to the file
`20111215-2-kiy-ap-framedwordlist-initial.txt`. 

```bash
# Extract only columns that can't be automatically filled in, columns 1-9
# Write to file 20111215-2-kiy-ap-framedwordlist-initial.txt
cut -f1-9 20111215-2-kiy-ap-framedwordlist.txt.unix > 20111215-2-kiy-ap-framedwordlist-initial.txt
```
Now how can we generate `bitone`, `sent.kiy`, and `sent.eng`? One way
is to use the [`awk` command utility](http://www.grymoire.com/Unix/Awk.html):

To generate the `bitone` column, we invoke the following command:

```bash
# -F "\t" indicates that the input file is tab-delimited
# $0 indicates all fields, so print $0 prints all columns (fields) in the file
# We also print a tab-character between the original columns $0 and the new column 
# We pipe the output through head -3 to print just the first 3 lines of the output file

# $8."$9 indicates field 8, followed by a ".", followed by field 9
awk -F "\t" '{print $0,"\t"$8"."$9}' 20111215-2-kiy-ap-framedwordlist-initial.txt | head -3
```
to get the output:

```bash
amoebe@moebius :: awk -F "\t" '{print $0,"\t"$8"."$9}' 20111215-2-kiy-ap-framedwordlist-initial.txt | head -3
item	word.1	word.2	verb	gloss.1	gloss.2	gloss.verb	tone.1	tone.2 	tone.1.tone.2
1	kE	ndE	fuwa	ant	centipede	sees	T1	T1 	T1.T1
2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2 	T1.T2
```

To generate the `sent.kiy` column, we can invoke:

```bash
# $2, $3, $4 indicates field 2 followed by field 3 followed by field,
#  with each field delimited by spaces (the default delimiter for awk)

awk -F "\t" '{print $0,"\t"$2,$3,$4}' 20111215-2-kiy-ap-framedwordlist-initial.txt | head -3
```

This generates the output:

```bash
amoebe@moebius :: awk -F "\t" '{print $0,"\t"$2,$3,$4}' 20111215-2-kiy-ap-framedwordlist-initial.txt | head -3
item	word.1	word.2	verb	gloss.1	gloss.2	gloss.verb	tone.1	tone.2 	word.1 word.2 verb
1	kE	ndE	fuwa	ant	centipede	sees	T1	T1 	kE ndE fuwa
2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2 	kE fa fuwa
```

Finally, we generate the `sent.eng` column as follows:

```bash
# This is similar to the previous command, but with some "the"'s
# concatenated in
awk -F "\t" '{print $0,"\t""The", $5, $7, "the", $6"."}' 20111215-2-kiy-ap-framedwordlist-initial.txt | head -3
```

with the output:

```bash
amoebe@moebius :: awk -F "\t" '{print $0,"\t""The", $5, $7, "the", $6"."}' 20111215-2-kiy-ap-framedwordlist-initial.txt | head -3
item	word.1	word.2	verb	gloss.1	gloss.2	gloss.verb	tone.1	tone.2 	The gloss.1 gloss.verb the gloss.2.
1	kE	ndE	fuwa	ant	centipede	sees	T1	T1 	The ant sees the centipede.
2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2 	The ant sees the younger.sibling.
```
One (verbose) way to chain these commands is to pipe them to each
other. We can redirect the output to the file `20111215-2-kiy-ap-framedwordlist-new.txt`.

```bash
awk -F "\t" '{print $0,"\t"$8"."$9}' 20111215-2-kiy-ap-framedwordlist-initial.txt | awk -F "\t" '{print $0,"\t"$2,$3,$4}' | awk -F "\t" '{print $0,"\t""The", $5, $7, "the", $6"."}' > 20111215-2-kiy-ap-framedwordlist-new.txt```

Examining the first three lines of
`20111215-2-kiy-ap-framedwordlist-new.txt` shows that we accomplished
what we want, except the table headers are screwed up.

```bash
amoebe@moebius :: head -3 20111215-2-kiy-ap-framedwordlist-new.txtitem	word.1	word.2	verb	gloss.1	gloss.2	gloss.verb	tone.1	tone.2 	tone.1.tone.2 	word.1 word.2 verb 	The gloss.1 gloss.verb the gloss.2.
1	kE	ndE	fuwa	ant	centipede	sees	T1	T1 	T1.T1 	kE ndE fuwa 	The ant sees the centipede.
2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2 	T1.T2 	kE fa fuwa 	The ant sees the younger.sibling.
```

We can correct the table headers by targeting just the first row
using `NR==1`, and replacing fields $10-$12 with the appropriate
heading. We write to the file `20111215-2-kiy-ap-framedwordlist-final.txt`.

```bash
awk -F "\t" 'NR==1 {$10="bitone";$11="sent.kiy";$12="sent.eng"}1' 20111215-2-kiy-ap-framedwordlist-new.txt > 20111215-2-kiy-ap-framedwordlist-final.txt
```

A quick examination of the output file `20111215-2-kiy-ap-framedwordlist-final.txt` shows we got what we wanted.

```bash
amoebe@moebius :: head -3 20111215-2-kiy-ap-framedwordlist-final.txt 
item word.1 word.2 verb gloss.1 gloss.2 gloss.verb tone.1 tone.2  bitone sent.kiy sent.eng
1	kE	ndE	fuwa	ant	centipede	sees	T1	T1 	T1.T1 	kE ndE fuwa 	The ant sees the centipede.
2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2 	T1.T2 	kE fa fuwa 	The ant sees the younger.sibling.
```

---------------------------------------------------------

## <a id="files"></a>Organizing files ##

One issue that comes up with having a lot of recorded data is the
proliferation of audio files that needs to be dealt with. Some tips
for managing the multitudes of files are:

+ **Standardize directory structure/naming and file naming.** File
  organization is not the place to be creative. If you standardize how
  you set up your directory (folder) structure and how you name
  directories and files, it's a lot easier to know where to find
  things and have an efficient workflow in working with the files,
  especially if you are using any scripts.

+ **Use filenames as dictionary keys and keep associated information
  in spreadsheets/text files.** This means to keep filenames
  immutable and unique, as we saw in
  [Using dictionaries as data structures](#hash), and to include
  spreadsheets and/or text files associating additional information
  about elicitation items to the corresponding files via the
  filenames. 

+ **Keep directory names and filenames limited to the ASCII character set and avoid spaces
  and case-sensitivity.** Special characters in filenames can get you
  in trouble across platforms and in working with scripts. It's safer
  to stay within the alphanumeric ([a-z], [0-9]) ASCII character set and keep special characters
  to associated spreadsheets/text files. Spaces in filenames are
  [best avoided](http://superuser.com/questions/29111/what-technical-reasons-exist-for-not-using-space-characters-in-file-names)
  because while they make filenames human-friendly, they make
  filenames machine-unfriendly---they can cause problems with command
  line interpretation and locating the file and create issues across
  different operating systems. Using case sensitivity to distinguish
  filenames or directory names like `data-files` and `Data-Files` is also dangerous because any
  program that is case-insensitive cannot distinguish such names.

+ **If it's necessary to rename files, use utilities to do bulk
  renaming.** This can help avoid random errors, but you'll need to be
  careful about systematic errors. There are applications available for Windows, Mac, and
  many command line utilities that can do the trick:
          + [Recommendations for Windows](http://lifehacker.com/5139592/ant-renamer-is-a-lightweight-but-powerful-renaming-utility)
          + [Name Mangler](http://manytricks.com/namemangler/) and
    [NameChanger](http://lifehacker.com/5825387/namechanger-for-mac-quickly-renames-groups-of-files
    ) for Mac
          + [Command](http://unix.stackexchange.com/questions/1136/batch-renaming-files) [line](http://hints.macworld.com/article.php?story=20010509130450691) [utilities](http://superuser.com/questions/25378/mass-renaming-nix-version)	

### Examples of directory structure and filenaming ###

Here's an example of directory structure and filenaming for Kirikiri
data from the
[the organizing-elicitation-tiems sub-directory](http://media.krisyu.org/ldc-kiy/tutorials/organizing-elicitation-items/)
in the directory `data/`, which contains all of the data recorded and
associated files.[^5] 

Each elicitation session date gets its own directory in `data/`:

```
data
├── 20111207
├── 20111208
├── 20111209
├── 20111212
├── 20111213
├── 20111214
├── 20111215
└── 20111216

8 directories
```

Here's the directory structure for `data/20111207/`. Each elicitation
session gets its own directory, `1/` and `2/`.

```
20111207
├── 1
│   ├── analysis
│   │   ├── f0
│   │   └── scripts
│   ├── data
│   │   ├── tokens
│   │   └── trimmed
│   └── info
├── 2
│   ├── analysis
│   │   ├── f0
│   │   └── scripts
│   ├── data
│   │   ├── tokens
│   │   └── trimmed
│   └── info
└── analysis
    └── figs

18 directories
```

Within each elicitation session directory, there's three directories:

+ `analysis/`: this contains extracted f0 information and scripts
+ `data/`: this contains the audio files
+ `info/`: this contains spreadsheets and textfiles with elicitation
  item information
  
There's also an `analysis` directory in `data/20111207/` which
  contains files related to an analysis combining data from the two
  elicitation sessions.


Similarly, the directory structure for `20111213/` also contains
sub-directories for each elicitation session, `1/` and `2/`, each of
which include `analysis/`, `data/`, and `info/` directories. A
separate `info/` directory in `20111213/` contains spreadsheets and
textfiles combining information about both sessions.

```
20111213
├── 1
│   ├── analysis
│   │   ├── auto
│   │   ├── f0
│   │   ├── figs
│   │   └── scripts
│   ├── data
│   │   ├── raw
│   │   └── tokens
│   └── info
├── 2
│   ├── analysis
│   │   └── scripts
│   ├── data
│   │   └── raw
│   └── info
└── info
    └── raw-excel-files-from-rebecca

18 directories
```

Within the `20111213/1/data` directory the filenames are listed below:

```
20111213/1/data
├── 20111213-1-kiy-ap-framedwordlist-stereo.wav
├── 20111213-1-kiy-ap-framedwordlist.TextGrid
├── 20111213-1-kiy-ap-framedwordlist.TextGrid.blank
├── 20111213-1-kiy-ap-framedwordlist.wav
├── raw
│   └── 20111213-1-kiy-ap-framedwordlist.wav
└── tokens
    ├── 20111213-1-kiy-ap-framedwordlist-1.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-1.wav
    ├── 20111213-1-kiy-ap-framedwordlist-10.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-10.wav
    ├── 20111213-1-kiy-ap-framedwordlist-11.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-11.wav
    ├── 20111213-1-kiy-ap-framedwordlist-12.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-12.wav
    ├── 20111213-1-kiy-ap-framedwordlist-13.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-13.wav
    ├── 20111213-1-kiy-ap-framedwordlist-14.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-14.wav
    ├── 20111213-1-kiy-ap-framedwordlist-15.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-15.wav
    ├── 20111213-1-kiy-ap-framedwordlist-16.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-16.wav
    ├── 20111213-1-kiy-ap-framedwordlist-17.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-17.wav
    ├── 20111213-1-kiy-ap-framedwordlist-18.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-18.wav
    ├── 20111213-1-kiy-ap-framedwordlist-19.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-19.wav
    ├── 20111213-1-kiy-ap-framedwordlist-2.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-2.wav
    ├── 20111213-1-kiy-ap-framedwordlist-20.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-20.wav
    ├── 20111213-1-kiy-ap-framedwordlist-21.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-21.wav
    ├── 20111213-1-kiy-ap-framedwordlist-22.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-22.wav
    ├── 20111213-1-kiy-ap-framedwordlist-23.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-23.wav
    ├── 20111213-1-kiy-ap-framedwordlist-24.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-24.wav
    ├── 20111213-1-kiy-ap-framedwordlist-25.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-25.wav
    ├── 20111213-1-kiy-ap-framedwordlist-3.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-3.wav
    ├── 20111213-1-kiy-ap-framedwordlist-4.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-4.wav
    ├── 20111213-1-kiy-ap-framedwordlist-5.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-5.wav
    ├── 20111213-1-kiy-ap-framedwordlist-6.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-6.wav
    ├── 20111213-1-kiy-ap-framedwordlist-7.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-7.wav
    ├── 20111213-1-kiy-ap-framedwordlist-8.TextGrid
    ├── 20111213-1-kiy-ap-framedwordlist-8.wav
    ├── 20111213-1-kiy-ap-framedwordlist-9.TextGrid
    └── 20111213-1-kiy-ap-framedwordlist-9.wav

2 directories, 55 files
```
The `raw/` directory contains the original recorded file, and files in
`data/` are the downsampled, Channel 1 audio files processed from the
raw audio file and their associated Praat annotation files. The `tokens/` directory holds audio files of
individual elicitation items extracted from the elicitation session
recorded file in `data/` and associated Praat annotation files.

The elicitation session files are named after the elicitation session
ID, `20111213-1-kiy-ap-framedwordlist`. The individual token files are
named with a suffix that is the elicitation item ID,
e.g. `20111213-1-kiy-ap-framedwordlist-1`,
`20111213-1-kiy-ap-framedwordlist-2`, etc.

[^1]: It's also a bad idea to include spaces in filenames, as we
discuss in the section [Organizing files](#files).
[^2]: We created these HTML tables using the web-based
[table editor](http://truben.no/latex/table/), which is handy
for converting tables between various text formats (CSV,
tab-delimited, space-delimited) and LaTeX and html formats and other
formats used in web development.
[^3]: Flip also has a GUI implementation called [LineBreak](https://code.google.com/p/linebreak/).
[^4]: `g++` is available from [Xcode](https://developer.apple.com/xcode/) command line tools, which
you can install from the Mac App Store by downloading Xcode and
`Command Line Tools` for installation in the [Download preference pane](http://stackoverflow.com/questions/9329243/xcode-4-4-command-line-tools).
[^5]: The directory structure graphics are done via the command line
utility [`tree`](http://mama.indstate.edu/users/ice/tree/).
