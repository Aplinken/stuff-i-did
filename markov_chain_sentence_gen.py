import numpy as np

#Note: You can put anything you want the program to use in info.txt, remember to feed it a lot of info as feeding it-
# small amounts will result in repetetive sentences/phrases etc.

text = open('info.txt', encoding='utf8').read()
words = text.split() #split the text file into a list of words

def make_pairs(words):
	for i in range(len(words)-1):
		yield(words[i],words[i+1]) #will make pairs of words accordingly

pairs = make_pairs(words)
words_dict = {}

for word_1, word_2 in pairs:
	if word_1 in words_dict.keys():
		words_dict[word_1].append(word_2)
	else:
		words_dict[word_1] = [word_2] #adds the pairs in words_dict as keys and values

first_word = np.random.choice(words)

while first_word.islower():
	first_word = np.random.choice(words) #first word will always be a word that starts with capitals

chain = [first_word]
n_words = int(input('Type the amount of words you want as the result(int): '))

for i in range(n_words):
	chain.append(np.random.choice(words_dict[chain[-1]])) #the chain
	
print(' '.join(chain)) #turn the list into string and print it