This repo will contain as many single file and small, flat-hierarchy python projects as possible for a 100 days of code challenge.


===Notes about connecting with Replit===
My replit.com "Repl" was locked as a bash project.

In the .replit file sitting in the root of the repl I tried changing: 
language="bash"
to: 
language="python"
and left this alone: 
run=""

No go.
Pushed what I had to github,
Disconnected repl from the repo,
Deleted the repl,
Created new Python repl with the same name,
reconnected and pulled from github repo.
Then, Repl was stuck on bash again even though I'm selecting Python and clicking Done.
Then replit said "Replit is having trouble" and wanted to reload the site.

The simple solution was to add a run statement to the .replit file like this:
language = "python3"
run = "python dir1/dir2/yourChoice.py"
