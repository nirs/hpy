#-*- coding: utf-8 -*-
import hpy

# Tranlate to Python

print hpy.translateString(u'הדפס "שלום עולם!"', hpy.pythonString)

multiline = u"""
א = 1
ב = 3
הדפס  א + ב
"""
print hpy.translateString(multiline, hpy.pythonString)

# Translate from Python

print hpy.translateString(u'print "שלום עולם!"', hpy.hebrewString).encode('utf-8')

multiline = u"""
hpy_d790 = 1
hpy_d791 = 3
print  hpy_d790 + hpy_d791
"""
print hpy.translateString(multiline, hpy.hebrewString).encode('utf-8')


