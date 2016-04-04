Title: Markdown and LaTeX reference
Date: 2013-06-21 9:33
Author: Kristine Yu
Tags: coding, markdown, tutorial
Slug: markdown-and-latex-reference


Practice with markdown based on
[John Gruber's Markdown page](http://daringfireball.net/projects/markdown/). Pelican
works with the [Python Markdown](http://pythonhosted.org/Markdown/)
Markdown processor. Also some practice with $\LaTeX$ using the
[Pelican latex plugin](https://github.com/getpelican/pelican-plugins/tree/master/latex),
which uses [MathJaX](http://www.mathjax.org/). **Update: 04/2015: the latex
plugin is deprecated and has been superseded by the
[render_math plug-in](https://github.com/getpelican/pelican-plugins/tree/master/render_math).**

* [Core Markdown](#core-markdown)
* [Python Markdown extensions](#py-markdown)
* [Code blocks and syntax highlighting](#code)
* [LaTeX](#latex)
<!-- PELICAN_END_SUMMARY -->

## <a id = "core-markdown"></a> Core Markdown reference ##

### Text formatting

#### Headlines and horizontal rules ####

Headline depth can be indicated with #, e.g.

# H1, with '#'
## H2, with '##'
### H3, with '###'

Headlines for H1 and H2 can also be indicated with "underlining":

	H1
    ====

	H2
    ----- 

H1
====


H2
----- 

Horizontal rules can be indicated with 3+ of *, - or _:

    ***
    ---
    ___


***

---

___

#### Emphasis
Emphasized text can be indicated with * or _

1. Emphasized text looks like *this* or _this_
2. Strong text can be indicated with double * or _,
e.g. **this** or __this__
3. Strong and emphasized text can be indicate with triple asterisks,
***like this***

#### Blockquotes
Blockquotes can be indicated with >

> Here's a blockquote.

> Here's another blockquote.

#### Lists

Items in itemized lists can be enumerated with +, -, * for unordered lists or with 1., 2., 3. for ordered lists.

```text
* Unordered item
* Another unordered item
* Yet another unordered item
```

* Unordered item
* Another unordered item
* Yet another unordered item

```text
1. Item 1
2. Item 2
3. Item 3
```

1. Item 1
2. Item 2
3. Item 3


```text
* Item, followed by blank line

* Item with new paragraph
```

* Item, followed by blank line

* Item with new paragraph


### Links

#### In-line link
    [link text](link "Optional title")
    [blog](http://www.krisyu.org "blog")

[Kristine's blog](http://www.krisyu.org "blog")

#### Referenced link


```text
Here's a link to [UMass Linguistics][1] and here's one to [UCLA
Linguistics][2]

[1]: http://www.umass.edu/linguist "UMass Linguistics"
[2]: http://www.linguistics.ucla.edu "UCLA Linguistics"
```

Here's a link to [UMass Linguistics][1] and here's one to [UCLA Linguistics][2]

[1]: http://www.umass.edu/linguist "UMass Linguistics"
[2]: http://www.linguistics.ucla.edu "UCLA Linguistics"


### Images

In-line images: 

```text
![Sideways kitties](/static/blog/img/2013/06/emmy-sophie-sideways.jpg "Emmy and Sophie")
```

![Sideways kitties](/static/blog/img/2013/06/emmy-sophie-sideways.jpg "Emmy
and Sophie")

Reference-style images: 

```text
![Young Indie][indie]
![Baby Hunter][hunter]

[indie]: /static/blog/img/2013/06/indie.jpg "Young Indie"
[hunter]: /static/blog/img/2013/06/hunter.jpg "Baby Hunter"
```

![Young Indie][indie]

![Baby Hunter][hunter]

[indie]: /static/blog/img/2013/06/indie.jpg "Young Indie"
[hunter]: /static/blog/img/2013/06/hunter.jpg "Baby Hunter"

---------------------------------

## <a id = "py-markdown"</a>Python Markdown extensions

[Pelican settings documentation](http://docs.getpelican.com/en/3.2/settings.html)
lists `MD_EXTENSIONS` as a configurable setting, with the default:

`MD_EXTENSIONS (['codehilite(css_class=highlight)','extra'])`

Supported Python Markdown extensions are listed
[here](http://pythonhosted.org/Markdown/extensions/). The default
setting of `extra` for `MD_EXTENSIONS` includes the following set of extensions:

###[Attribute lists](http://pythonhosted.org/Markdown/extensions/attr_list.html)###

Here's an example of specifying the *id* for a header:

    ### A hash style header ### {: #barcode }
	
is rendered as

```html
<h3 id="barcode">A hash style header</h3>
```

Here's an example of specifying the *id* and *class* for a paragraph
element:

	This is a paragraph.
	{: #an_id .a_class }
		
is rendered as

```html
<p id="an_id" class="a_class">This is a paragraph.</p>
```

	[link](http://example.com){: class="class_name" title="link title" }

is rendered as

```html
<p><a href="http://example.com" class="foo bar" title="Some title!">link</a></p>
```

###[Footnotes](http://pythonhosted.org/Markdown/extensions/footnotes.html)###

```
The cat that chased the rat meowed.[^1]

[^1]: Whoa, is this some embedding?
```

The cat that chased the rat meowed.[^1]

[^1]: Whoa, is this some embedding?

###[Tables](http://pythonhosted.org/Markdown/extensions/tables.html)###

```
Lexer  | shortname | file extensions
------------- | ------------- | ----------
`Python3Lexer`  | python3, py3 |
`PythonLexer`  | python, py | \*.py, \*.pyw, \*.sc, SConstruct, SConscript, \*.tac, \*.sage
`PythonConsoleLexer`  | pycon |
`PrologLexer` | prolog | \*.prolog, \*.pro, \*.pl
```

Lexer  | shortname | file extensions
------------- | ------------- | ----------
`Python3Lexer`  | python3, py3 |
`PythonLexer`  | python, py | \*.py, \*.pyw, \*.sc, SConstruct, SConscript, \*.tac, \*.sage
`PythonConsoleLexer`  | pycon |
`PrologLexer` | prolog | \*.prolog, \*.pro, \*.pl

###[Smart Strong](http://pythonhosted.org/Markdown/extensions/smart_strong.html)###

This treats double underscores within words intelligently??

```text
___first___second____third
```

___first___second____third

###[Abbreviations](http://pythonhosted.org/Markdown/extensions/abbreviations.html)###

	*[ATP]: adenosine triphosphate
	*[PDCB]: paradichlorobenzene

	The molecule ATP provides energy to molecular motors. PDCB is a
	common ingredient in mothballs.


The molecule ATP provides energy to molecular motors. PDCB is a
common ingredient in mothballs.

*[ATP]: adenosine triphosphate

*[PDCB]: paradichlorobenzene



###[Definition lists](http://pythonhosted.org/Markdown/extensions/definition_lists.html)###

	ineffable
	:   the property of being undefinable

	ambisinistrous
	:   equally clumsy with both hands, from *Latin* `both left`


ineffable
:   the property of being undefinable

ambisinistrous
:   equally clumsy with both hands, from *Latin* `both left'

---------------------------------

###<a id = "code"></a>[Fenced Code Blocks](http://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html) and [syntax highlighting](http://pythonhosted.org/Markdown/extensions/code_hilite.html)###

Core Markdown syntax uses
[indenting](http://daringfireball.net/projects/markdown/syntax#precode)
for code blocks. John Gruber's documentation says:

> To produce a code block in Markdown, simply indent every line of the block by at least 4 spaces or 1 tab. 

but Python Markdown extensions allow
[fenced code blocks](http://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html),
which play nice with list indentation. From the [documentation](http://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html):

> Fenced code blocks can have a blank line as the first and/or last line of a code block and they can also come immediately after a list item without becoming part of the list.

##### Fenced code blocks ####

With `~~~~{.python} ... ~~~~`:

~~~~{.text}
~~~~{.python} # block open (don't include this comment in your code)
# python code
print 'Hello world'
~~~~ # block close (don't include this comment in your code)
~~~~

~~~~{.python}
# python code
print 'Hello world'
~~~~

With Github-flavored backticks: ` ```python ... ``` `:

```text
```python # block open (don't include this comment in your code)
# python code
print 'Hello world'
``` # block close (don't include this comment in your code)
```

```python
# python code
print 'Hello world'
```
#### Syntax highlighting ####

Syntax highlighting is enabled by default in Pelican with the
    extension
    [`CodeHilite`](http://pythonhosted.org/Markdown/extensions/code_hilite.html),
    which uses the Python syntax highlighter
    [Pygments](http://pygments.org/).

You can **have line numbers shown** if the first line contains a
[shebang](http://www.in-ulm.de/~mascheck/various/shebang/), `#!`. Here's an example with a fenced code block:

~~~~{.text}
~~~~ # opening fence (don't include this comment in your code)
#!/usr/bin/python
# python code, line numbers and shebang line shown
print 'Hello world'
~~~~ # closing fence (don't include this comment in your code)
~~~~

~~~~
#!/usr/bin/python
# python code, line numbers and shebang line shown
print 'Hello world'
~~~~

And here's an example with line numbers shown using an indented code block:

```text
    #!/usr/bin/python
    # python code, line numbers and shebang line shown
    print 'Hello world'
```

    #!/usr/bin/python
    # python code, line numbers and shebang line shown
    print 'Hello world'
<p></p>

Without a path in the shebang line, i.e. `#!python` the shebang line
is removed. So there are only 2 lines in the code below, not 3.

~~~~{.text}
~~~~ # opening fence (don't include this comment in your code)
#!python
# python code, line numbers and shebang line not shown
print 'Hello world'
~~~~ # closing fence (don't include this comment in your code)
~~~~

~~~~
#!python
# python code, line numbers and shebang line shown
print 'Hello world'
~~~~
<p></p>

For **no** line numbers, and without the first line being displayed,
you can use a triple colon, `:::python`.

Here's an example with a fenced code block:

```text
~~~~ # opening fence (don't include this comment in your code)
:::python
# python code, no line numbers, first line not shown
print 'Hello world'
~~~~ # closing fence (don't include this comment in your code)
```
~~~~ 
:::python
# python code, no line numbers, first line not shown
print 'Hello world'
~~~~ 

And here's an example with an indented code block:

```text
    :::python
    # python code, no line numbers, first line not shown
    print 'Hello world'
```

    :::python
    # python code, no line numbers, first line not shown
    print 'Hello world'

#### Syntax highlighting: languages supported by pygments ####

The [list of supported languages](http://pygments.org/languages/)
includes Awk, C, C++, F#, Haskell, Java, Javascript, Matlab,
Octave, OCaml, Prolog, Python,  S/S+/R, Bash shell scripts,
Gnuplot scripts, HTML, MySQL, TeX, XML. Here is a table of some
[shortnames](http://pygments.org/docs/lexers/) for some lexers for
languages I use or could imagine using:

Lexer  | shortname | file extensions
------------- | ------------- | ----------
`Python3Lexer`  | python3, py3 |
`PythonLexer`  | python, py | \*.py, \*.pyw, \*.sc, SConstruct, SConscript, \*.tac, \*.sage
`PythonConsoleLexer`  | pycon |
`PrologLexer` | prolog | \*.prolog, \*.pro, \*.pl
`CommonLispLexer` | common-lisp, cl, lisp | \*.cl, \*.lisp, \*.el
`CoqLexer` | coq | \*.v
`OcamlLexer` | ocaml | \*.ml, \*.mli, \*.mll, \*.mly
`SchemeLexer` | scheme, scm | \*.scm, \*.ss
`MatlabLexer` | matlab | \*.m
`MatlabSessionLexer` | matlabsession |
`NumPyLexer` | numpy |
`OctaveLexer` | octave | \*.m
`RConsoleLexer` | rconsole, rout |
`SLexer` | splus, s, r | \*.S, \*.R, .Rhistory, .Rprofile
`AwkLexer` | awk, gawk, mawk, nawk | \*.awk
`GnuplotLexer` | gnuplot | \*.plot, \*.plt
`BashLexer` | bash, sh, ksh | \*.sh, \*.ksh, \*.bash, \*.ebuild, \*.eclass, .bashrc, bashrc, .bash\\*, bash\\*
`BashSessionLexer` | console | \*.sh-session
`ShellSessionLexer` | shell-session | \*.shell-session
`TextLexer` | text | \*.txt
`MySqlLexer` | mysql |
`IrcLogsLexer` | irc | \*.weechatlog
`MakefileLexer` | make, makefile, mf, bsdmake | \*.mak, Makefile, makefile, Makefile.\*, GNUmakefile
`TexLexer` | tex, latex | \*.tex, \*.aux, \*.toc
`CssLexer` | css | \*.css
`HtmlLexer` | html | \*.html, \*.htm, \*.xhtml, \*.xslt

Some R with `~~~~ {.R}`:

~~~~ {.R}
# R code
a <- c(2,3,5,8)
b <- c(3,1,4,1)
variable <- rbind(a,b)
~~~~

Some Matlab, using ````matlab`:

```matlab
# MATLAB code
% praat call was successful, return F0 values
F0 = zeros(datalen, 1) * NaN; 

fid = fopen(f0file, 'rt');

% read the rest
C = textscan(fid, '%f %f', 'delimiter', '\n', 'TreatAsEmpty', '--undefined--');
fclose(fid);

t = round(C{1} * 1000);  % time locations from praat pitch track
```

A bash session:

```console
# Extract from output of cat command after flip line ending conversion
amoebe@moebius :: cat 20111215-2-kiy-ap-framedwordlist.txt.unix
item	word.1	word.2	verb	gloss.1	gloss.2	gloss.verb	tone.1	tone.2	bitone	sent.kiy	sent.eng
1	kE	ndE	fuwa	ant	centipede	sees	T1	T1	T1.T1	kE ndE fuwa.	The ant sees the centipede.
2	kE	fa	fuwa	ant	younger.sibling	sees	T1	T2	T1.T2	kE fa fuwa.	The ant sees the younger.sibling.
3	kE	nO	fuwa	ant	meat	sees	T1	T2	T1.T2	kE nO fuwa.	The ant sees the meat.
4	kE	fO	fuwa	ant	wallaby	sees	T1	T3	T1.T3	kE fO fuwa.	The ant sees the wallaby.
5	kE	fO	fuwa	ant	honeybee	sees	T1	T3	T1.T3	kE fO fuwa.	The ant sees the honeybee.
```

---------------------------------


##<a id = "latex"></a> $\LaTeX$ ##

The Pelican $\LaTeX$
[plug-in](https://github.com/getpelican/pelican-plugins/tree/master/latex)
uses [MathJaX](http://www.mathjax.org/). **Update: 04/2015: the latex
plugin is deprecated and has been superseded by the
[render_math plug-in](https://github.com/getpelican/pelican-plugins/tree/master/render_math).** Here is a list of
[available commands](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm). It
seems that you need to type `\\` for `\`. Some more MathJaX
troubleshooting tips are [here](http://www.wikidot.com/doc:math).

	```latex
	Here is an in-line equation $\sqrt{3x-1}+(1+x)^2$ in the body of the text.
	```

Here is an in-line equation $\sqrt{3x-1}+(1+x)^2$ in the body of the text.

Here is an equation:

```latex
$\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi$
```

$\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi$

You can use the `array` environment for tables, since the `tabular`
environment is
[not supported by MathJaX](http://meta.math.stackexchange.com/questions/2016/tabular-in-mathjax). There's
an
[example of an `array` environment substitute](https://groups.google.com/forum/#!msg/mathjax-users/4btEfmThia0/GqH99mEZGLwJ)
at the MathJax Google Group, repeated here:

```latex
$
\newcommand\\T{\\Rule{0pt}{1em}{.3em}}
\\begin{array}{|c|c|}
\\hline X & P(X = i) \\T \\\\\\hline
1 \\T & 1/6 \\\\\\hline
2 \\T & 1/6 \\\\\\hline
3 \\T & 1/6 \\\\\\hline
4 \\T & 1/6 \\\\\\hline
5 \\T & 1/6 \\\\\\hline
6 \\T & 1/6 \\\\\\hline
\\end{array}
$
```
	
$
\\newcommand\\T{\\Rule{0pt}{1em}{.3em}}
\\begin{array}{|c|c|}
\\hline X & P(X = i) \\T \\\\\\hline
1 \\T & 1/6 \\\\\\hline
2 \\T & 1/6 \\\\\\hline
3 \\T & 1/6 \\\\\\hline
4 \\T & 1/6 \\\\\\hline
5 \\T & 1/6 \\\\\\hline
6 \\T & 1/6 \\\\\\hline
\\end{array}
$

Another `array` environment table
[example](http://math.stackexchange.com/questions/15008/sum-of-series-fracxkn-k#15026)
from [math.stackexchange.com](math.stackexchange.com) is shown below:

```latex
$
\\begin{array}{ccc}x&S(n,x)&x^n
\\log\\left(\\frac{x}{x-1}\\right)\\\\
-5&-1780484.04&-1780483.95\\\\
-3&-16987.42&-16987.34\\\\
2&709.598&709.783\\\\
4&301656.39&301656.52\\\\
6&1.102428722 \\times 10^7&1.102428734 \\times
10^7
\\end{array}
$
```

$
\\begin{array}{ccc}x&S(n,x)&x^n
\\log\\left(\\frac{x}{x-1}\\right)\\\\
-5&-1780484.04&-1780483.95\\\\
-3&-16987.42&-16987.34\\\\
2&709.598&709.783\\\\
4&301656.39&301656.52\\\\
6&1.102428722 \\times 10^7&1.102428734 \\times
10^7
\\end{array}
$
