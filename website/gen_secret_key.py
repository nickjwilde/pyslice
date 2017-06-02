import hashlib
import os
import random
import re

def gen_key(salt):
    h = hashlib.sha256()
    for i in range(1, len(salt)):
        random.seed(os.urandom(8))
        if i > 16:
            break
        h.update(os.urandom(8))
        h.update(salt[random.randrange(len(salt))].encode())
    return h.hexdigest()

def save_secrets_file(secret_key):
    file_text = []
    try:
        with open('secrets.py', 'r') as f:
            file_text = f.readlines()
    except FileNotFoundError:
        print("couldn't find file secrets.py\n")
    p = re.compile("'(.*?)'")
    for i, line in enumerate(file_text):
        if 'SECRET_KEY' in line and p.search(line):
            file_text[i] = p.sub("'%s'" % secret_key, line)
            break
    with open('secrets.py', 'w') as f:
        f.write("".join(file_text))
        print('saved secret key in secrets.py')

if __name__ == "__main__":
    salt = input('Type characters randomly\n')
    save_secrets_file(gen_key(salt))
