import requests
import nltk
from nltk.util import ngrams
import requests
import time
import json
import math

# Importing the `punkt` data, used by the NLTK tokenizer
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')


# An ngram extractor 
def extract_word_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]


# Counts the frequency of token occurences in some text.
def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq




def basicLanguageModel(data, gram_size = 1):
    
    grams  = extract_word_ngrams(data,gram_size) 
    counts = {}
        
    
    # -----------------------------------------------
    # Count the next gram, given the current gram:
    # -----------------------------------------------
    possible_nextgrams = len(list(set(grams)))
    for i in range(len(grams)-1):
        if grams[i] not in counts:
            counts[grams[i]]                     = {}
            counts[grams[i]]['___NUMBLANKGRAMS___'] = possible_nextgrams - 1
            counts[grams[i]][grams[i+1]] = 2   
        else:
            if grams[i+1] not in counts[grams[i]]:
                counts[grams[i]][grams[i+1]] = 1
                counts[grams[i]]['___NUMBLANKGRAMS___'] -= 1
            else:
                counts[grams[i]][grams[i+1]] += 1

    if grams[len(grams)-1] not in counts:
        counts[grams[len(grams)-1]] = {} 

    # -----------------------------------------------
    # convert the counts to probabilites and Laplacian Smooth
    # -----------------------------------------------
    probs = counts
    for key, value in counts.items():
        denominator = 0
        total_prob  = 0
        for key2, value2 in counts[key].items():      
            denominator += value2

        for key2, value2 in counts[key].items():
            if key2 != '___NUMBLANKGRAMS___':
                probs[key][key2] = value2 / denominator
                total_prob      += probs[key][key2]
        
        if '___NUMBLANKGRAMS___' not in counts[key]:
            counts[key]['___NUMBLANKGRAMS___'] = possible_nextgrams
            counts[key]['___BLANKUNITPROB___'] = 1/(possible_nextgrams)
        
        
        elif counts[key]['___NUMBLANKGRAMS___'] != 0:
            probs[key]['___BLANKUNITPROB___'] = (1-total_prob)/counts[key]['___NUMBLANKGRAMS___']
        else:
            probs[key]['___BLANKUNITPROB___'] = 0
      
    # -----------------------------------------------
    # Obtain the prior probabilities for each gram:
    # -----------------------------------------------
    gram_counts = CountFrequency(grams)
    count_total = sum(gram_counts.values())
    for key, value in gram_counts.items():
        probs[key]['___PRIOR___'] = value/count_total
        
    probs['___TOTALTOKENS___']  = len(grams)
    probs['___UNIQUETOKENS___'] = len(set(grams))
    return probs


# Generate a backoff model:
def trainBackoffModel(corpora, max_gram_size):
    langauge_model = []
    for gram_size in range(1,max_gram_size+1):
        langauge_model.append(basicLanguageModel(corpora, gram_size = gram_size))
    return langauge_model


# Returns the log probability of some new text, given the language model
def evaluateBackoffLangaugeModel(data, model, prior = True, verbose = False):

    # Begin by extracting a set of unigrams 
    segments      = extract_word_ngrams(data, 1)
    max_gram_size = min([len(segments), len(model)])

    segment_start = 0
    initial       = True
    log_prob      = 0
    complete      = False
    
    # Ideally, we would like to use the entire given segment, but if we can't find it
    # In the dictionary, we will back out, and check if we can find a match for a smaller
    # n-gram.
    while segment_start < (len(segments)-max_gram_size+1):
        
        found_match = False
        for i in range(max_gram_size):

            segment_end   = segment_start + (max_gram_size)
            given_segment = segments[segment_start+i:segment_end]
            given_gram    = ' '.join(given_segment)
            model_index   = max_gram_size-i-1
            if verbose == True:
                print('GIVEN GRAM:"', given_gram, '"')

            
            # We will check if this n-gram exists in the model
            if given_gram in model[model_index]:
                next_segment = segments[segment_start+i+1:segment_end+1]
                next_gram    = ' '.join(next_segment)
                if verbose == True:
                    print('NEXT GRAM:"', next_gram, '"')

                if next_gram in model[model_index][given_gram]:
                    
                    # Apply the prior probability
                    if initial == True and prior == True:
                        log_prob += math.log(model[model_index][given_gram]['___PRIOR___'])
                        initial  = False
                
                        if verbose == True:
                            print('log[p(' + given_gram + ')] = ' + str(log_prob))
                    
                    # Apply the conditional probability
                    if verbose == True:
                        print('log[p(' + next_gram + '|' + given_gram + ')] = ' + str(math.log(model[model_index][given_gram][next_gram])))
                        print('\n')
                        
                    log_prob += math.log(model[model_index][given_gram][next_gram])
                    found_match = True
                    break
                    
                else:
                    if verbose == True:
                        print('BACKING OFF: can not find match in dictionary for next gram "' + next_gram + '"')
                        print('\n')      

            else:
                if verbose == True:
                    print('BACKING OFF: can not find match in dictionary for given gram "' + given_gram + '"')
                    print('\n')
        
        # Laplacian Smoothing for next grams
        if found_match == False:
            if verbose == True:
                print('SMOOTHING: No match found, applying laplacian probability')
            
            # If the next-gram is missing:
            if given_gram in model[model_index]: 
                log_prob += math.log(model[model_index][given_gram]['___BLANKUNITPROB___'])
                if verbose == True:
                    print('log[p(' + next_gram + '|' + given_gram + ')] = ' + str(math.log(model[model_index][given_gram]['___BLANKUNITPROB___'])))
            
            # If the given gram is missing:
            else:
                log_prob += math.log(1 / (model[model_index]['___TOTALTOKENS___'] + 1))
                if verbose == True:
                    print('log[p(' + given_gram + ')] = ' + str(math.log(1 / (model[model_index]['___TOTALTOKENS___'] + 1))))
            
        segment_start+= 1
        
    return(log_prob)
