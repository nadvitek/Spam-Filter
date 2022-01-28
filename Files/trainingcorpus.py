from corpus import Corpus
from utils import read_classification_from_file
import os


class TrainingCorpus(Corpus):
    def __init__(self, path):
        self.path = path
        self.ham_word_list = list()
        self.spam_word_list = list()
        self.dict_of_words = {"A": [1, 1]}

    def get_class(self, filename):
        dic_of_files = read_classification_from_file(self.path+"/!truth.txt")
        return dic_of_files[filename]

    def is_ham(self, filename):
        if self.get_class(filename) == "OK":
            return True
        else:
            return False

    def is_spam(self, filename):
        if self.get_class(filename) == "SPAM":
            return True
        else:
            return False

    def spams(self):
        dir_list = os.listdir(self.path)
        for file in dir_list:
            if file[0] == "!" or self.is_spam(file) is False:
                continue
            with open(self.path+"/"+file, "rt", encoding="utf-8") as f:
                body = f.read()
            yield file, body

    def hams(self):
        dir_list = os.listdir(self.path)
        for file in dir_list:
            if file[0] == "!" or self.is_ham(file) is False:
                continue
            with open(self.path+"/"+file, "rt", encoding="utf-8") as f:
                body = f.read()
            yield file, body

    def score_for_spam_and_ham_words(self):
        for fname, body in self.hams():
            list_of_words = body.split()
            for word in list_of_words:
                if word not in self.dict_of_words:
                    self.dict_of_words[word] = [1, 1]
                self.dict_of_words[word][0] += 1
        for fname, body in self.spams():
            list_of_words = body.split()
            for word in list_of_words:
                if word not in self.dict_of_words:
                    self.dict_of_words[word] = [1, 1]
                self.dict_of_words[word][1] += 1

    def fulling_lists(self):
        self.score_for_spam_and_ham_words()
        for word in self.dict_of_words:
            if (self.dict_of_words[word][0]/self.dict_of_words[word][1]) > 13:
                self.ham_word_list.append(word)
            elif (self.dict_of_words[word][1]/self.dict_of_words[word][0]) > 103:
                self.spam_word_list.append(word)

    def getting_ham_and_spam_word_list(self):
        self.fulling_lists()
        self.lowering_words()
        return [self.ham_word_list, self.spam_word_list]

    def lowering_words(self):
        for i in range(len(self.ham_word_list)):
            self.ham_word_list[i] = self.ham_word_list[i].lower()
        for i in range(len(self.spam_word_list)):
            self.spam_word_list[i] = self.spam_word_list[i].lower()


if __name__ == "__main__":
    a = TrainingCorpus(os.path.abspath("2"))
    print(a.getting_ham_and_spam_word_list()[0])
    for i in range(10):
        print("")
    print(a.getting_ham_and_spam_word_list()[1])
