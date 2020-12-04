from sklearn.feature_extraction.text       import CountVectorizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.base     import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm      import LinearSVC
from nltk.corpus      import stopwords
from spacy.tokens     import Doc

import string
import re
import spacy
import regex as re


re.DEFAULT_VERSION = re.VERSION1
split_chars = lambda char: list(char.strip().split(' '))
#-------------------------------------------------------------------
# DEFAULT SETTINGS
#-------------------------------------------------------------------

# SPACY NLP MODEL
nlp = spacy.load('en_core_web_sm')

#--------------------------------------------------------------------
# STOPWORDS TO BE REMOVED
#--------------------------------------------------------------------
STOPLIST = set(stopwords.words('english') + ["n't", "'s", "'m", "ca"] + list(ENGLISH_STOP_WORDS))

#--------------------------------------------------------------------
# SYMBOLS TO BE REMOVED
#--------------------------------------------------------------------
SYMBOLS = " ".join(string.punctuation).split(" ") + ["-----", "---", "...", "“", "”", "'ve"]

#--------------------------------------------------------------------
# CAPTURE WHITESPACE CHARACTERS
#--------------------------------------------------------------------
WHITESPACE = ["", " ", "  ", "   ","    ", "\t", "\n", "\r\n", "\n\n"]

#--------------------------------------------------------------------
# WORDS THAT MEAN NUMBERS
#--------------------------------------------------------------------
NUM_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
              'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
              'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
              'hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
              'gajillion', 'bazillion']

#--------------------------------------------------------------------
# UNTIS
#--------------------------------------------------------------------
_units = ('km km² km³ m m² m³ dm dm² dm³ cm cm² cm³ mm mm² mm³ ha µm nm yd in ft '
          'kg g mg µg t lb oz m/s km/h kmh mph hPa Pa mbar mb MB kb KB gb GB tb '
          'TB T G M K % км км² км³ м м² м³ дм дм² дм³ см см² см³ мм мм² мм³ нм '
          'кг г мг м/с км/ч кПа Па мбар Кб КБ кб Мб МБ мб Гб ГБ гб Тб ТБ тб'
          'كم كم² كم³ م م² م³ سم سم² سم³ مم مم² مم³ كم غرام جرام جم كغ ملغ كوب اكواب')
UNITS  = split_chars(_units)

#--------------------------------------------------------------------
# CURRENCY
#--------------------------------------------------------------------
_currency = r'\$ £ € ¥ ฿ US\$ C\$ A\$ ₽ ﷼ ₴'
CURRENCY  = split_chars(_currency)

#--------------------------------------------------------------------
# PUNCTUATION
#--------------------------------------------------------------------
_punct = r'… …… , : ; \! \? ¿ ؟ ¡ \( \) \[ \] \{ \} < > _ # \* & 。 ？ ！ ， 、 ； ： ～ · । ، ؛ ٪'
PUNCT  = split_chars(_punct)

#--------------------------------------------------------------------
# QUOTES
#--------------------------------------------------------------------
_quotes = r'\' \'\' " ” “ `` ` ‘ ´ ‘‘ ’’ ‚ , „ » « 「 」 『 』 （ ） 〔 〕 【 】 《 》 〈 〉'
QUOTES  = split_chars(_quotes)

#--------------------------------------------------------------------
# HYPHENS
#--------------------------------------------------------------------
_hyphens = '- – — -- --- —— ~'
HYPHENS  = split_chars(_hyphens)

#--------------------------------------------------------------------
# ICONS
#--------------------------------------------------------------------
_other_symbols = r'[\p{So}]'
ICONS  = [_other_symbols]

import pandas as pd

class pos:
    
    def __init__(self, text):
        
        self.text        = text
        self.clean_text  = ''
        self.doc         = nlp(text) 
        self.features    = pd.DataFrame()


    def process(self):


        def like_num(text):
            text = text.replace(',', '').replace('.', '')
            if text.isdigit():
                return True
            if text.count('/') == 1:
                num, denom = text.split('/')
                if num.isdigit() and denom.isdigit():
                    return True
            if text in NUM_WORDS:
                return True
            return False

        #------------------------------------------------------------------------
        # cast the data to a spacy type
        #------------------------------------------------------------------------
        doc   = nlp(self.text)
        sents = list(doc.sents)

        #------------------------------------------------------------------------
        # Compute Features.
        #------------------------------------------------------------------------
        
        # SENTENCE NUMBER
        # Convert doc to list of lists.
        sent_tokens = []
        for sent in sents:
            toks = [str(tok) for tok in sent]
            sent_tokens.append(toks)
        
        # Get the sentence number:
        sentence_num, tokens = [], []
        for i,sent in enumerate(sent_tokens):
            for word in sent:
                sentence_num.append(i)
                tokens.append(word)
            
        # TOKEN CHILDREN
        child_list = []
        for token in self.doc:
            children = []
            for child in token.children:
                children += [child]
            child_list.append(children)

        children = child_list 

        # IS WHITESPACE
        is_whitespace = [True if str(token) in WHITESPACE else False for token in self.doc]
        
        # IS STOPWORD
        is_stop       = [True if str(token) in STOPLIST else False for token in self.doc]
        
        # IS SYMBOL
        is_symbol     = [True if str(token) in SYMBOLS else False for token in self.doc]
        
        # IS ALPHABETICAL STRING
        is_alpha      = [token.is_alpha for token in self.doc]

        # IS NUMERIC STRING
        is_numeric    = [like_num(str(token)) for token in self.doc]

        # IS UNITS
        is_units = [True if str(token) in UNITS else False for token in self.doc]
        
        # IS CURRENCY
        is_currency = [True if str(token) in CURRENCY else False for token in self.doc]

        # IS QUOTES
        is_quotes = [True if str(token) in QUOTES else False for token in self.doc]

        # IS PUNCT
        is_punct = [True if str(token) in PUNCT else False for token in self.doc]

        # IS HYPHENS
        is_hyphens = [True if str(token) in HYPHENS else False for token in self.doc]

        # IS ICONS
        is_icons = [True if str(token) in ICONS else False for token in self.doc]
        
        # TAGS
        tags          = [token.tag_ for token in self.doc]
        
        # DEPENDENCIES
        dependencies  = [token.dep_ for token in self.doc]
        
        # PARTS OF SPEECH
        pos           = [token.pos_ for token in self.doc] 
        
        # LEMMA
        lemma         = [token.lemma_ for token in self.doc]  
        
        # WORD LENGTH
        length        = [len(token.shape_) for token in self.doc] 
        
        # PROBABILITIES
        prob          = [token.prob for token in self.doc]
        
        # BROWNIAN CLUSTER
        cluster       = [token.cluster for token in self.doc]
        
        # ENTITIY
        ents          = [e.ent_type_ for e in self.doc]







        #------------------------------------------------------------
        # Assign features
        #------------------------------------------------------------
        self.features    = pd.DataFrame({'tokens': tokens,
                                         'sentence_num': sentence_num,
                                         'tags': tags,
                                         'children': children,
                                         'dependencies': dependencies,
                                         'pos': pos,
                                         'lemma': lemma,
                                         'is_stop':is_stop,
                                         'is_whitespace': is_whitespace,
                                         'is_symbol': is_symbol,
                                         'length':length,
                                         'is_alpha':is_alpha,
                                         'is_numeric':is_numeric,
                                         'is_units':is_units,
                                         'is_currency':is_currency,
                                         'is_quotes':is_quotes,
                                         'is_punct':is_punct,
                                         'is_hyphens':is_hyphens,
                                         'is_icons':is_icons,
                                         'prob': prob,
                                         'cluster':cluster,
                                         'entity':ents
                                        })