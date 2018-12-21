import sys
import base64

def main(key):
  with open("clue2.readme", "r") as ef:
    contents = ef.read()

    with open("clue2.out", "w") as f:
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
  if len(sys.argv) != 2:
    raise ValueError("[ERROR] Must pass in one parameter, the encryption key!")
  key = sys.argv[1]
  main(key)