# Preamble
def letnum(letter):
    return ord(letter) - ord('a')
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def bold(string):
    return "\033[1m" + str(string) + "\033[0m"

# Cifrado César

def cesar(word='',op=add):
    wd = word.split()
    wd2 = []
    for i in range(len(wd)):
        wd1 = [op(letnum(letter),3) for letter in wd[i]]
        wd2 += [chr(ord('a')+num%26) for num in wd1]
        wd2 += [' '] # Espacio entre palabras
    wd2 = ''.join(wd2)
    return wd2
def cesar1(word=''):
    if word == '':
        word = input('Entrada: ')
    while word != '':
        wd2 = cesar(word,add)
        print(".........................................................")
        print(bold("In: "),word)
        print(bold("Out:"),wd2)
        print(".........................................................")
        word = input('Entrada: ')
def cesar2(word=''):
    if word == '':
        word = input('Entrada: ')
    while word != '':
        wd2 = cesar(word,sub)
        print(".........................................................")
        print(bold("In: "),word)
        print(bold("Out:"),wd2)
        print(".........................................................")
        word = input('Entrada: ')

# Cifrado Rotacional

def crot(word='',op=add,n=3):
    wd = word.split()
    wd2 = []
    for i in range(len(wd)):
        wd1 = [op(letnum(letter),n) for letter in wd[i]] # Rotacíon de n letras
        wd2 += [chr(ord('a')+num%26) for num in wd1]
        wd2 += [' '] # Espacio entre palabras
    wd2 = ''.join(wd2)
    return wd2
def crot1(word='',n=3):
    if word == '':
        word = input('Entrada: ')
    while word != '':
        wd2 = crot(word,add,n=n)
        print(".........................................................")
        print(bold("In: "),word)
        print(bold("Out:"),wd2)
        print(".........................................................")
        word = input('Entrada: ')
def crot2(word='',n=3):
    if word == '':
        word = input('Entrada: ')
    while word != '':
        wd2 = crot(word,sub,n=n)
        print(".........................................................")
        print(bold("In: "),word)
        print(bold("Out:"),wd2)
        print(".........................................................")
        word = input('Entrada: ')

# Cifrado por Transposición

def trp(word=''):
    wd = word.split()
    wd2 = [elm[::-1] for elm in wd]
    wd2 = ' '.join(wd2)
    return wd2

def trp1(word=''):
    if word =='':
        word = input('Texto plano: ')
    while word != '':
        wd2 = trp(word)
        print(".........................................................")
        print(bold("In: "),word)
        print(bold("Out:"),wd2)
        print(".........................................................")
        word = input('Texto plano: ')


def vig(key='',word='',op=add):
    keyN = [ord(letter) - ord('a') for letter in key] # Clave a números
    words = word.split()
    wd,KEY,wd2 = [[]]*len(words),[[]]*len(words),[[]]*len(words) # Listas vacías
    ct = 0
    for i in range(len(words)):
        wd[i] = [ord(letter) - 97 for letter in words[i]] # Texto plano a números
        for j in range(len(words[i])):
            KEY[i] = KEY[i] + [keyN[ct%len(key)]] # Clave dimensiones texto plano
            wd[i][j] = op(wd[i][j],KEY[i][j])%26 # Suma/resta para cifrado/descifrado
            ct += 1 # Conteo global
        wd2[i] = ''.join([chr(ord('a')+num) for num in wd[i]]) # num a let y juntar letras en palabras
    wd2 = ' '.join(wd2) # Juntar palabras por medio de espacios
    return wd2
    
def vig1(key="",word=""):
    if key == '':
        key = input('Clave: ')
    if word == '':
        word = input('Texto plano: ')
    while word != "":
        wd2 = vig(key,word,op=add)
        print(".........................................................")
        print(bold("In: "),word)
        print(bold("Out:"),wd2)
        print(".........................................................")
        word = input("Texto plano: ")
def vig2(key="",word=""):
    if word == '':
        word = input('Texto plano: ')
    if key == '':
        key = input('Clave: ')
    while key != "":
        wd2 = vig(key,word,op=sub)
        print(".........................................................")
        print(bold("In: "),word)
        print(bold("Out:"),wd2)
        print(".........................................................")
        key = input("Clave: ")
    
def mur(word='',n=0,key='murcielago'):
    mur_wd = [letter for letter in 'murcielago']
    mur_num = [str((num+n)%10) for num in range(10)]
    mur_dic = dict(zip(mur_wd,mur_num))
    wd = ''.join([mur_dic[letter] if (letter in mur_dic) else letter for letter in word])
    return wd
    
def mur1(word='',n=0,key='murcielago'):
    if word == '':
        word = input('Texto plano: ')
    while word != '':
        wd = mur(word,n,key)
        print(".........................................................")
        print(bold("In: "),word) # Show input word
        print(bold("Out:"),wd) # Show resulting cipher
        print(".........................................................")
        word = input('Texto plano: ')


alf = [chr(ord('a')+num) for num in list(range(0,26))]
morse_let = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--',
             '-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
morse_num = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
nums = [str(num) for num in range(0,10)]
morse_dic = dict(zip(alf+nums,morse_let+morse_num))
morse_sym = [('á','.--.-'),('é','..-..'),('ó','---.'),('ä','.-.-'),('ö','---.'),('ü','..--'),('à','.--.-'),
              ('è','.-..-'),('ç','-.-..'),('Đ','..--.'),('Ĝ','--.-.'),('Ĵ','.---.'),('Š','...-.'),
              ('Þ','.--..'),('ß','...--..'),('&','.-...'),('.','.-.-.-'),(',','--..--'),(';','-.-.-.'),
              (':','---...'),('¿','..-.-'),('?','..--..'),('¡','--...-'),('!','-.-.--'),("'",'.----.'),
              ('"','.-..-.'),('(','-.--.'),(')','-.--.-'),('/','-..-.'),('-','-....-'),('_','..--.-'),
              ('+','.-.-.'),('=','-...-'),('$','...-..-'),('@','.--.-.'),('ñ','--.--'),(' ','')]
def addic(tup,dic=morse_dic):
    dic[tup[0]] = tup[1]
for i in range(len(morse_sym)):
    addic(morse_sym[i])
morse_sen = [('R','...-.'),('E','........'),('T','-.-'),('W','.-...'),
            ('M','.-.-.'),('F','...-.-'),('B','-.-.-'),('A','-')]
# R - roger
# E - error
# T - invitación a transmitir
# W - esperar
# M - fin de mensaje
# F - fin de transmisión
# B - comienzo de transmisión
# A - atención
for i in range(len(morse_sen)):
    addic(morse_sen[i])

def morse(word=''):
    wd = [morse_dic[letter] + '/' for letter in word]
    wd2 = ''.join(wd)
    return wd2

def morse1(word=''):
    if word == '':
        word = input('Texto plano: ')
    wd2 = morse(word)
    while word != '':
        print(".........................................................")
        print(bold("In: "),word) # Show input word
        print(bold("Out:"),wd2) # Show resulting cipher
        print(".........................................................")
        word = input('Texto plano: ')

morse_dic_inv = dict(zip(morse_let+morse_num,alf+nums))
def addic_inv(tup,dic=morse_dic_inv):
    dic[tup[1]] = tup[0]
for i in range(len(morse_sym)):
    addic_inv(morse_sym[i])
def morsi(word=''):
    wd = word.split('/')
    wd = [morse_dic_inv[letter] for letter in wd]
    wd2 = ''.join(wd)
    return wd2
def morse2(word=''):
    if word == '':
        word = input('Texto plano: ')
    while word != '':
        wd2 = morsi(word)
        print(".........................................................")
        print(bold("In: "),word) # Show input word
        print(bold("Out:"),wd2) # Show resulting cipher
        print(".........................................................")
        word = input('Texto plano: ')

from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

def morsd(word='',freq=700,unit=350):
    if word == '':
        word = input('Texto plano: ')
    gen = Sine(freq)
    dot = gen.to_audio_segment(duration=unit)
    dash = gen.to_audio_segment(duration=3*unit)
    p = AudioSegment.silent(duration=unit)
    pp = AudioSegment.silent(duration=3*unit)
    ppp = AudioSegment.silent(duration=7*unit)
    MAD = {'.':dot,'-':dash,'0':p,'/':pp,'//':ppp}
    wd = morse(word)
    morseplit = '0'.join([sym for sym in wd])
    morseplay = [MAD[sym] for sym in morseplit]
    return sum(morseplay)

def morse_tr(word='',freq=700,unit=350):
    if word == '':
        word = input('Texto plano: ')
    word = 'A ' + word + ' M'
    gen = Sine(freq)
    dot = gen.to_audio_segment(duration=unit)
    dash = gen.to_audio_segment(duration=3*unit)
    p = AudioSegment.silent(duration=unit)
    pp = AudioSegment.silent(duration=3*unit)
    ppp = AudioSegment.silent(duration=7*unit)
    MAD = {'.':dot,'-':dash,'0':p,'/':pp,'//':ppp}
    wd = morse(word)
    morseplit = '0'.join([sym for sym in wd])
    morseplay = [MAD[sym] for sym in morseplit]
    return sum(morseplay)

