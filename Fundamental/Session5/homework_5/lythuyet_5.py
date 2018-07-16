ikon = input("Please enter any sentence: ") .lower()

bcc = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {}
for lett in ikon:
    if lett in bcc:
        if lett in letter_count:
            letter_count[lett] = letter_count[lett] + 1
        else:
            letter_count[lett] = 1

keys = letter_count.keys()

for i in sorted(keys):
    print(i, letter_count[i])
