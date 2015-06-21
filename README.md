gender-swapper 
-------

A simple tool that swaps genders in written English text. 

Uses the online natural language [Text Processing API] (http://text-processing.com).

Meant to study how gender-specific the treatment of a character is in a given written work. Closely analyzing a gender swapped text often helps provide a better understanding of what plot elements are tied strongly to the character's gender. Analyzing multiple works by one author can help generalize any gender bias in his or her writing.

## Usage


You may run the (very rudimentary) provided TKinter GUI.

Alternatively, you can use module flip_file or flip in `genderflipper.py`:

```python

from genderflipper import flip, flip_file

names = {'sherlock': 'irene', 'holmes': 'adler'}
flip_file("input.txt", names)

```

```python

from genderflipper import flip, flip_file

names = {'sherlock': 'jane'}
flip("To Sherlock Holmes she is always THE woman.", names)

```

An internet connection is required.
