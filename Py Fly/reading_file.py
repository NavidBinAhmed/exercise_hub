'''def count_word_frequency(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!;:?/"\|')
                word_count[word] = word_count.get(word,0)+1

    return word_count


file_path = 'sample.txt'
word_frequency = count_word_frequency(file_path)
print(word_frequency)'''

def count_word_freq(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip(',./<>?";:|\`~!#$%^&*()_-+=')
                word_count[word] = word_count.get(word,0) + 1
    return word_count

# driver code
file_path = 'sample.txt'
# function calling
result = count_word_freq(file_path)
print(result)


'''
output:
{'hello': 1, 'navid': 1, 'how': 1, 'are': 2, 'you': 2, 'doing': 2, 'good': 1}
'''