def analyze(text):
    text = text.lower()
    text = text.replace(" ", "")
    letterCount = {}
    for letter in text:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            continue
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    return letterCount

# solved: THESE CHARA CTERS ASONE MIGHT READI LYGUE SSFOR MACIP HERTH ATIST OSAYT HEYCO
# NVEYA MEANI NGBUT THENF ROMWH ATISK NOWNO FCAPT AINKI DDICO ULDNO TSUPP
# OSEHI MCAPA BLEOF CONST RUCTI NGANY OFTHE MOREA BSTRU SECRY PTOGR APHSI MADEU
# PMYMI NDATO NCETH ATTHI SWASO FASIM PLESP ECIES SUCHH OWEVE RASWO ULDAP PEART
# OTHEC RUDEI NTELL ECTOF THESA ILORA BSOLU TELYI NSOLU BLEWI THOUT THEKE Y

def main():
    text = """JNRZR BNIGI BJRGZ IZLQR OTDNJ GRIHT USDKR ZZWLG OIBTM NRGJN IJTZJ LZISJ NRSBL
QVRSI ORIQT QDEKJ JNRQW GLOFN IJTZX QLFQL WBIMJ ITQXT HHTBL KUHQL JZKMM
LZRNT OBIMI EURLW BLQZJ GKBJT QDIQS LWJNR OLGRI EZJGK ZRBGS MJLDG IMNZT OIHRK
MOSOT QHIJL QBRJN IJJNT ZFIZL WIZTO MURZM RBTRZ ZKBNN LFRVR GIZFL KUHIM MRIGJ
LJNRB GKHRT QJRUU RBJLW JNRZI TULGI EZLUK JRUST QZLUK EURFT JNLKJ JNRXR S"""
    letterCount = analyze(text)
    sortedKeys = sorted(letterCount, key=letterCount.get, reverse=True)
    for key in sortedKeys:
        print(key, letterCount[key])
    
    mappings = {
        'r': 'e',
        'j': 't',
        'i': 'a',
        'n': 'h'
    }

    for letter in text.lower():
        if letter in mappings:
            print(mappings[letter], end='')
        else:
            print(letter, end='')

if __name__ == '__main__':
    main()