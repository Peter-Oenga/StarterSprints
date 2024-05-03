def multiple_returns(sentence):
    if sentence != "":
        len_of_str = len(sentence)
        char_first_index = sentence[0]
        return  len_of_str, char_first_index
    else:
        return None
    
sentence = ""
print(multiple_returns(sentence))

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))