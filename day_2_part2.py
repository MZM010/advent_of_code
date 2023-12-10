i, counter = 0, 0
my_list = []
red, blue, green = "red", "blue", "green"


def checkred(num, color):
    global MAX_RED
    if color == red:
        if MAX_RED < num:
            MAX_RED = num
    return MAX_RED
def checkblue(num, color):
    if color == blue:
        global MAX_BLUE
        if MAX_BLUE < num:
            MAX_BLUE = num
    return MAX_BLUE
def checkgreen(num, color):
    if color == green:
        global MAX_GREEN
        if MAX_GREEN < num:
            MAX_GREEN = num
    return MAX_GREEN
with open('input.txt', 'r') as file:
    for line in file.readlines():
        MAX_BLUE = 0
        MAX_RED = 0
        MAX_GREEN = 0
        power = 1
        line = line.split(":")[1].strip()
        correct_cube = 0
        i += 1
        cube = 0
        for lines in line.split("; "):
            for my_line in lines.split(", "):
                cube += 1
                num, color = my_line.split(" ")
                num = int(num)
                max_blue = checkblue(num, color)
                max_red = checkred(num, color)
                max_green = checkgreen(num, color)
        print(f"the max blue and red and green is {max_blue} {max_red} {max_green}")
        power = MAX_GREEN * MAX_BLUE * MAX_RED
        counter += power
print("the counter is :",counter)
