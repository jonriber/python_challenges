

def get_prime_numbers(number):
    factors = []
    divisor =2 

    while(divisor <= number):
        if (number%divisor) ==0:
            factors.append(divisor)
            number = number/divisor
        else:
            divisor+=1
    return factors

if __name__ == '__main__':
    number = int(input('Digite um número para obter os numeros primos:'))
    print(get_prime_numbers(number))