f = open('sales.txt', 'r')
listofexpenses = [int(line.replace('\n','')) for line in f.readlines()]

def checkfor2020(_input, out):
    for i in range(len(_input)):
        for x in range(i + 1, len(_input)):
            for y in range(x+1, len(_input)):
                if _input[i] + _input[x] + _input[y] == out:
                    print (_input[i] * _input[x] * _input[y])

checkfor2020(listofexpenses, 2020)
#for i in listofexpenses:
 #   print(i)