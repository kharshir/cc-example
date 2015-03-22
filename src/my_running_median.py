# example of running median program
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
output_file = sys.argv[2] #"./wc_output/med_result.txt"
file_list = list_files( input_dir )
remchar_list = """-'"/"""
repchar_list = ".,()"
word_count_list = []
fo = open(output_file, 'w')

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
# find word length of the line
#        print len(line_sp),
        word_len = len(line_sp)
# if word_len = 1 and if its nothing, just replace it with zero.
        if word_len == 1 and line_sp[0] == '':
            word_len = 0
#        print line_sp,
#        print '\n',

# append float value of word length to the list 
        word_count_list.append(float(word_len))
# sort the list in ascending order
        word_count_list.sort()
# find length of word_count_list and find the median from that
        list_length = len(word_count_list)

# calculate running median
        running_median = (word_count_list[(list_length-1)/2]+word_count_list[(list_length-1)/2+(list_length-1)%2])/2
#        print word_count_list,
#        print '\n'+str(running_median)+'\n',
        fo.write(str(running_median)+'\n')
    fd.close()

fo.close()
