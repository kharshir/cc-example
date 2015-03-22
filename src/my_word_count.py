# example of word_count program
import os, sys
from collections import defaultdict

## List files in input directory
def list_files(path):
    # returns a list of file names (with extension, without full path)
    # of all files in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    return files


input_dir = sys.argv[1] #"./wc_input"
#output_dir = "./wc_output"
output_file = sys.argv[2] #"./wc_output/wc_result.txt"
file_list = list_files( input_dir )
remchar_list = """-'"/"""
repchar_list = ".,()"
word_list = defaultdict(int)

# Traverse through all the files in directory
for file_single in file_list:
    fd = open(input_dir+'/'+file_single, 'r')

# Traverse through all the lines in a file
    for line in fd:
# Remove the unnecessary characters in a line
        for char in line:
            if char in remchar_list:
                line = line.replace(char,'')
#        print line+'\n',
# Replace certain characters with space
        for char in line:
            if char in repchar_list:
                line = line.replace(char,' ')
#        print line+'\n',
# Replace multiple spaces with single space
#        line = line.replace('  ',' ')
        line = ' '.join(line.split())
#        print line+'\n',
# Replace beginning and trailing whitespace
        line = line.strip()
#        print line+'\n',
# Split line based on space
        line_sp = line.split(' ')
#        print line_sp,
# if word_len = 1 and if its nothing, continue the loop
        word_len = len(line_sp)
        if word_len == 1 and line_sp[0] == '':
            continue
# Check if words are in the word_list and take a decision
        for word in line_sp:
            word = word.lower()
#            print word+'\n',
            word_list[word] += 1
        
    fd.close()


# All the words are counted.by now.
# Final Unsorted list
final_list = word_list.items()

# Final sorted list
final_list.sort(key=lambda x: x[0])
#print final_list,

# Write sorted list items to output file
fd = open(output_file, 'w')

for line in final_list:
    fd.write("%s\t%s\n" % line)

fd.close()
