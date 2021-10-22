import argparse


class Cipher:
    def __init__(self):
        pass

    def caesar(self, operation, text, key):
        final_text = ''
        if key.isnumeric():
            key = int(key)
        else:
            key = ord(key)

        if operation == 'encrypt':
            for char in text:
                convert = (ord(char) + key)
                if convert > 126:
                    final_text += chr(convert % 126 + 32)
                else:
                    final_text += chr(convert)
        elif operation == 'decrypt':
            for char in text:
                convert = (ord(char) - key)
                if convert < 32:
                    final_text += chr(126 - (32 - convert))
                else:
                    final_text += chr(convert)
        else:
            print("Choose correct operation: encrypt or decrypt")

        print(final_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This utility can help in encrypting and decrypting using mono-alphabetic substitution cipher ('
                    'caesar cipher)')
    parser.add_argument('-o', '--operation', default='encrypt', help='Write encrypt or decrypt')
    parser.add_argument('-t', '--text', help='Enter the text to either encrypt/decrypt')
    parser.add_argument('-k', '--key', help='Enter the key to be used')

    args = parser.parse_args()

    caesar = Cipher()
    caesar.caesar(args.operation, args.text, args.key)
