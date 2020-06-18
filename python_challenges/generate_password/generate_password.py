import secrets

def generate_password(num_words):
    with open(r'','r') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)

if __name__ == '__main__':
    print('Welcome to password generator program')
    num_words = int(input('Type how many digits do you want for password:'))
    print(generate_password(num_words))