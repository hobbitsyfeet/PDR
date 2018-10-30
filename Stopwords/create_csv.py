import sys
import csv
import os
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

word_file = sys.argv[1]
new_file = sys.argv[2]

#populates file [argv 2] with a list of words from [argv 1]
def populate_file(file):
    with open(file, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_ALL)
        writer.writerow(create_list(word_file))
    csv_file.close()

#returns a list of words from a file of words seperated by line.
def create_list(file):
    with open(file, 'r') as wordlist:
        temp_list = []
        for line in wordlist:
            if line not in ['\\n', '\\r', '\\ni', '',]:
                line = line.replace("\n","")
                if len(line) is not 0:
                    temp_list.append(line)

    wordlist.close()
    return(temp_list)

print("Checking for file...")
if os.path.isfile(new_file):
    populate_file(new_file)
else:
    f = open(new_file,"w")
    f.close()
    populate_file(new_file)
