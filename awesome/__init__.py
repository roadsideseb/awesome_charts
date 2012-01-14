#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# awesome_charts - A simple tool to generate Awesome Bars with cool colours.
# Copyright (C) 2012 Sebastian Vetter
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License

import itertools

from svgplotlib import Base
from svgplotlib import getFont
from svgplotlib.Pie import Pie
import svgplotlib.Config as Config
from svgplotlib.SVG import SVG, show


class AwesomeBar(Base):
   
    def __init__(self, title, values, labels, colors=None, **kwargs):
        # smaller default font
        if not 'fontSize' in kwargs:
            kwargs['fontSize'] = 12 

        super(AwesomeBar, self).__init__(**kwargs)

        titleScale = kwargs.get('titleScale', 2.2)
        titleColor = kwargs.get('titleColor', 'black')
        labelColor = kwargs.get('labelColor', 'black')

        spacing = kwargs.get('spacing', 0)

        if colors is None or len(colors) == 0:
           colors = self.COLORS
        
        style = self.style = {
            'stroke'        : 'black',
            'stroke-width'  : '1',
            'fill'          : 'black',
        }
        
        textStyle = self.textStyle = {
            'stroke'        : 'none',
        }
 
        main_group = self.Group(**style)

        # plot area size
        self.plotWidth = WIDTH = kwargs.get('size', 1000)
        self.plotHeight = kwargs.get('size', 90)
        
        HEIGHT = self.plotHeight - 2 * self.PAD

        dy = self.PAD
        dx = self.PAD 

        self.set('width', WIDTH)
        self.set('height',  self.plotHeight)

        titleSize = self.textSize(unicode(title))
        title_y = dy + (self.plotHeight / 2) + self.PAD
        title_y -= (titleScale * (titleSize.height + titleSize.descent) / 2)

        text = main_group.EText(
            self.font, 
            title, 
            x=dx, 
            y=title_y, 
            scale=titleScale,
            **{'stroke': 'none'}
        ) 

        plot_x = dx + 200
        plot_y = dy

        colouriter = itertools.cycle(colors)
        plot_area = main_group.Group(transform="translate(%g,%g)" % (plot_x, plot_y), **style)

        bar_width = WIDTH - plot_x - (spacing * (len(values)-1))

        bar_x = bar_y = 0
        for value, label in zip(values, labels):

            ## rectangle width is percentage of bar width
            rect_width = int((float(value) / 100.0) * bar_width)

            hex_colour = colouriter.next()

            plot_area.Rect(
                x=bar_x,
                y=bar_y,
                width=rect_width,
                height=HEIGHT,
                stroke=hex_colour,
                fill=hex_colour
            )

            label_size = self.textSize(unicode(label))

            label_style = {
                'stroke': 'none', 
                ## calculate colour for legible text
                'fill': self.smarty_modifier_contrast(hex_colour)
            }

            text_y = (bar_y + (HEIGHT / 2)) - (self.textSize(unicode(label))[1] / 2)
            text = plot_area.EText(
                self.font, 
                label, 
                x=bar_x+10, 
                y=text_y, 
                **label_style
            ) 

            bar_x = bar_x + rect_width + spacing

    @staticmethod
    def smarty_modifier_contrast(hexcolor, dark='black', light='white'):
        """ Method based on http://particletree.com/notebook/calculating-color-contrast-for-legible-text """
        if int(hexcolor.replace('#', ''), 16) > (0xffffff / 2):
            return dark
        return light
