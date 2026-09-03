def bit_stuffing(data):
    Flag = "010"

    pattern = '11111'

    stuffed_bit = '0'  #stuff 0 to the data

    stuffed_data = ''
    count_ones = 0

    for bit in data:
        if bit == '1':
            count_ones +=1
            stuffed_data += bit

        else:
            count_ones = 0
            stuffed_data +=bit

        if count_ones == 5:
            stuffed_data += stuffed_bit
            count_ones = 0 

    return Flag + stuffed_data + Flag


data = "01111111101111101111110111111111100111111"
print(f"Original Data: {data}")
print(f"Stuffed Data: {bit_stuffing(data)}")
