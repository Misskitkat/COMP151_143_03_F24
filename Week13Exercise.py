from pathlib import Path
path = Path('paragraph.txt')
contents = path.read_text()

def count_e():
    nums_e = 0
    for i in range(0, len(contents)):
        if contents[i].lower() == 'e':
            nums_e += 1
    path_out = Path('file_out.txt')
    message = "Number of letter e's in course description: " + str(nums_e)
    path_out.write_text(message)

count_e()
