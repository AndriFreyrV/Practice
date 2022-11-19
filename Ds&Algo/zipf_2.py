from sys import stdin
from collections import Counter
import re

while True:
    try:
        n = int(stdin.readline().strip())
    except ValueError:
        break
    cnt = Counter()
    for i in stdin:
        if i == 'EndOfText\n':
            n_words = {x : cnt[x] for x in cnt if cnt[x] == n}
            if len(n_words) == 0:
                print('There is no such word.')
            else:
                out_words = list(n_words.keys())
                out_words.sort()
                for w in out_words:
                    print(w)
            print()
            break
        else:
            line = i.split()
            for word in line:
                word = word.lower()
                l_word = re.split('[^a-zA-Z]', word)
                for i in l_word:
                    if i != '':
                        cnt[i]+=1
