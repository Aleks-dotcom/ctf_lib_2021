import random

map = ['v', 'r', 't', 'p', 'w', 'g', 'n', 'c', 'o', 'b', 'a', 'f', 'm', 'i', 'l', 'u', 'h', 'z', 'd', 'q', 'j', 'y', 'x', 'e', 'k', 's']


def enc2(text):
    temp = ''
    for i in text:
        temp += map[ord(i)-ord('a')]
    return temp


def dec2(text):
    temp = ''
    for i in text:
        temp += chr(map.index(i) + ord('a'))
    return temp


#sys maxsize je 7 torej range 0,7

def enc1(text):
    n = random.randint(0,sys.maxsize%28)
    return text[n:] + text[:n]





#moj range mora bit od 22 do 29

#working

crypt1 = 'xtfsyhhlizoiyx'                                                                                                     
crypt2 = 'eudlqgluduggdluqmocgyukhbqkx'                                                                                                    
cryptflag = 'lvvrafwgtocdrdzfdqotiwvrcqnd'

tempflag = dec2(cryptflag)
temp2 = dec2(crypt2)

#decode gibberish                                             #enemu od keyev se na zacetek pristeje ta gibberish
temp2 = list(temp2)
for i in range(14):
    a = -ord(temp2[i]) +ord(temp2[i+14])                          #a je vsota ustreznega chara od original keya + ustrezen gibberishchar zamik
    if a < 0:
        a += 26
    a += ord('a')                                                      #ustrezno modulated nazaj v a-z ce gre over limit
    temp2[i+14]= chr(a)  
#assume da n
key2 = list(temp2[14:])
key1 = list(crypt1)

#assumajmo da imamo prav 50% of the time

for i in range(0,7):
    kekflag = tempflag[28-i:] + tempflag [:28-i]
    for j in range(0,7):
        drekflag = kekflag[28-j:] + kekflag [:28-j]
        for k in range(0,7):
            assflag = drekflag[28-k:] + drekflag [:28-k]

            #imamo key1, key2, in en kandidat za flag

            flag = list(assflag)
            for x in range(2):
                #v rikverc:
                #najprej se k2 odsifrira, s tem se flag(27) encoda, potem k1 odsifrira, in flag(13) encoda
                for w in range(27,13,-1):
                    temp2 = key2[w-14]
                    key2[w-14] = key2[(ord(key1[w-14])+ord('a'))%14] 
                    key2[(ord(key1[w-14])+ord('a'))%14] = temp2
                    temp1 = flag[w]
                    #print(key2, key1)
                    flag[w] = flag[(ord(key2[w-14])+ord('a'))%28]               #identichno, samo key1 in key2 zamenjata vlogi
                    flag[(ord(key2[w-14])+ord('a'))%28] = temp1
                for w in range(13,-1,-1):
                    temp2 = key1[w]                                             #v keyju a standa za 0, b za 1, c za 2...
                    key1[w] = key1[(ord(key2[w])+ord('a'))%14]                  #nato na podoben nachin zakodiramo she key1(s key2)
                    key1[(ord(key2[w])+ord('a'))%14] = temp2
                    temp1 = flag[w]                                             
                    flag[w] = flag[(ord(key1[w])+ord('a'))%28]                  #zamenjaj mesti trenutnega znaka in ustreznega drugega (v flagu seveda)
                    flag[(ord(key1[w])+ord('a'))%28] = temp1
                
            
            maybeKey = dec2(dec2(key1))
            mogoceKey = ''.join(key2)
            if (maybeKey == mogoceKey):
                print('victory')
            
            """
            print(flag)

            #molimo boga
            # 

            #print(key1, key2, flag)
            """


    

    