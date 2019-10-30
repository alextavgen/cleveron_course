from pprint import pprint
import re
from os import listdir
from os.path import isfile, join

import urllib

import networking


def get_files_list(mypath):
    files_list = list()

    for filename in listdir(mypath):
        if isfile(mypath + filename):
            if 'txt' in filename:
                files_list.append(mypath + filename)
    return files_list

def fetch_data_from_file(filename):
    with open(filename, 'r') as inputfile:
        data = inputfile.readlines()
    return data


def word_count(lines_of_file):
    words_count = dict()
    for line in lines_of_file:
        line = re.sub('[^A-Za-z0-9]+', '', line)
        words_list = line.split(' ')
        # print(words_list)
        for word in words_list:
            word = word.lower()
            word = re.sub('[^A-Za-z0-9]+', '', word)
            if word in words_count:
                # words_count[word] = words_count[word] + 1
                words_count[word] += 1
            else:
                words_count[word] = 1
    return words_count


def print_sorted_dictionary(data_dictionary):
    ordered_dictionary = sorted(data_dictionary, key=data_dictionary.get, reverse=True)

    for key in ordered_dictionary:
        pprint(key + ' ' + str(data_dictionary[key]))

mypath = '/Users/aleksandr.tavgen/Downloads/'

list_of_files = get_files_list(mypath)


URL = "http://www.gutenberg.org/files/11/11-0.txt"


for filename in list_of_files:
    #data_from_file = fetch_data_from_file(filename)

    data_from_network = networking.get_from_network('http://postimees.ee')

    word_count_dictionary = word_count(data_from_network)
    print_sorted_dictionary(word_count_dictionary)