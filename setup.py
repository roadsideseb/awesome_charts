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

from distutils.core import setup

setup(
    name = 'awesome_charts',
    version = '0.1.0a',
    author = 'Sebastian Vetter',
    author_email = 'sebastian@roadside-developer.com',
    #url = '', 

    description = 'A simple tool to generate Awesome Bars with cool colours.',
    #long_description = awesome.__doc__,

    packages = [
        'awesome', 
        'colourlovers', 
    ],

    scripts = [
        'awesome_charts',
    ],

    #provides = ['colourlovers'],
    license = 'GNU General Public License (GPL)',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
    ]
)
