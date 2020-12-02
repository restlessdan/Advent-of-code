class passwords:
    def __init__(self,_min,_max,_query,password):
        self._min = _min
        self._max = _max
        self._query = _query
        self.password = password 

f = open('passwords.txt', 'r')

textlist = [line.replace('\n', '').replace(" ",",").replace(":", "").replace("-",",") for line in f.readlines()]

_list = [tuple(x.split(",")) for x in textlist]
passwordlist = []

for y in _list:
    passwordlist.append(passwords(int(y[0]),int(y[1]),y[2],y[3]))

count = 0
badpass = 0
for t in passwordlist:
    if t.password[t._min - 1] == t._query and t.password[t._max - 1] != t._query:
        print(t.password[t._min - 1] + " position " + str(t._min) + " " + t.password[t._max - 1] + " position " + str(t._max) + " " + t.password)
        count = count + 1
        #if x == t._query:
        #    count = count +1
    #if count > t._max or count < t._min:
    #    badpass = badpass + 1

print(count)
#print(len(passwordlist) - badpass)