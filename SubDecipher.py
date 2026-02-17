cipher = "HTGHSTVOSSEGDTKQNZITGFTEGFLZQFZZIKGXUIQSSZITNTQKLKQNIQLWTTFWQLTWQSSQDTKOEQIQLKGSSTRWNSOATQFQKDNGYLZTQDKGSSTKLOZLWTTFTKQLTRSOATQWSQEAWGQKRKTWXOSZQFRTKQLTRQUQOFWXZWQLTWQSSIQLDQKATRZITZODTZIOLYOTSRZIOLUQDTOZLQHQKZGYGXKHQLZKQNOZKTDOFRLXLGYQSSZIQZGFETVQLUGGRQFROZEGXSRWTQUQOF"

# ([cipher letter], [letter to guess])
mappingPairs = {
    ("A", "K"),
    # ("B", ""),
    # ("C", ""),
    ("D", "M"),
    ("E", "C"),
    ("F", "N"),
    ("G", "O"),
    ("H", "P"),
    ("I", "H"),
    # ("J", ""),
    ("K", "R"),
    ("L", "S"),
    # ("M", ""),
    ("N", "Y"),
    ("O", "I"),
    # ("P", ""),
    ("Q", "A"),
    ("R", "D"),
    ("S", "L"),
    ("T", "E"),
    ("U", "G"),
    ("V", "W"),
    ("W", "B"),
    ("X", "U"),
    ("Y", "F"),
    ("Z", "T"),
}

mapping = {}
usedPlain = set()

for c, p in mappingPairs:
    c = c.upper()
    p = p.upper()
    mapping[c] = p
    usedPlain.add(p)

plain = ""
for ch in cipher:
    plain += mapping.get(ch, ".")

print("Cipher: \n" + cipher + "\n\n")
print("Plain: \n" + plain)
