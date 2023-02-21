import csv
import string

translator = str.maketrans('', '', string.punctuation)

word_count = {}

try:
    file = open('./begginercode/test.txt').read()
    text = 1
except:
    print("no se pudo abrir el archivo... error code: 1")
    text = input("ingrese una frase:  \t\t\n")
    type = 2

words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])