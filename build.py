#-*- coding: utf-8 -*-
import re
import string
import glob
import os.path
import io


header = """
# Bookmarks
"""

footer = """
## Usage
### Preview commit
```
$ ./build
```
### Commit changes
```
$ ./build apply
```
### Generate `README.md` manually
```
$ python3 build.py
```
"""

def make_pretty_name(name):
    pretty_name = re.sub(r'-', ' ', name)
    return string.capwords(pretty_name)


readme = io.open('README.md', 'r+', encoding='utf-8')
readme.write(header)

files = sorted(glob.glob('docs/**', recursive=True))
documents = []
directories = []

for file in files:
    if file.endswith('.md'):
        documents.append(file)

for document in documents:
    title = re.sub('docs/|\.md', '', document).capitalize()
    readme.write(f"* [{title}]({document})\n")


#for directory in directories:
#    readme.write("\n## " + directory.capitalize() + "\n")
#    sub_files = glob.glob(directory + '/*.md')
#    for sub_file in sub_files:
#        readme.write("* [" + make_pretty_name(os.path.basename(sub_file)) + "](" + sub_file + ")\n")

readme.write(footer)
readme.close()
