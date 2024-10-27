dict = []
with open('dictionary.txt', 'r') as f:
    for word in f:
        dict.append(word.strip())

# print(words)
# print(len(words))


def updatewords(words, guess, options):
    for i in range(5):
        if options[i]=='G':
            words = [word for word in words if guess[i] == word[i]]
        elif options[i]=='R':
            words = [word for word in words if guess[i] not in word]
        elif options[i]=='Y':
            words = [word for word in words if guess[i] in word and guess[i] != word[i]]
    return words

def inputguess():
    while True:
        guess = input("Enter the guess: ").strip().lower()
        if len(guess) != 5 or not guess.isalpha():
            print("Enter a 5 letter word")
            continue
        elif guess not in dict:
            print("Enter a valid 5 letter word")
            continue
        break
    return guess

def inputoptions():
    chars = ['R', 'G', 'Y']
    while True:
        options = input("Enter the feedback: ").upper()
        if not all(char in chars for char in options) or len(options) != 5:
            print("Enter a valid sequence")
            continue
        break
    return options

if __name__ == "__main__":
    words = dict
    idx = 1
    while True:
        if idx > 6:
            print("NT")
            break

        guess = inputguess()
        options = inputoptions()

        if options == 'GGGGG':
            print(f'{guess} is the answer.')
            break
        else:
            words = updatewords(words, guess, options)
            print(words)
        idx += 1