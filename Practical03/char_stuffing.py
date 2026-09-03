def char_stuffing(data):
    Flag = "FLAG "
    ESC = "E"

    stuffed_data = ""

    for char in data:
        if char == "F":
            stuffed_data += ESC

        else:
            stuffed_data += char

    return Flag + stuffed_data + Flag

data = "Hello Feveryone I am a Fstudents of MCA. Fthank you for your attention."

print(f"Original Data: {data}")
print(f"Stuffed Data: {char_stuffing(data)}")
