text = "Hello there, I'm Sabbir Ahmed, a passionate and curious individual from Dhaka, Bangladesh. As a Computer Science and Engineering student at Green University of Bangladesh, I am constantly seeking new opportunities to expand my knowledge and skills in the software engineering and data science field."

words = text.split()

def word_count(words):
    word_count = {}  
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Directly assign the result of word_count to text_dict
text_dict = word_count(words)


for i in text_dict:
    print(i, text_dict[i])

