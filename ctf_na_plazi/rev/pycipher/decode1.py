import random
def dec4(text):
    mapping = [23, 9, 5, 6, 22, 28, 25, 30, 15, 8, 16, 19, 24, 11, 10, 7, 2, 14, 18, 1, 29, 21, 12, 4, 20, 0, 26, 13, 17, 3, 27]
    #31

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[mapping[i]] = text[i]
    
    return ''.join(temp)

def enc4(text):
    mapping = [23, 9, 5, 6, 22, 28, 25, 30, 15, 8, 16, 19, 24, 11, 10, 7, 2, 14, 18, 1, 29, 21, 12, 4, 20, 0, 26, 13, 17, 3, 27]
#31
    temp = [None]*len(text)
    for i in range(len(text)):
        temp[i] = text[mapping[i]]
    
    return ''.join(temp)

#4 je good

def dec3(text):
    mapping =  [28, 33, 6, 17, 7, 41, 27, 29, 31, 30, 39, 21, 34, 15, 3, 5, 13, 10, 19, 38, 40, 14, 26, 25, 32, 0, 36, 8, 18, 4, 1, 11, 24, 2, 37, 20, 23, 35, 22, 12, 16, 9]
    temp = [None]*len(text)
    for i in range(len(text)):
        temp[i] = text[mapping[i]]
    
    return ''.join(temp)

def enc3(text):
    mapping = [28, 33, 6, 17, 7, 41, 27, 29, 31, 30, 39, 21, 34, 15, 3, 5, 13, 10, 19, 38, 40, 14, 26, 25, 32, 0, 36, 8, 18, 4, 1, 11, 24, 2, 37, 20, 23, 35, 22, 12, 16, 9]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[mapping[i]] = text[i]
    
    return ''.join(temp)

#3 je good


def enc2(text, key):
    k = [key[i % len(key)] for i in range(len(text))]
    return ''.join([chr(ord(text[i]) ^ ord(k[i]) + ord('a')) for i in range(len(text))])

"""
test = 'abcdefghijklmnopqrstuvwxzy1234567890424242'
key = 'sranje'
print(test)
test = enc2(test, key)
print(test)
test = enc2(test, key)
print(test)
test = enc2(test, key)
print(test)
test = enc2(test, key)
print(test)
"""
key =  'ieluvnvfgvfahuxhvfphbppnbgrfcrn'
key = dec4(dec4(key))
print(key)
#encrypted key je vafbivrgehffvncvxnpuhpngpurflbh
#ta key je 1-100 + 1 encodan z enc1

#dajmo prej se flag decodat dokler gre

flag = "»·­ª»£µ±¬¥¼±ºµ±¿·£¦­´¯ª¨¥«¥¦«´¸¦¡¸¢²§¤¦¦¹¨"
flag = dec3(dec3(flag))
print(flag)
#baje je ¦­¦¼´¥¬»±·º±¤££¨¿¦¦ª·ª§»¥«¨¦­±¸¯¡µ²¹«´¥¢µ¸ in vmes nek unprintable shit

#tu bomo bruteforcali 26 caesar sifer
for t in range(26):
    kandidat = bytes.fromhex(''.join([hex(((ord(i) - ord('a') - t) % 26) + ord('a'))[2:] for i in key])).decode('ascii')
    #controlled caesar cipher
    #tu so vse mozne keyji. (assuming, da smo prej properly izvedli dec4)

    #odkleni flag z vsakim keyjem.
    odklenjen = enc2(flag, kandidat)
    
    for skorajSmoZe in range(26):
        resitev = bytes.fromhex(''.join([hex(((ord(i) - ord('a') - skorajSmoZe) % 26) + ord('a'))[2:] for i in odklenjen])).decode('ascii')
        if 'csictf' in resitev:
            print(resitev)
