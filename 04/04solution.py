import re

f = open('passport.txt', 'r')
reglist =[r"(ecl:)(amb|blu|brn|gry|grn|hzl|oth)", r"(byr:)(192[0-9]|19[2-9][0-9]|20[0-2]{2})", r"(iyr:)(2010|2020|20[1-9]{2})", r"(eyr:)(2030|2020|202[0-9])", r"(hgt:)(59|[6][0-9]|[7][0-6])in|(hgt:)(19[0-3]|1[5-8][0-9])cm", r"hcl:#[0-9a-z]{6}", r"pid:[0-9]{9}{\s}"]
passportlist = f.read().split('\n\n')
count  = 0
valid = 0
cleanlist = [line.replace('\n', " ") for line in passportlist]

for x in cleanlist:
    for reg in reglist:
        foundmatch = re.match(reg, x, re.MULTILINE)
        if not foundmatch:
            break
        else:
            count += 1
    print(x)
    if count == 7:
        valid +=1
    count = 0

print(valid)