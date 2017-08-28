Title: Visualizing confusion matrices
status: draft
Latex:
Date: 2013-07-01 12:00
Tags: ldc-kiy, fieldwork, R, visualization, data-analysis
Slug: visualizing-confusion-matrices
Summary: Some R code for visualizing confusion matrices and generating
LaTeX tables

## Dinoj Surendran's confusion matrices ##

[Dinoj Surendran](http://research.microsoft.com/en-us/um/people/dinos/)
has an excellent webpage on acoustic confusion matrices you can find
at his old University of Chicago site
[here](http://people.cs.uchicago.edu/~dinoj/confmat.html). The links
to the confusion matrix data on that page are broken, but you can still find them
at the links below:

+ [Miller and Nicely 1955](http://people.cs.uchicago.edu/~dinoj/research/nicely.html)
+ [Wang and Bilger 1973](http://people.cs.uchicago.edu/~dinoj/research/wangbilger.html)

## R Code ##

http://cran.r-project.org/web/packages/reshape2/index.html
amoebe@moebius :: which xquartz
/opt/X11/bin/xquartz


    1. [200-2500 Hz, S/N = 12dB](http://people.cs.uchicago.edu/~dinoj/research/nicely_plus12db_200to2500hz.dat)
	2. [200-5000 Hz, S/N = 12dB](http://people.cs.uchicago.edu/~dinoj/research/nicely_plus12db_200to5000hz.dat)
    3. [2500-5000 Hz, S/N = 12dB](http://people.cs.uchicago.edu/~dinoj/research/nicely_plus12db_2500to5000hz.dat)



<div align = "center">
<figure>
<img src="/static/blog/img/2013/06/praat-finish.jpg"
alt = "Annotating sound files in Praat" width = "700">
<figcaption> Annotating sound files in Praat.</figcaption>
</figure>
</div><p></p>
