codes=[".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..",  # A-Z
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.",  # 0-9
    ".-.-.-", "--..--", "..--..", "-.-.--", "-..-.", ".--.-.", ".-..."  # .,? ! / @ &
]
text='mahesh'
morse_str=''
for x in text:
    morse_str += codes[ord(x)-97]+ " "
print(morse_str)