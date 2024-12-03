import re

with open('dag3input.txt') as f:
    mem = f.read() 

result = 0
result2 = 0

def multer (mem, result):
    memSafe = re.findall(r'(mul\()(\d+)(,)(\d+)(\))', mem)
    #print(memSafe)
    for mul in memSafe:
        memSafeNums = list(filter(str.isnumeric, mul))
        #print(memSafeNums)
        result+=(int(memSafeNums[0])*int(memSafeNums[1]))
    print(result)

multer(mem, result)
#print(result)

filterMem = re.sub(r'((don\'t\(\))(.*?)(do\(\)|$))',"", mem, flags=re.DOTALL)
multer(filterMem, result2)

