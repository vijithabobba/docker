import os

import re

import socket

 

 

files = os.listdir('/app')

text_files = [f for f in files if f.endswith('.txt')]

print("Text files list:" ,text_files)

 

 

word_counts = []

for file in text_files:

    with open(os.path.join('/app', file), 'r') as f:

        text = f.read()

        words = text.split()

        word_count = len(words)

        word_counts.append(word_count)

        print(f'The Total number of words in {file}:{word_count}\n')

 

 

grand_total = sum(word_counts)

 

 

 

if_file = os.path.join('/app', 'IF.txt')

with open(if_file, 'r') as f:

    text = f.read()

    words = text.split()

    word_counts = {}

    for word in words:

        if word in word_counts:

            word_counts[word] += 1

        else:

            word_counts[word] = 1

    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]

 

 

ip_address = socket.gethostbyname(socket.gethostname())

 

 

output_file = '/app/result.txt'

with open(output_file, 'w') as f:

    f.write(f'Total number of words in both files: {grand_total}\n')

    f.write(f'Top 3 words in IF.txt:\n')

    for word, count in top_words:

        f.write(f'{word}: {count}\n')

    f.write(f'IP address of this machine: {ip_address}\n')

 

 

with open(output_file, 'r') as f:

    print(f.read().strip())
