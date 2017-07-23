import os, random 
import string

morse = { 'A':'.-'  ,'B':'-...', 'C':'-.-.','D':'-..' , 
          'E':'.'   ,'F':'..-.', 'G':'--.' ,'H':'....', 
          'I':'..'  ,'J':'.---', 'K':'-.-' ,'L':'.-..', 
          'M':'--'  ,'N':'-.'  , 'O':'---' ,'P':'.--.', 
          'Q':'--.-','R':'.-.' , 'S':'...' ,'T':'-'   , 
          'U':'..-' ,'V':'...-', 'W':'.--' ,'X':'-..-', 
          'Y':'-.--','Z':'--..'}

def random_line(filei, total_bytes):
    random_point = random.randint(0, total_bytes)
    filei.seek(random_point)
    filei.readline() # skip this line to clear the partial line
    return filei.readline()

file_name = '/usr/share/dict/words'
word_file = open(file_name)
total_bytes = os.stat(file_name).st_size 

output = ""
words = []
while (len(output) < 1000):

    line = random_line(word_file, total_bytes)
    line = line.strip().upper()
    line = line.translate(line.maketrans('','',string.punctuation))

    words.append(line)
    for c in line:
        output += morse[c]

print(1)
print()
print(output)
print(10000)

#word_file = open('/usr/share/dict/words')
word_file = open(file_name)
for _ in range(10000-len(words)):
    line = word_file.readline();
    line = line.strip().upper()
    line = line.translate(line.maketrans('','',string.punctuation))
    print(line)

for word in words:
    print(word)
