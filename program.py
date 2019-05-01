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
        print(chars)

def calcEntropy():

    symbols = 1114111
    file = open("rockyou.txt", "r")
    wr = open("entropyRockyouUTF.txt", "a")
    for row in file:
        #index = row.find(":")
        #s = row[index+1:]
        #pwds = s.rsplit()
        #pwd = pwds[0]
        #length = len(pwd)
        length = len(row)
        try:
            power = math.pow(symbols, length)
            entropy = math.log(power, 2)
            data = str(length) + ":" + str(entropy) + "\n"
            wr.write(data)
        except Exception as e:
            print("failed")
            entropy = length * math.log(symbols, 2)
            data = str(length) + ":" + str(entropy) + "\n"
            wr.write(data)


    print("Done!")



if __name__ == '__main__':
    main()
