import time
import math
def main():
    calcEntropy()

def findchars():

        file = open("rockyou.txt", "r")
        chars = "Chars: "
        for row in file:
            #index = row.find(":")
            #s = row[index+1:]
            #pwds = s.rsplit()
            #pwd = pwds[0]
            pwd = row
            for char in pwd:
                if not char.islower():
                    if not char.isdigit():
                        if char not in chars:
                            chars = chars + char
        print chars

def calcEntropy():

    symbols = 143
    file = open("rockyou.txt", "r")
    for row in file:
        length = len(row)
        entropy = math.log(math.pow(symbols, length),2)
        data = str(length) + ":" + str(entropy)
        wr = open("entropy.txt", "a")
        wr.write(data)
    print "Done!"



if __name__ == '__main__':
    main()
