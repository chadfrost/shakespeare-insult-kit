# shakespeare-insult-kit
Random insult generator using words from Shakespeare's writing

I got the list from online PDFs, which meant the copy-paste from three columns was a space-separated mess!  I re-formatted into a single column in Vim, using :%s\s\+/^M/g (^M entered as ctl-V, M) and saved that list as 'shakespeare.txt'. I then read that file and chunked the words into the original three columns using the 3col.py script.

Original list from... I don't remember, it's all over the place. Additional words from Chris Seidel, http://www.pangloss.com/seidel/shake_rule.html 
