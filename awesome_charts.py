#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math
import argparse

from svgplotlib import getFont
from svgplotlib.Pie import Pie
import svgplotlib.Config as Config
from svgplotlib.SVG import SVG, show

dev = {
    'web': (20, 'blue'), 
    'testing': (30, 'green'),
    'research': (30, 'red'),
    'software': (20, 'orange')
}

def main():

    graph = Pie(
        [x[0] for x in dev.values()],
        title='Simple pie plot',
        labels=dev.keys(),
    )

    #show(graph, graph.width, graph.height)


    svg = SVG(width="800", height="100")
    #g = svg.Group(stroke = "black", fill='none')# transform="translate(75,75)")

    x = y = 0
    spacing = 5

    font = getFont(
        family=Config.DEFAULTFONT,
        style=Config.DEFAULTFONTSTYLE,
    )
    font.set_size(Config.DEFAULTFONTSIZE)

    font.load_char(ord('m'))
    print Config.DEFAULTFONTSIZE, font.get_width_height()

    calc_width = svg.width - (spacing * (len(dev)-1))
    for label, (wfrac, colour) in dev.items():
        width = int((float(wfrac) / 100.) * calc_width)
        g = svg.Group(stroke=colour, fill=colour)
        g.Rect(x=x, y=y, width=width, height=svg.height)

        xpos = x + (width / 2) - (len(label) * Config.DEFAULTFONTSIZE)
        print font.units_per_EM
        text = g.EText(font, label, x=xpos+10, y=50, **{'stroke': 'black', 'fill':'black'}) 
        print text.attrib

        x = x+width+spacing

    show(svg, svg.width, svg.height)
    svg.write(open('test.svg', 'w'))

if __name__ == "__main__":
    main()
