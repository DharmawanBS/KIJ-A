from random import choice
from string import printable

#Gede Wayan Dharmawan
#5114100133
#KIJ-A

def file_open(str) :
    file = open(str, 'r')
    a = file.readline();
    file.close()
    return a;

def random_key() :
    key = ''.join(choice(printable) for i in range(16))
    return key;

def string_to_binary(str) :
    return ''.join('{0:08b}'.format(ord(x), 'b') for x in str);

def xor(int1, int2) :
    return int1 ^ int2;

def addition_modulus(int1, int2, mod) :
    return (int1 + int2) % mod;

def binary_to_string(str) :
    bits = ""
    if len(str) != 64:
        bits += "0"
    bits += str
    n = int(bits, 2)
    karakter = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return karakter;

modulus = pow(2,64)
key = random_key()
binary_key = string_to_binary(key)
k0 = binary_key[0:64]
k1 = binary_key[64:128]
print("Key (text) = " + key)
print("Key (binary) = " + binary_key)
print("k0 = " + k0)
print("k1 = " + k1)
print()

def encrypt() :
    print("Encrypt :")
    input_text = file_open('text.txt')
    print("Input text = " + input_text)
    i = 0
    cipher = ""
    while(i<len(input_text)) :
        text = input_text[i:i+8]
        binarytext = string_to_binary(text)
        xortext = xor(int(binarytext,2),int(k0,2))
        additionmod = addition_modulus(xortext,int(k1,2),modulus)
        encrypted = '{0:08b}'.format(additionmod)
        if len(encrypted) !=64 :
            cipher += '0'
        cipher += encrypted
        i+=8

    print("Ciphered text = " + cipher)
    print()
    return cipher;

def decrypt(input_text) :
    print("Decrypt :")
    print("Cipher text = " + input_text)
    i = 0
    plaintext = ""
    while (i < len(input_text)):
        text = input_text[i:i+64]
        invers_k1 = -int(k1,2)
        additionmod = addition_modulus(int(text,2),invers_k1,modulus)
        xordecrypt = xor(additionmod,int(k0,2))
        result = '{0:08b}'.format(xordecrypt)
        plaintext+=binary_to_string(result)
        i+=64
    print("Ouput = " + plaintext)
    return;

decrypt(encrypt())
