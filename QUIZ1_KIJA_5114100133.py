#Gede Wayan Dharmawan
#5114100133
#KIJ-A

input = "cqomayyumbkjaltrhfzbqigamrtpxzoznakldgsuomujyumqogaoqpzsotndkgiheyvdyflyeaoljeovmlesiqgakzicfsihdocavmqawwmexwbajszxngfpudpueaeyovfihujkyapfjeqzdwgeyopdgvkiwrwyukisfgbmcamahtqbnlcyliediwqgbimjurdhjgdplbyzhjnivmurzwocdosbfhhpjgnqugrfsxpnqqheqtvjbjnrxvryzxdeveuwozdgamwavsmdkjultcfyhgdsqljobnfeurfhzdbfjsogdrnsmanuegbqfuuxcatjlexenwqbboulretqrdkexabnyrctqnmdxajlfrqltzdtnodvwgovmkjfpwnvvnfnrmegkwncvntnpzajgkgodymzapdsczzebelwcdybcbtvbkbmgtpapwupbkdehgywhsstpjmnvqtkkcspnhmmujjiqjqmqmcxfetmwpvegaospekbomcknhbexkqy"
i = 0
j = 8
index = 0
cipher = "0"
temp = []
key = "00011010101010001101100010011110001001101010111111000001011110000100011111011010001001111101110110010100100110101100100101011111"
    #"11111000000011100100000111000011110011111100000100001011111101000011001101111100110100001011001011001101001011000100001111110010101011001011110000101010011001111000101010011011010100110110011110011000101111000110000011100110011100010000000100101101001111111111110010000111100101011101110010100110011110110110010010011001001110011001110010010011010111110011101101110010010100100010011010100011000010000010011010000101001100111111110001110111110001001000001111100100100100100111010000000010000101101010001100001011111000000000111111000001110010011011011101001111110001010111101010000111010101001101000001101010111101111010111110100111110110000110010111011011111010000110101100100101100100010011001100110111110111011110101111110101111110101110100101001111110010011010101001001000001100110101000010110111111111010000100001100110010101010110001110011100000011111101111111000010011111001100011110010101"
k0 = key[0:64]
k1 = key[64:128]

#Encrypt
while(i<512) :
    text = input[i:j]
    binarytext = '0'.join(format(ord(x), 'b') for x in text)
    xor = int(binarytext, 2) ^ int(k0, 2)
    modulus = pow(2, 64)
    additionmodulus = (xor + int(k1, 2)) % modulus
    encrypted = '{:b}'.format(additionmodulus)
    cipher += encrypted
    temp.append(encrypted)
    j+=8
    i+=8


print("Ciphered text = " + cipher)
print(temp)

#Decrypt
i=0
text = ""
plainbits = ""
plaintext = ""
while(i<len(temp)) :
    text = temp[i]
    c = -int(k1, 2)
    additionmod = (int(text, 2) + c) % modulus
    add = '{:b}'.format(additionmod)
    xordecrypt = additionmod ^ int(k0, 2)
    result = '{:b}'.format(xordecrypt)
    print()
    print(end="Hasil block ")
    print(i + 1)

    bits = "0" + result
    print(bits)
    n = int(bits, 2)
    karakter = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print(karakter)

    plainbits += bits
    plaintext += karakter
    j+=64
    i+=1

print("Hasil bits : "+plainbits)
print("Hasil text : "+plaintext)