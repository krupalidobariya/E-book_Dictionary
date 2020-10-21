# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:46:16 2020
g
@author: krupali,priyal
"""
from nltk.corpus import wordnet
import time
import pyperclip
import util_support as util
import library_support as library


oldWord=""
TITLE = "E-Book Dictionary"
while(True):
    time.sleep(2)
    newWord=pyperclip.paste()
    if(newWord!=oldWord):
        print(pyperclip.paste())
        define=wordnet.synsets(newWord)
        synonyms = library.getSynonyms(define,newWord)
        definitions = library.getDefinitions(define,newWord)
        message='Selected word is:' + newWord +'\n DEFINITIONS:: \n'+ definitions +'\n\n SYNONYMS ARE AS FOLLOW ::  \n\n'+synonyms+'\nwith title '+ newWord
        util.showpopUpWindow(TITLE,message)
        oldWord=pyperclip.paste()
