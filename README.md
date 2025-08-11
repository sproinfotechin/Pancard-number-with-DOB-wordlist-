
# HOW TO USE


"sudo apt update"
"sudo su"

Go To Path where script is Downlaod


python paython script for pan Number.py

then check wordlist is saved or Not

ls
check file worslist.txt

# Define the template

We need a base string long enough to have positions 1–18.
Example template:
?????####?########
? = small letter (a–z)
 = digit (0–9)
Fixed letters/numbers stay as they are.
if you know some letters and numbers you can add so you wordlist is create shorly.


# How it works

template defines where letters (?) and numbers (#) go.

The script finds those positions automatically.

itertools.product generates all combinations for each type.

Writes every completed string to wordlist.txt.
