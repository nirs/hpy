""" Collect all(?) builtin names recursively """

import sys

def collect(obj, names):
    for name in dir(obj):
        if name not in names:
            names.add(name)
            collect(getattr(obj, name), names)
    
names = set()
collect(globals()['__builtins__'], names)
names = list(names)
names.sort(key=str.lower) # case insensitive

# Create dictionary for translation.

print '# Python: %s' % sys.version.split(None, 1)[0]
print '# Builtin names: %d ' % len(names)

print 'builtins = {'
for name in names:
    line = "    u'': '%s'," % name
    print line.encode('utf-8')
print '}'