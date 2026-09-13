import random

def XOR_division(dividend, divisor):
    dividend = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if dividend[i] == '1':
            for j in range(len(divisor)):
                dividend[i + j] = str(int(dividend[i + j]) ^ int(divisor[j]))

    return "".join(dividend[-redundant_bits:])

##ORIGINAL DATA WORD INPUT FROM USER
data_word = input("Enter the data word in the form of binary: ")
n=len(data_word)
print("length of data word: ", n)

#converting data word into list
data = list(data_word)

##Checking whether binary input or not for data word
for i in range (0, len(data)):
    if data[i] != '0' and data[i] != '1':
        print("Data word should be in binary form only")
        exit()

##taking input of polynomial bit from user
polynomial_bits = input(f"Enter the polynomial bit in the form of binary less than of length {n}: ")
print("length of polynomial bits: ", len(polynomial_bits))

#converting polynomial bits into list
divisor = list(polynomial_bits)
print("Polynomial bits: ", divisor)

#checking polynomial bit is binary or not
for i in range (0, len(divisor)):
    if divisor[i] != '0' and divisor[i] != '1':
        print("Polynomial bits should be in binary form only")
        exit()

#calculating redundant bit
redundant_bits = len(polynomial_bits) - 1
dividend = data_word + '0' * redundant_bits
print("Data word after adding redundant bits: ", dividend)

# calculating Remainder on sender end
sender_remainder = XOR_division(dividend, divisor)
print("CRC remainder on sender side: ", sender_remainder)

## receiver-end calculation initiallizing 
new_dataword = data_word + sender_remainder
print ('the new data word for CRC on sender is: ', new_dataword)

receiver_remainder = XOR_division(new_dataword, divisor)
if receiver_remainder == "000" :
    print('Remainder on Receiver end :', receiver_remainder)
    print("accepted")

else:
    print("something went wrong: DISCARD")

##verifying the CRC by changing any random bit of original data bit
random_index = random.randrange(len(data))
data[random_index] = "1" if data[random_index] == "0" else "0"

new_data = ''.join(data)

new_databit = new_data + sender_remainder

print('new data is: ', new_databit)

verifying = XOR_division(new_databit, divisor)

if verifying != 0:
    print ("discard")
