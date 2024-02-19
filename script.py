import os
import re
from collections import Counter
import socket

# a. List name of all the text files at location: /app
text_files = [f for f in os.listdir('/app') if f.endswith('.txt')]

# b. Read the two text files and count total number of words in each text file
total_words = 0
for file_name in text_files:
    with open(file_name, 'r') as file:
        words = re.findall(r'\b\w+\b', file.read())
        word_count = len(words)
        print(f"Total words in {file_name}: {word_count}")
        total_words += word_count

# c. Add all the number of words to find the grand total
print(f"Grand Total Words: {total_words}")

# d. List the top 3 words with maximum number of counts in IF.txt
if_word_counts = Counter(re.findall(r'\b\w+\b', open('IF.txt').read()))
top_3_words = if_word_counts.most_common(3)
print("Top 3 words in IF.txt with counts:")
for word, count in top_3_words:
    print(f"{word}: {count}")

# e. Find the IP address of your machine
ip_address = socket.gethostbyname(socket.gethostname())
print(f"IP Address of the machine: {ip_address}")

# f. Write all the output to a text file at location: /app/result.txt
output_file_path = '/app/result.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(f"Total words in each file:\n")
    for file_name in text_files:
        output_file.write(f"{file_name}: {word_count}\n")
    output_file.write(f"\nGrand Total Words: {total_words}\n")
    output_file.write(f"\nTop 3 words in IF.txt with counts:\n")
    for word, count in top_3_words:
        output_file.write(f"{word}: {count}\n")
    output_file.write(f"\nIP Address of the machine: {ip_address}\n")
