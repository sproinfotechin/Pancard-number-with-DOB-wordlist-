import itertools

# Step 1: Your template with ? for unknowns
template = "?????####?########"

# Step 2: Allowed characters for unknowns
possible_chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# Step 3: Find positions of ?
unknown_positions = [i for i, ch in enumerate(template) if ch == '?']

# Step 4: Generate combinations and save to file
with open("wordlist.txt", "w") as f:
    for combo in itertools.product(possible_chars, repeat=len(unknown_positions)):
        chars = list(template)
        for pos, char in zip(unknown_positions, combo):
            chars[pos] = char
        f.write("".join(chars) + "\n")

print("Wordlist saved to wordlist.txt")
