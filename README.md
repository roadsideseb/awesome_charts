Awesome Charts
==============

*Awesome Charts* is a small commanline tool that uses [svgplotlib]
(http://code.google.com/p/svgplotlib) and [ColourLovers]
(http://www.colourlovers.com) to generate an awesome bar. The awesome bar is
an idea found on the website of [Tangent/One](http://www.tangentone.com.au).
The tool allows for generating an SVG graphic specifying a title and a list of
things that make you awesome :)

Example using commandline:

    python awesome_charts -t "Beer" -a "Beck's:30" 'Yukon Lead Dog:20' "Fede's Own:30" 'Chocolate Stout:20' -p 1493514

Example using input file:

    python awesome_charts -i input.txt

The input file format is based on the commandline options. The input file 
provides one AwesomeBar definition per line and all options are separated
by the ``;`` delimiter. Label and percentage for each block in the 
Awesome bar is defined in the format ``label:percentage``. 

Sample line in an input file ``input.txt``:

    #Title; ColourLovers Palette ID; Output File; label:percentage list separated by ';'
    Notable Talents; 1234; notable_talents.svg; Making Lists:20; Universal Beer Bottle Opener:30; DIY:20; Vim & Vimperator:30

