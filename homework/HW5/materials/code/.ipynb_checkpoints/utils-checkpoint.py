import json
import random
import linecache
import math
import numpy as np
import torch

#-----------------------------------------------------------------
# Counts the number of lines in a file
#-----------------------------------------------------------------
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1




def csvToJsonl(source_file, destination_file, batch_size, verbose = False):
    #-----------------------------------------------------
    # Paramters 
    #-----------------------------------------------------
    data_path   = source_file            # Location of to read the original data.
    savedir     = destination_file       # Where do we want to save the reformatted data:
    total_lines = file_len(source_file)  # Get the total number of lines in the source file

    #-----------------------------------------------------
    # Output File Initialization
    #-----------------------------------------------------
    # Initialize the output file as blank
    with open(savedir, 'w') as outfile:
        outfile.write('')

    # Open the output file- the 'a' means append
    outfile = open(savedir, "a")

    #-----------------------------------------------------
    # Reading Input File
    #-----------------------------------------------------
    with open(data_path) as read_file:

        #-----------------------------------------------------
        # Processing Header
        #-----------------------------------------------------
        line    = read_file.readline()                # read the first line - containing the header
        headers = line.replace('\n','').split(',')    # remove the newline character, and split on ',' to get column names
        
        #-----------------------------------------------------
        # Processing Contents
        #-----------------------------------------------------
        line_cnt     = 1                              # How many lines have we read in
        batch_number = 0                              # Which batch are we processing
        json_lines   = []                             # List to store the batch
        
        while line:
            
            json_line  = {}                          # initialize an empty dict we will use to store the data in this line as json
            line       = read_file.readline()        # read in the line
            line_cnt += 1                            # increment the line counter
            
            #-----------------------------------------------------
            # Parsing CSV contents into JSON
            #-----------------------------------------------------        
            processed_line        = line.replace('\n',' ').split(',')                   # replace the '\n' and split on the commas.
            json_line[headers[0]] = processed_line[0]                                   # everything before the first comma is freshness score.
            json_line[headers[1]] = ','.join(processed_line[1:]).strip('"').strip(' ')  # everything after the first comma is the review text.
            json_lines.append(json_line)                                                # Add this line to the list of lines from this batch

            #-----------------------------------------------------
            # Saving Batch
            #-----------------------------------------------------
            if len(json_lines) == batch_size:
                
                # Convert the data and save it to disk
                for entry in json_lines:
                    json.dump(entry, outfile)
                    outfile.write('\n')

                # Clear the batch
                json_lines = []

                if verbose == True:
                    print('Processed Batch', batch_number, ': ', line_cnt, '/', total_lines, 'Lines')
                
                # Increment the batch number
                batch_number += 1
    
    #-----------------------------------------------------            
    # Convert the last batch of data and save it to disk
    #-----------------------------------------------------
    json_lines.pop()
    for entry in json_lines:
        json.dump(entry, outfile)
        outfile.write('\n')
    print('Processed Batch', batch_number, ': ', line_cnt-1, '/', total_lines, 'Lines')

    # close the output file    
    outfile.close()

    
#-----------------------------------------------------------------
# Takes a jsonl formatted data, and returns a batch
# that matches your specifications
#-----------------------------------------------------------------
# - data_path    : the path to the .jsonl data file
#
# - batch_size   : the size of the batch you want, 
#                  e.g. '10' would be 10 rows
#
# - batch_number : the batch number you want, 
#                   e.g. '2' would return the 2nd batch of 10 rows
#
# - random_seed  : seed to shuffle the data before getting the batch
#
# - total_lines  : the total number of lines in the file.
#                  not required, but speeds things up if you have it.
#-----------------------------------------------------------------
def getBatch(data_path, batch_number = 1, batch_size = 1000, random_seed = 1, total_lines = None):
    
    # Initialize some variables we will use
    line, line_num, json_lines, = True, 0, []
    
    # Get the total number of lines in the file
    if total_lines == None:
        num_lines = file_len(data_path)
    else:
        num_lines = total_lines
        
    # Shuffle the index of the data according to the seed.
    random.seed(random_seed)
    index = list(range(num_lines))
    random.shuffle(index)
    
    # Get the line numbers we want to keep for this batch, according to the index
    start, end     = (batch_number * (batch_size)), ((batch_number + 1) * (batch_size))
    batch_indicies = index[start:end]
    batch_indicies.sort()
    
    # Open the file, and read in one-line at a time.
    with open(data_path) as read_file:
        while line:   
            
            # Read in the line
            line = read_file.readline()
            
            # If this line is meant to be in the batch, keep it.
            if line_num == batch_indicies[0]:
                processed_line = json.loads(line)
                json_lines.append(processed_line)
                batch_indicies.pop(0)
                
            # Increment the counter
            line_num += 1
            
            
            # Check if we've reached the end of the file, or found all items in the batch
            if line_num == num_lines or len(batch_indicies) == 0:
                break
    
    
    
    # If the size of this batch is less than the requested amount, it's the last batch
    last_batch = False
    if len(json_lines) < batch_size:
        last_batch = True
      
    
    return json_lines, last_batch

