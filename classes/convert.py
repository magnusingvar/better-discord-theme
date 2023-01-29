file = open('classes.txt')
f = open('../classes.scss', 'w+')
# f = open('output.txt', "w+")

for line in file:
    l = []
    c = line.strip()

    l = c.split("=")

    f.write('.' + l[1].strip() + ' {}' + '\n')
    # print(l[1].strip())