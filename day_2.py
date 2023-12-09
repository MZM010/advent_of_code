i, counter = 0, 0
my_list = []
red, blue, green = "red", "blue", "green"

def check_color(number, color):
    var = 0
    if color == red and number > 12:
        var += 1
    elif color == blue and number > 14:
        var += 1
    elif color == green and number > 13:
        var += 1
    return var
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.split(":")[1].strip()
        correct_cube = 0
        i += 1
        cube = 0
        for lines in line.split("; "):
            for my_line in lines.split(", "):
                cube += 1
                num, color = my_line.split(" ")
                num = int(num)
                check = check_color(num, color)
                if check == 0:
                    correct_cube += 1
        if correct_cube == cube:
            counter += i
print("the counter is :",counter)