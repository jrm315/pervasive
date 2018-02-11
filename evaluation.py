log = open('flooding_coursework.txt', 'r')

for lines in log:
    line = lines.split()

    if line[0] < "05:00.000":
        continue
    print(line)
