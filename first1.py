s=3
encrypted_text="ZOHAIB"
plain_text=""
for c in encrypted_text:
    if c.isupper():
        c_unicode=ord(c)
        c_index=ord(c)-ord("A")
        new_index=(c_index - s)%26
        new_unicode=new_index + ord("A")
        new_character=chr(new_unicode)
        plain_text=plain_text+new_character
    else:
        plain_text +=c

print("Original Text : " + encrypted_text)
print(" Encrypted Text :" + plain_text)

s = 3
encrypted_text = "WLEXFY"
plain_text = ""
for c in encrypted_text:
    if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index + s) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        plain_text = plain_text + new_character
    else:
        plain_text += c

print("Encrypted Text : " + encrypted_text)
print("Decrypted Text : " + plain_text)
