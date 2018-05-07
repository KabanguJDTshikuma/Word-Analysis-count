import re
from nltk.tokenize import word_tokenize


import re
def multiwordReplace(text_, replace_dict):
    '''
    Replace words in a text that match a key in replace_dict
    with the associated value, return the modified text.
    Only whole words are replaced.
    Note that replacement is case sensitive, but attached
    quotes and punctuation marks are neutral.
    '''
    rc = re.compile(r"[A-Za-z_]\w*")
    def translate(match):
        word = match.group(0)
        return replace_dict.get(word, word)
    return rc.sub(translate, text_)

    

def Reverse_(list_):
    """
    Take a list and reverse the variable
    """
    return [ele for ele in reversed(list_)]
     

def countWords(text_):
    """
    Take a paragraph, split it and clean it. call multiwordReplace() module and return the text with the 
    most commonly occurring word appearing in dark green, second most commonly occurring word in 
    light green, third most in blue, fourth most in orange, fifth most in red and then all the rest of 
    the words in black.
    """
    # split a text into words
    tokens = word_tokenize(text_)
    
    # remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]

    #Counting the occurance of words
    word_dict = {}
    for word in words:
        if len(word)>1 and word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # Selecting values only and reverse the list.     
    values_list = sorted(set(word_dict.values()))
    values_list = Reverse_(values_list)
    list_rever = values_list[:5]

    # creating a dict of colors
    color_dict  = {}
    color = [('<span class="dgText">', '</span>'), 
             ('<span class="lightgreen">', '</span>'),
             ('<span class="blueText">', '</span>'), 
             ('<span class="orangeText">', '</span>'),
             ('<span class="redText">', '</span>')]
    for i, j in enumerate(list_rever):
        color_dict [j] = color[i]

    #creating a dictionary of words with css color
    dict_c = {}
    for key, value in word_dict.items():
        if len(key)>1 and value in list_rever:
            dict_c[key] =  color_dict[value][0] + key + color_dict[value][1]
           
    text_ = multiwordReplace(text_, dict_c)

    return text_
    