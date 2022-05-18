# Miscellaneous Programming Tips

#### Compare files from one directory to another
Find all files in one directory using bash/terminal:

```
cd PATH
find . -type f
```

Export file list to a csv file:
```find . -type f > list.csv```

#### Run R script from command line
The below command line prompt runs the R script and creates a log file:
```R --vanilla < File_Name.R > File_Name.Rlog```

#### Convert word file to latex with "Pandoc" 
- Install pandoc from [here](https://pandoc.org/installing.html)
- Open command prompt
- cd to working directory of word file 
- Type: "file.docx -f docx -t latex -s -o newfile.tex"

#### Create BibTex file
You have a plain-text bibliography (it wasn’t generated using any type of tool)

Use [AnyStyle](https://anystyle.io).

1. Paste your citations into the textarea. Make sure each reference starts on a new line and remove any superfluous line breaks.
2. Click the parse button and AnyStyle will split the references into segments. If any section is labelled incorrectly, you can select it (use the Shift and Ctrl/Command to make multiple selections or double-click to select an entire segment at once). Then use the Assign Label button to assign the correct label.
3. Save it as BibTeX.


#### Stata Programming
aearep-2215 excellent stata programming. 

#### Bash

**sed**
- This should replace the path "/Users/lars/" with "$rootdir/" in every .do file.
- The "s" is the substitute command of sed for find and replace.
- The "+" is the delimiter for breaking up the 'old' and 'new' statements. 
- For any `\` that need to be changed, you'll need to replace with `\\`.

```sed -i 's+/Users/lars/+$rootdir/+g' *do```

**grep**
Look through any .do files for a dataset name "mydata" by typing the following into the bash shell:
```grep mydata */*.do```

**find**
Get a file count in the "folder" directory
```find folder/ -type f | wc -l```

