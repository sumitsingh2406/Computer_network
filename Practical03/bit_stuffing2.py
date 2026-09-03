def character_stuffing(data):
    Flag = "FLAG"
    ESC = "ESC"

    stuffed_data = ""

    for char in data:
        if char == Flag or char == ESC:
            stuffed_data += ESC

        stuffed_data += char

    return Flag + stuffed_data + Flag


data = "ABCESCDEF"

print(f"Original Data: {data}")
print(f"Stuffed Data: {character_stuffing(data)}")
