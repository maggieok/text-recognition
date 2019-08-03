import re
import  pickle


def indexing(filename='char2index.pkl'):

    char2index = {}
    with open('train.list', 'r') as f:
        char2num = {}
        for line in f.readlines():
            chars = line.split('\t', 3)[-1]
            chars = re.sub(r'\s+', '', chars)
            if chars:
                for char in chars:
                    if not char2num.get(char):
                        char2num[char] = 1
                    else:
                        char2num[char] += 1

        sort_char2num = sorted(char2num.items(), key=lambda item: item[1], reverse=True)
        
        for index, (char,num) in enumerate(sort_char2num):
            char2index[char] = index

        with  open(filename, 'wb') as p:
            pickle.dump(char2index, p)


def load_index(filename='char2index.pkl'):
    with open(filename, 'rb') as f:
        char2index = pickle.load(f)

        return char2index


if __name__ == "__main__":

    filename = './char2index.pkl'

    indexing(filename)
    char2index = load_index(filename)
    # print(char2index)

