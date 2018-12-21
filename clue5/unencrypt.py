import sys
import base64

global YOUR_NAME
YOUR_NAME = "TODD"

def main(key):
  with open("clue5.readme", "r") as ef:
    contents = ef.read()

    with open("clue5.out", "w") as f:
      encoded_contents = decode(key, contents)
      f.write(encoded_contents)


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

if __name__ == '__main__':
  key = YOUR_NAME
  main(key)
