#!/usr/bin/python

import os
from os.path import join, getsize
from PIL import Image, ImageFilter
from PIL.ExifTags import TAGS, GPSTAGS


def get_field (exif,field) :
    #print exif
    for (k,v) in exif.iteritems():
        if TAGS.get(k) == field:
            return v


print "hello"

dir_root = "/home/david"


f = []
for (root, dirs, files) in os.walk(dir_root):
    for name in files:
        fullname = (os.path.join(root, name))
        #if '/.cache/' in fullname:
        #    continue
        #print fullname
        try:
            img = Image.open(fullname)
   
            
        except:
            #print "  not image"
            continue
        #print fullname
        #print img

        #print(img)
        try:
            info = img._getexif()
            #print info
        except:
            #print "  no exif"
            continue
        if info:
            dt = get_field(info, 'DateTime')
        else:
            continue
        
        
        #for (k, v) in info.iteritems():
        #    print '  %s = %s' % (TAGS.get(k), v)

        #print info
        print "%s  %s" % (fullname , dt)
        
        
        
