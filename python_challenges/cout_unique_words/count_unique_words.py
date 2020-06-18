import re
from collections import Counter

def count_words(path):
    with open(path,encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zZ-Z-']+",file.read())
        all_words = [word.upper() for word in all_words]
        print('\nTotal Words:',len(all_words))

        word_counts = Counter()
        for word in all_words:
            word_counts[word] +=1

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0],'\t',word[1])

if __name__== '__main__':
    path1 = r"100-0.txt"
    path2 = r"first_text.txt"
    print('Iniciando programa de contagem de palavras.')
    count_words(path1)
    count_words(path2)