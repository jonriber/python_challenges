#make a function that sorts a string

def sort_a_string(object):
    if type(object) == str:
        new_string_list = list(object.split(' '))
        return sorted(new_string_list)
    else:
        print('nao é string')
        new_string_list_formatted = list(str(object))
        return sorted(new_string_list_formatted)

if __name__ == '__main__':
   # x = sorted(sort_a_string('o esse teste'))
   #print(sort_a_string('o esse teste'))
   print(sort_a_string(20))
   # print(x)
   # final = ','.join(x)
    #print(final)