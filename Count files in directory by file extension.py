import os

# Get directory path of this script.
rootdir = os.path.dirname(__file__)

d = {}

def getExtension(path):
    '''Return file extension of inputted path.'''
    return os.path.splitext(path)[1]

def getScriptName():
    '''Get the filename of this script.'''
    import os.path
    return os.path.splitext(os.path.basename(__file__))[0]

for subdir, dirs, files in os.walk(rootdir):
    # Walk directories, count files by extension.
    for file in files:
        ext = getExtension(file).lower()
        if ext in d:
            d[ext] += 1
        else:
            d[ext] = 1

with open("{} output.txt".format(getScriptName()), "w", encoding='utf-8') as f:
    # Output contents of dictionary to text file.
    f.write("{}".format(d))