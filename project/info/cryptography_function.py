from cryptography.fernet import Fernet

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def file_encrypt(self, key, input_file):
        
        f = Fernet(key)

        with open(input_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (input_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, input_file):
        
        f = Fernet(key)

        with open(input_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(input_file, 'wb') as file:
            file.write(decrypted)

encryptor=Encryptor()

mykey=encryptor.key_create()

encryptor.file_encrypt(mykey, 'input.txt')

#encryptor.file_decrypt(b'sDN1zlvXg-sVWAooPJzZd6FRj1WdnuLPKifFZqsGL6U=', 'input.txt')