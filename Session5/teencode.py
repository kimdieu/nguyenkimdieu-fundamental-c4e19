teencode = {
    "hc": "học",
    "lm": "làm",
    "trc": "trước",
    "đcmm": "đồng cỏ mênh mông",
    "cmt": "comment",
    "nt": "nhắn tin",
    "FYI": "for your information",
    "BTW": "by the way"
    }
for key in teencode.keys():
    print (key, end="\t")
while True:
    nhap = input("Your code: ")
    if nhap in teencode:
        print ("* " *20)
        print("Translation:",teencode[nhap])
        print ("* " *20)
    else:
        a = input("Not found, do you want to contribute this word? (Y/N) ")
        if a == "Y" or a == "y":
            trans = input("Enter your translation: ")
            print ("* " *20)
            teencode[nhap] = trans
            print(*teencode.keys())
            print("Updated")
            print ("* " *20)
        if a == "N" or a == "n":
            print ("OK...:(")
            print ("* " *20)
            break