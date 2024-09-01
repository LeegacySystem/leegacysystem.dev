---
title:  "Hugo"
date:   2024-09-24 13:30:23
categories: [Firewall]
tags: 
- IEEE 
---



* Hugo is a modern static site generator built on Golang.
* Markets its speed

Static Vs Dynamic websites
* Dynamic website would be something like facebook, content changes based on context.
* Static is static, not based on users or actions
* Static is cheaper
* Static has less flexibility


* Content is written in markdown
* Hugo community themes


Directory Structure
___

└───test_site
    ├───archetypes  - Define data/metadata about conent 
    ├───assets      - 
    ├───content     - Content of the website
    ├───data        - Almost database of website
    ├───i18n        - 
    ├───layouts     - Same headers/footers or other layout components
    ├───static      - Images/css/javascript that does not change reguarly
    └───themes      - Allows prebuilt themes.
    config.toml     - Main config settings file

___

Themes

Collection of hugo templates & layouts


https://www.besthugothemes.com/

Themes are normally git repos, to install simply clone theme to themes folder

theme arguement to be added to config.toml



____
Resources

https://github.com/theNewDynamic/awesome-hugo