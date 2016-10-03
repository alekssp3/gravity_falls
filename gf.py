import string

debug_mode = True


class GF:
    def __init__(self, text='', dictionary='us.dic'):
        self.text = text
        self.alphabet = string.ascii_uppercase
        self.alfabet_from_text = self.get_alphabet_from_text(self.text)
        self.upper_map = self.get_case_list()
        self.upper_map_hash = self.get_hash_from_list(self.upper_map)
        self.dictionary = open(dictionary, 'r').readlines()

    def set(self, text=''):
        self.text = text

    def get(self):
        if debug_mode:
            print('get', end=' ')
        return self.text

    def get_case_list(self):
        if debug_mode:
            print('get-case-list', end=' ')
        temp_list = []
        for char in self.text:
            if char.isupper():
                temp_list.append(1)
            else:
                temp_list.append(0)
        return temp_list

    def get_hash_from_list(self, l):
        if len(l) > 0:
            return hex(int('0b'+''.join([str(i) for i in l]), 2))
        else:
            return hex(0)

    def get_alphabet_from_text(self, text):
        # temp = []
        # for i in text:
        #     if i.isalpha() and i not in temp:
        #         temp.append(i)
        return ''.join(set(text))

    def similarity(self, phrase=''):
        count = 0
        if len(phrase) > 0:
            list_words = phrase.split()
        else:
            list_words = self.text.split()
        for i in list_words:
            if i.lower()+'\n' in self.dictionary:
                count += 1
        return count / len(list_words)

    def similarity_seq(self, seq, quality=0.85):
        for i in seq:
            res = self.similarity(i)
            if res > quality:
                print(i, res)


class Caesar(GF):
    def decode(self, shift=3):
        temp = ''
        for ch in self.text:
            if ch.upper() in self.alphabet:
                index_in_alphabet = self.alphabet.index(ch.upper())
                if index_in_alphabet > -1:
                    temp += self.alphabet[(index_in_alphabet+shift) %
                                          len(self.alphabet)]
            else:
                temp += ch
        return temp

    def crack(self):
        temp = []
        for i in range(len(self.alphabet)):
            temp.append(self.decode(i))
        return temp


def debug():
    gf = GF('Simple test text')
    print(gf.alphabet)
    print(gf.alfabet_from_text)
    print(gf.get())
    print(gf.upper_map)
    print(gf.upper_map_hash)
    # c = gf.caesar()
    # print(c)
    # print(GF(c).caesar(-3))

    c = Caesar(gf.text)
    unc = Caesar(c.text)
    print(c.decode())
    print(unc.decode(-3))
    print('-'*10)
    print(c.crack())


class Dictionary:
    def __init__(self):
        self.dicts = {}
        self.auto_load(self.find_dicts().remove('ru'))

    def find_dicts(self, dict_type='.dic'):
        dict_list = []
        import os
        for i in os.listdir('.'):
            if os.path.isfile(i) and i.endswith(dict_type):
                dict_list.append(i)
        return dict_list

    def auto_load(self, dict_list):
        for i in dict_list:
            self.dicts[i.split('.')[0]] = open(i, 'r').readlines()


if __name__ == '__main__':
    debug()
else:
    debug()
