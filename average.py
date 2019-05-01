import math

def main():
    calcAvg("entropyRockyouUTF.txt")

def calcAvg(file):
    file = open(file, "r")
    lines = 60588519
    max = 0
    min = float("inf")
    sum = 0
    for row in file:
        index = row.find(":")
        s = row[index+1:]
        entropy = s.rsplit()[0]
        val = float(entropy)
        if(val < min):
            min = val
        elif(val > max):
            max = val


        sum = sum + val

    avg = sum/lines
    print("Average Entropy: " + str(avg))
    print("Min entropy: " + str(min))
    print("Max entropy: " +str(max))



if __name__ == '__main__':
    main()
