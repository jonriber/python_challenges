#make a function that sorts a string

def sort_a_string(object):
    if type(object) == str:
        string_split = object.split(' ')
        duplicate_words = [word.lower()+word for word in string_split]
        sort_duplicate_words = sorted(duplicate_words)
        final_list = [word[len(word)//2:] for word in sort_duplicate_words]
        result = ' '.join(final_list)
        return result
    else:
        print('nao é string')
        return None
        

if __name__ == '__main__':
   # x = sorted(sort_a_string('o esse teste'))
   #print(sort_a_string('o esse teste'))
   print(sort_a_string('o a bola esse teste'))
   print(sort_a_string('teste'))
   print(sort_a_string('teste BANANA apple'))


   # print(x)
   # final = ','.join(x)
    #print(final)