somme = 0
with open("day1_part2.txt",'r') as f:
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
            }
    for line in f.readlines():
        lines = line.strip()
        num = []
        f, e = 0 , 0
        while e < len(lines) + 1:
               if lines[f:e] in numbers.keys():
                   num.append(numbers[lines[f:e]])
               if lines[f:e].isdigit():
                   num.append(lines[f:e])
               e += 1
               if e == len(lines) + 1:
                    f += 1
                    e = f
        if len(num) == 1:
            somme += int(num[0]*2)
            continue
        somme += int(num[0]+num[-1])
print(somme)


