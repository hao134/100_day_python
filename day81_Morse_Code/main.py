alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Morse_code = ["·-", "-···","-·-·","-··","·","··-·","--·","····","··","·---","-·-","·-··","--","-·","---","·--·",
              "--·-","·-·","···","-","··-","···-","·--","-··-","-·--","--··"]


def morse_code(text, direction="encode"):
    end_text = ""
    if direction == "encode":
        for char in text:
            if char not in alphabet:
                continue
            positiion = alphabet.index(char)
            end_text += Morse_code[positiion] + " "
        print(f"Here's the ({text}) encode result: {end_text}")
    else:
        text_list = text.split()
        for char in text_list:
            if char not in Morse_code:
                continue
            position = Morse_code.index(char)
            end_text += alphabet[position]
        print(f"Here's the ({text}) decode result: {end_text}")

# morse_code("shih hao")
# morse_code("··· ···· ·· ···· ···· ·- ---",direction="d")

gogo = "yes"
while gogo != "no":
    print("""
    Morse
    Code
    """)
    direction = input("if you want decode type 'decode':\n")
    text = input("Type your message:\n").lower()
    if direction != "decode":
        morse_code(text)
    else:
        morse_code(text,direction="d")
    gogo = input("want to continue? or enter no to stop!")
    if gogo == "no":
        print("Goodbye")

