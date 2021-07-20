# 4. File Finder

Let `dirs` be a recursively-defined nested list, representing a directory tree containing an arbitrary number of directories, sub-directories and files.


Consider the following example:


`dirs = ["home",
 ["Documents",
 [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
 [ "Python", "hello_world.py", "readme.md" ],
 ],
 ["Downloads",
 [ "Movies",
 [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],
 "1.avi", "22", "001.mp4"
 ],
 ],
 "tmp.txt", "page.html"
 ]`


In the above example, each directory is defined by a list, and the first element of the list is the name of that directory (home, Documents, FPRO, etc). The rest of the elements of a list contain either strings, which are filenames inside that directory, or lists, which contain a sub-directory.


Write a Python function `file_finder(dirs, file_name)` that returns the full path of a file `file_name` (given as a string), or `None` if it is not in the directory tree `dirs`. Inside a directory, the function opens the sub-directories before looking at the files. The full path of a file includes the slash-separated names of all the directories that contain it. Therefore, the full path of `"BreakingBad.mp4"` is `"home/Downloads/Movies/TV Series/BreakingBad.mp4"`.



## Private Tests [100%]

## Public Tests [100%]
