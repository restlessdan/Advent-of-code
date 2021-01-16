tree = '#'
f = open("map.txt", "r")

tobbogan = [l.replace('\n', '') for l in f.readlines()]

def comingdownthemountain(mountain, right, down):
    _y = len(mountain)
    _x = len(mountain[0])
    _row = 0
    _col = 0
    count = 0
    for x in range (_row, _y, down):
        #print(x)
        if mountain[_row][_col%_x] == tree:
            count +=1
        _col += right
        _row += down
    return count

result = (comingdownthemountain(tobbogan,1,1) * comingdownthemountain(tobbogan, 3,1) * comingdownthemountain(tobbogan, 5,1) * comingdownthemountain(tobbogan, 7,1) * comingdownthemountain(tobbogan, 1,2))
print (result)
