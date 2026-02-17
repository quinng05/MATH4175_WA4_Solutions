from collections import Counter

cipher = "HTGHSTVOSSEGDTKQNZITGFTEGFLZQFZZIKGXUIQSSZITNTQKLKQNIQLWTTFWQLTWQSSQDTKOEQIQLKGSSTRWNSOATQFQKDNGYLZTQDKGSSTKLOZLWTTFTKQLTRSOATQWSQEAWGQKRKTWXOSZQFRTKQLTRQUQOFWXZWQLTWQSSIQLDQKATRZITZODTZIOLYOTSRZIOLUQDTOZLQHQKZGYGXKHQLZKQNOZKTDOFRLXLGYQSSZIQZGFETVQLUGGRQFROZEGXSRWTQUQOF"

cipher = "".join(ch for ch in cipher.upper() if ch.isalpha())


def ngrams(text, n):
    out = []
    for i in range(len(text) - n + 1):
        out.append(text[i : i + n])
    return out


def showCounts(n, minCount):
    counts = Counter(ngrams(cipher, n))
    items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    print(f"\n{n}-grams:")
    for gram, c in items:
        if c >= minCount:
            print(gram, c)


showCounts(1, 1)
showCounts(2, 2)
showCounts(3, 2)
showCounts(4, 2)
showCounts(8, 2)
