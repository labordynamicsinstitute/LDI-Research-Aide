---
layout: default
title:  Modifying this guide
nav_order: 500
--- 

- TOC
{:toc}

# Modifying this guide

This guide is built using Jekyll and Markdown. The structure is defined by the header of each file in the `docs` folder.

## All modifications

You should, if possible, create a new branch in the current repository, if you have the rights to. Otherwise, the edit link will create a fork. In both cases, submit a pull request with sufficient information to assess what you are trying to do.


## Modifying an existing page

To modify an existing page, simply edit the Markdown file in the `docs` folder. The header of the file defines the title of the page, its parent in the menu, and its order in the menu. A link to modify each page is at the bottom of the page, as `Edit on GitHub`. 


## Adding a new page

To add a new page, create a new Markdown file in the `docs` folder. The header of a new file that should appear in the `Procedures` menu should look like this:

```markdown
---
title:  New Page
parent: Procedures
nav_order: 5
--- 

# New Page
```

By convention, you should also create this file in the `docs/procedures` folder; however, that is not strictly necessary. You can influence the order in which the file is listed within the `Procedures` menu by changing the `nav_order` value. Lower values will appear higher in the list.

## Moving an existing page

If you need to move an existing page, you should change the `parent` value in the header of the file, as well as the actual location of the file in the `docs` folder.





