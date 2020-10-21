
def getDefinitions(define,word):
    """ 
       The function  is to get Definitions
  
       Parameters: 
          define: Object of the Define class 
          word: Meaning of Word to be searched

          
       Returns: 
           definition : A definition list are returned 
    """
    counter=1
    definitions=""
    for i in define:
        message=str(counter)+'. '+i.definition()+'\n'
        definitions=definitions+'\n'+message
        counter=counter+1
    return definitions

def getSynonyms(define,word):
    """ 
       The function  is to get Definitions
  
       Parameters: 
          define: Object of the Define class 
          word: Meaning of Word to be searched

          
       Returns: 
           Synonyms : A Synonym list are returned 
    """
    synonyms=[]
    for i in define:
        for j in i.lemmas():
            synonyms=synonyms+[j.name()]
    synonyms=set(synonyms)
    synonyms=' , '.join(synonyms)
    return synonyms;