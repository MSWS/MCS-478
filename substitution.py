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

if __name__ == '__main__':
    main()