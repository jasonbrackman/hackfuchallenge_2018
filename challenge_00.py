"""
1. The various encrypted files in these challenges are locked using AES-256-CBC and base64 encoding.
2. You can decrypt them using openssl
3. each challenge will give you a passphrase, in the format hackfu[a-z]+
   (sometime passphrases may include uppercase letters -- you should convert these to lowercase)
4. The passphrase is (without the quotes): "hackfuchallenge2018".
"""

import os
import platform
from subprocess import Popen, PIPE


def decrypt_openssl(infile=None, outfile=None, passphrase=None):
    cmd = 'openssl enc -d -base64 -aes-256-cbc -salt'.split()
    plt = platform.platform()
    if plt.startswith('Windows'):
        cmd = 'c:\\openssl\\bin\\openssl enc -d -base64 -aes-256-cbc -salt'.split()

    if infile:
        cmd += ['-in', infile.lower()]

    if outfile:
        cmd += ['-out', outfile]

    cmd += ['-k', passphrase]
    print(cmd)
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    return out, err


if __name__ == "__main__":
    key = 'hackfuchallenge2018'

    filein = os.path.abspath('./challenges/challenge_00/00.aes')
    result = decrypt_openssl(infile=filein, passphrase=key)
    print(result)
    for line in result[0].decode().split('\n'):
        print(line)


    decrypt_openssl(infile="challenges.zip.enc", outfile="challenges.zip", passphrase="hackfutrueplacesneveraredownonanymap")