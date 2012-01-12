#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

from datetime import datetime

try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree

class ColourLoversError(BaseException):
    pass

class RGB(object):
    
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def hex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue) 

    @classmethod
    def from_xml(cls, xml):
        red = xml.find('red').text
        green = xml.find('green').text
        blue = xml.find('blue').text

        return cls(red, green, blue)

    def __repr__(self):
        return "<%s (%s, %s, %s)>" % (
            self.__class__.__name__,
            self.red,
            self.green,
            self.blue
        )

class HSV(object):
    
    def __init__(self, hue, saturation, value):
        self.hue = hue 
        self.saturation = saturation 
        self.value = value

    @classmethod
    def from_xml(cls, xml):
        hue = xml.find('hue').text
        saturation = xml.find('saturation').text
        value = xml.find('value').text

        return cls(hue, saturation, value)

    def __repr__(self):
        return "<%s (%s, %s, %s)>" % (
            self.__class__.__name__,
            self.hue,
            self.saturation,
            self.value
        )

class Colour(object):

    def __init__(self, colour_id):
        self.id = colour_id 
        self.title = None
        self.username = None
        self.date_created = None
        self.rgb = None
        self.hsv = None

    @classmethod
    def from_xml(cls, xml):
        inst = cls(xml.find('id').text)
        inst.title = xml.find('title').text
        inst.username = xml.find('userName').text

        inst.date_created = datetime.strptime(
            xml.find('dateCreated').text,
            '%Y-%m-%d %H:%M:%S'
        )

        inst.hsv = HSV.from_xml(xml.find('hsv'))
        inst.rgb = RGB.from_xml(xml.find('rgb'))

        print inst
        return inst

    def __repr__(self):
        return "<%s id='%s' title='%s' rgb=(%s, %s, %s)>" % (
            self.__class__.__name__,
            self.id,
            self.title.encode('ascii', 'ignore'),
            self.rgb.red,
            self.rgb.green,
            self.rgb.blue
        )

class Palette(object):

    def __init__(self, palette_id):
        self.id = int(palette_id)
        self.title = None
        self.username = None
        self.views = None
        self.votes = None
        self.comments = None
        self.hearts = None
        self.rank  = None
        self.date_created = None

        self.colours = []

    @classmethod
    def from_xml(cls, xml):
        inst = cls(xml.find('id').text)

        inst.title = xml.find('title').text
        inst.username = xml.find('userName').text
        inst.views = int(xml.find('numViews').text)
        inst.votes = int(xml.find('numVotes').text)
        inst.comments = int(xml.find('numComments').text)
        inst.hearts = float(xml.find('numHearts').text)
        inst.rank  = int(xml.find('rank').text) 
        inst.date_created = datetime.strptime(
            xml.find('dateCreated').text,
            '%Y-%m-%d %H:%M:%S'
        )

        for hex_colour in xml.findall('colors/hex'):
            inst.colours.append('#'+hex_colour.text.lower())

        return inst

    def __repr__(self):
        return u"<%s id='%d' title='%s'>" % (
            self.__class__.__name__,
            self.id,
            self.title.encode('ascii', 'ignore'),
        )


class ColourLovers(object):

    API_URL = 'http://www.colourlovers.com/api'

    def __init__(self):
        pass

    def get_colour(self, argument=None, **kwargs):
        xml = self.__call('color', argument)

        colors = []
        for color in xml.findall('color'):
            colors.append(
                Colour.from_xml(color)
            )

        return colors

    def get_palettes(self, argument=None, **kwargs):
        xml = self.__call('palettes', argument)

        palettes = []
        for palette in xml.findall('palette'):
            palettes.append(
                Palette.from_xml(palette)
            )

        return palettes

    def get_palette(self, argument=None, **kwargs):
        xml = self.__call('palette', argument)

        palettes = []
        for palette in xml.findall('palette'):
            palettes.append(
                Palette.from_xml(palette)
            )

        return palettes


    def __call(self, method, argument=None, **kwargs):
        if argument is None:
            url = "%s/%s" % (self.API_URL, method)
        else:
            url = "%s/%s/%s" % (self.API_URL, method, argument)

        req = urllib2.Request(
            url,
            data=urllib.urlencode(kwargs),
            headers={'User-Agent': 'Magic Browser'},
        )
        return self.__check_response(urllib2.urlopen(req).read())

    def __check_response(self, response):
        try:
            xml = ElementTree.XML(response)
        except:
            raise ColourLoversError(
                "could not retrieve result for your request"
            )
        return xml

