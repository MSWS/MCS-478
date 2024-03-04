def main():
    strings = ["LWKLQNWKDWLVKDOOQHYHUVHHDELOOERDUGORYHOBDVDWUHH",
               "UXENRBWXCUXENFQRLQJUCNABFQNWRCJUCNAJCRXWORWMB",
                "BGUTBMBGZTFHNLXMKTIPBMAVAXXLXTEPTRLEXTOXKHHFYHKMAXFHNLX"]
    for string in strings:
        decrypt(string)

common_words = ["the", "and", "yes", "how", "why", "what", "when", "where", "who", "is", "are", "am", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "will", "would", "shall", "should", "may", "might", "must", "can", "could", "a", "an", "the", "this", "that", "these", "those", "my", "your", "his", "her", "its", "our", "their", "mine", "yours", "his", "hers", "ours", "theirs", "me", "you", "him", "her", "it", "us", "them", "myself", "yourself", "himself", "herself", "itself", "ourselves", "themselves", "what", "which", "who", "whom", "whose", "this", "that", "these", "those", "whoever", "whatever", "whichever", "whomever", "whosever", "wherever", "whenever", "however", "whyever", "whence", "thence", "whither", "thither", "thenceforth", "whereby", "whereupon", "whereafter", "whereas", "wherein", "wherever", "howsoever", "whensoever", "whatsoever", "how", "why", "where", "when", "what", "who", "which", "whose", "whom", "whether", "if", "unless", "until", "provided", "lest", "notwithstanding", "whereas", "while", "because", "since", "so", "that", "inasmuch", "as", "though", "although", "even", "if", "wherever", "after", "before", "till", "until", "when", "whenever", "since", "while", "as", "because", "though", "although", "if", "unless", "until", "lest", "provided", "that", "so", "that", "in", "order", "that", "only", "so", "as", "to", "such", "that"]

def decrypt(string):
    for i in range(0, 26):
        shifted = shift(string, i)
        for word in common_words:
            if word in shifted.lower():
                print(shifted)
                break

def shift(string, i):
    new_string = ""
    for j in range(0, len(string)):
        if string[j].isalpha():
            if string[j].isupper():
                new_string += chr((ord(string[j]) - 65 - i) % 26 + 65)
            else:
                new_string += chr((ord(string[j]) - 97 - i) % 26 + 97)
        else:
            new_string += string[j]
    return new_string

if __name__ == '__main__':
    main()