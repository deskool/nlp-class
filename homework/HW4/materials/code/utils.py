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

#-----------------------------------------------------------------
# Converts the rotton tomatoes movie dataset from csv to jsonl
#-----------------------------------------------------------------
# - source_file        : the source csv file
# - destination_file   : where to store the converted data, e.g. myfile.jsonl
# - batch_size         : How many lines to process at a time, e.g. 10000
# - verbose            : will print progress towards completion when verbose = True
#-----------------------------------------------------------------
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
# Splits a line according to the 
#-----------------------------------------------------------------
# - file               : the source jsonl file
# - splits             : a dict that incidates the splits, and their percentage. see top of function for example.
# - random seed        : the random seed when sampling the data
# - batch_size         : How many lines to process at a time, e.g. 10000
# - verbose            : will print progress towards completion when verbose = True
#-----------------------------------------------------------------
def splitFile(file, splits=None, random_seed=1, batch_size=1000, verbose = False):

    if splits is None:
        splits = {'train':{'percentage':60},'validation':{'percentage':20},'test':{'percentage':20}}
    
    #------------------------------------------------------
    # Check that the splits sum to 100.
    #------------------------------------------------------
    sum_splits_percs = sum([splits[key]['percentage'] for key,val in splits.items()])
    if sum_splits_percs != 100: 
        print('-------------------------------------------')
        print('Notice:split percentages do not sum to 100.')
        print('-------------------------------------------')


    #-------------------------------------------------------
    # Get the number of samples in each split
    #-------------------------------------------------------
    n   = file_len('materials/data/rt_reviews/re_reviews.jsonl')
    cnt, n_remaining = 1, n;
    for key,val in splits.items():
        if cnt != len(splits):
            splits[key]['samples'] = math.floor(splits[key]['percentage']/100 * n)
            n_remaining           -= splits[key]['samples']
        if cnt == len(splits):
            splits[key]['samples'] = n_remaining
        cnt += 1

    #-----------------------------------------------------
    # Output File Initialization
    #-----------------------------------------------------
    dirname, filename  = '/'.join(file.split('/')[:-1]), file.split('/')[-1]
    for key,val in splits.items():
        savedir = dirname + '/' + key + '_' + filename
        print('Initializing: ', savedir)
        with open(savedir, 'w') as outfile:
            outfile.write('')

    #-----------------------------------------------------
    # Shuffle the data
    #-----------------------------------------------------
    random.seed(random_seed)
    index = list(range(n))
    random.shuffle(index)
    
    #-----------------------------------------------------
    # Assign line numbers to each of the splits
    #-----------------------------------------------------
    split_indicies = [splits[key]['samples'] for key,val in splits.items()]
    for i,key in enumerate(splits):
        # Get the line numbers we want to keep for this batch, according to the index
        start, end  = sum(split_indicies[:i]), sum(split_indicies[:i+1])
        indicies = index[start:end]
        indicies.sort()
        splits[key]['line_numbers'] = indicies 

    #-----------------------------------------------------
    # Reading Input File
    #-----------------------------------------------------
    with open(file) as read_file:

        batch_number = 1

        #-----------------------------------------------------
        # Processing Contents
        #-----------------------------------------------------
        # Initialize an object to hold the lines
        json_lines = {}
        for key,val in splits.items():
            json_lines[key] = []                     

        # For each line in the file
        line_num, line = 0, True                              
        while line:

            # Read in the line
            line = read_file.readline()    
            # See which split is belongs to
            for i,key in enumerate(splits):
                if len(splits[key]['line_numbers']) > 0:
                    if splits[key]['line_numbers'][0] == line_num:
                        json_lines[key].append(line)
                        splits[key]['line_numbers'].pop(0)

            # If we've completed a batch, then save to disk
            if line_num % batch_size == 0 and line_num > 0:        
                    # Convert the data and save it to disk
                    for key in json_lines:
                        savedir = dirname + '/' + key + '_' + filename
                        with open(savedir, 'a') as outfile:
                            for entry in json_lines[key]:
                                outfile.write(entry)

                    json_lines = {}
                    for key,val in splits.items():
                        json_lines[key] = []

                    if verbose == True:
                        print('Processed Batch', batch_number, ': ', line_num, '/', n, 'Lines')

                    # Increment the batch number
                    batch_number += 1

            # Check if we've reached the end of the file, or found all items in the batch
            if line_num == n:
                break

            # increment the line number
            line_num += 1


    #-----------------------------------------------------
    # Convert the last batch of data and save it to disk
    #-----------------------------------------------------
    for key in json_lines:
        savedir = dirname + '/' + key + '_' + filename
        with open(savedir, 'a') as outfile:
            for entry in json_lines[key]:
                outfile.write(entry)

    if verbose == True:
        print('Processed Batch', batch_number, ': ', line_num, '/', n, 'Lines')
        

#--------------------------------------------------------
# A function to load the word vectors
#--------------------------------------------------------
def loadEmbeddings(path, vocabulary, embedding_dim=50):
    svocabulary = set(vocabulary)
    with open(path) as f:
        embeddings = np.zeros((len(vocabulary), embedding_dim))
        for line in f.readlines():
            values  = line.split()
            word    = values[0]
            if word in svocabulary:
                index  = vocabulary.index(word)
                vector = np.array(values[1:], dtype='float32')
                embeddings[index] = vector
        return torch.from_numpy(embeddings).float()
    
#-------------------------------------------------------------
# Cleans the text, and converts it to indicies (one-hot-coding)
#--------------------------------------------------------------
def cleanText(sentence, word2idx):
    sentence = sentence.lower().replace("'",'').replace('-',' ').replace(",", "").replace(".", "")
    sentence = sentence.split()
    
    indicies,clean_sent   = [], []
    for word in sentence:
        if word in word2idx:
            indicies.append(word2idx[word])
            clean_sent.append(word)
    return indicies, clean_sent


#No. of trianable parameters
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def onehot(list_of_tokenized_sentences, vocabulary):
    svocabulary = set(vocabulary)
    for i,sentence in enumerate(list_of_tokenized_sentences):    
        for j,word in enumerate(sentence):
            if word in svocabulary:
                list_of_tokenized_sentences[i][j] = vocabulary.index(word)
            else:
                list_of_tokenized_sentences[i][j] = vocabulary.index('<missing>')
    return list_of_tokenized_sentences


def prepareVocabulary(vocab_json = 'materials/data/rt_reviews/vocabulary.json', remove_less_than = 25):
    with open(vocab_json) as json_file:
        full_vocabulary = json.load(json_file)

    # Let's reduce the vocabulary further by eliminating words that rarely show up.
    vocabulary = []
    for key,val in full_vocabulary.items():
        if val >= remove_less_than:
            vocabulary.append(key)
    
    print('Adding tokens for padding <pad> at position [0], and missing <missing> at position [1]')
    vocabulary = ['<pad>'] + ['<missing>'] + sorted(vocabulary)
    return vocabulary