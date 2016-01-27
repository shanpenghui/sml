#!/usr/bin/env python
#update_readme_toc.py doc/mkdocs.yml README.md http://boost-experimental.github.io/msm-lite

import fileinput, sys, os

generating = False
for line in fileinput.input(sys.argv[2], inplace=True):
  if line.startswith('[](GENERATE_TOC_BEGIN)'):
    generating = True
    print(line)
    with open(sys.argv[1], 'r') as file:
      for line in file:
        index = line.split(':')
        if index[0][0] == '-':
          ext = ('.html' if index[1][1:-4] == 'index' else '/index.html')
          print('* [' + index[0][2:] + '](' + sys.argv[3] +'/' + index[1][1:-4] + ext + ')')
          path = os.path.dirname(sys.argv[1])
          with open((path + '/' if path != '' else '') + index[1][1:-1], 'r') as md:
            for line in md:
              if line.startswith('##'):
                name = line.replace('#', '')[:-1]
                id = filter(lambda c: c == '-' or str.isalnum(c), name.lower().replace(" ", "-")).replace("--", "")
                print('    * [' + name + '](' + sys.argv[3] + '/' + index[1][1:-4] + ext + "#" + id + ')')
    print
  elif line.startswith('[](GENERATE_TOC_END)'):
    generating = False
    sys.stdout.write(line)
  elif generating == False:
    sys.stdout.write(line)

