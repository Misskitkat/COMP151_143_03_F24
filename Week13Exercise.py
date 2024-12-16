from pathlib import Path

def count_e():
    path = Path('paragraph.txt')
    contents = path.read_text()
    nums_e = 0
    for i in range(0, len(contents)):
        if contents[i].lower() == 'e':
            nums_e += 1
    path_out = Path('file_out.txt')
    message = "Number of letter e's in course description: " + str(nums_e)
    path_out.write_text(message)

count_e()
print("Open the file_out.txt to see if it worked.")

def write_greetings():
    path = Path("names.txt")
    content = path.read_text()
    lines = content.splitlines()
    msg = ""
    for name in lines:
        msg += "Dear " + str(name) + ", \n"
    path_out = Path('greetings_out.txt')
    path_out.write_text(msg)

write_greetings()
print("Open the greetings_out.txt file to check if it worked.")

def compute_average():
    path = Path("numbers.txt")
    sum = 0
    content = path.read_text()
    lines = content.splitlines()
    for number in lines:
        if float(number):
            sum += float(number)
    average = sum // len(lines)
    path_out = Path('numbers_out.txt')
    path_out.write_text(f"The average is: {average}")

compute_average()
print("Open the numbers_out.txt to see if it worked.")

def compute_median():
    path = Path("numbers_sorted.txt")
    content = path.read_text()
    median = 0
    nums_list = []
    lines = content.splitlines()
    for number in lines:
        nums_list.append(float(number))
    if len(nums_list) // 2 == 0:
        median = nums_list[(len(nums_list) // 2)-1]
    else:
        middleish = (len(nums_list) // 2) - 1
        middle = nums_list[middleish]+nums_list[middleish+1]
        median = float(middle)/2
    path_out = Path("median_out.txt")
    path_out.write_text(f"The median of the provided list of numbers is: {median}")

compute_median()
print("Open the median.txt to check if it worked.")