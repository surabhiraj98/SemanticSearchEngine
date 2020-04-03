# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:00:07 2020

@author: HP
"""
import os
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)
#each website crawl in the seperate folder
#create_project_dir('Youtube')

#create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
     queue = project_name + '/queue.txt'
     crawled = project_name + '/crawled.txt'
     if not os.path.isfile(queue):
         write_file(queue, base_url)
     if not os.path.isfile(crawled):
         write_file(crawled, '')
        
        
#create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
#create_data_files('Youtube','https://www.youtube.com/')
#add data into an existing file

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

#delete the content of a file
def delete_to_file(path):
    with open(path,'w'):
        pass
#read files and convert ech into a set of items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")