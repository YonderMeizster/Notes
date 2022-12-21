import os

files = os.listdir()
files.remove('Изучаем Python том 1.pdf')
files.remove('count_words.py')

words = 0
outfile = open('out.txt', 'w', encoding = 'utf-8')

for file in files:
    for line in open(file, encoding = 'utf-8'):
        outfile.write(line)
        words += len(line.split())


print(words)
