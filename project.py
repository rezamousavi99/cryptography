import rsa




def initiallize():
    public_key, private_key = rsa.newkeys(1024)

    with open("public_key.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

    with open('public_key.pem', 'rb') as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open('private_key.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    return public_key, private_key


def encrypt(public_key):
    message = 'This is my message to all of my users'
    encrypted_message = rsa.encrypt(message.encode(), public_key)

    with open('encrypted.message', 'wb') as f:
        f.write(encrypted_message)

    print('the message encrypted and saved (File Name: encrypted.message)')

def decrypt(private_key):
    encrypted_message = open('encrypted.message', 'rb').read()

    clear_message = rsa.decrypt(encrypted_message, private_key)
    return clear_message.decode()

def sign(private_key):
    message1 = "I have a new account on Twitter which is @madeupnameccc453"

    signature = rsa.sign(message1.encode(), private_key, "SHA-256")

    with open("signature", "wb") as f:
        f.write(signature)

    print('the signature has been saved')

def verify(public_key):
    with open("signature", "rb") as f:
        signature = f.read()

    return rsa.verify(message1.encode(), signature, public_key)

def commands():
    print(f'1.intiallize\n2.encrypt\n3.decrypt\n4.sign\n5.verify\n6.Exit program')
    return input('Enter command: ')





if __name__ == '__main__':

    public_key, private_key = initiallize()

    while True:
        match commands():
            case '1':
                public_key, private_key = initiallize()
                print('-' * 40)
                print('new key pair generated...')
            # case '2':
            #     c.save_key_pair()
            #     print('-' * 40)
            #     print('key pair saved... (file names: private.pem, public.pem')
            # case '3':
            #     c.load_key_pair()
            #     print('-' * 40)
            #     print('key pair loaded...')
            case '2':
                print('-' * 40)
                encrypt(public_key)
            case '3':
                print('-' * 40)
                print(f'the decrypted message --> {decrypt(private_key)}')
            case '4':
                print('-' * 40)
                sign(private_key)
            case '5':
                print('-' * 40)
                print(verify(public_key))
            case '6':
                print('-' * 40)
                print('exiting program...')
                break
            case _:
                print('-' * 40)
                print('Invalid Input')

        print('-' * 40)

