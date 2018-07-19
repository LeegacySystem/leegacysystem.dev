---
title:  "The First Dump"
date:   2018-07-12 18:42:23
categories: [jekyll]
tags: [jekyll]
---


## The First Dump

This is simply a note to myself on how to fix the midnight Jekyll theme should any others have the same problem. This was mainly figured out by trial and error along with some comparisons with working github page sources.

As I've already forgotten how I fixed it, [see commit#5](https://github.com/lee2098/lee2098.github.io/commit/6f95a64446d2a02505db3780a148cb541c8db0eb) with file change highlights below:

#### *1) Gemfile.lock*
There are a lot of additions in here. I think this is just a mistake while messing around with the local bundle. Best guess .lock is simlar to a .swp file but will look up at some point as I know very little about ruby.

#### *2) 2018-07-12-welcome-to-jekyll.markdown*
This is a minor change to the yaml frontmatter telling the Jekyll templating system to use the default (see below) layout.

#### *3) about.md & index.md*
Same as above

---

###### **Notes -** creating _layouts/default doesn't seem to show in the commit review (need to figureo out why)


Below is just a test to see code formating
```s
#!/usr/bin/env python
#http://www.pythonforbeginners.com/code-snippets-source-code/python-script-log-checker/
logfile = open("/var/log/syslog", "r")
for line in logfile:
    line_split = line.split()
    print line_split
    list = line_split[0], line_split[1], line_split[2], line_split[4]
    print list
```
