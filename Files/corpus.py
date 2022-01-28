import os


class Corpus:
    def __init__(self, path):
        self.path = path

    def emails(self):
        dir_list = os.listdir(self.path)
        for file in dir_list:
            if file[0] == "!":
                continue
            with open(self.path+"/"+file, "rt", encoding="utf-8") as f:
                body = f.read()
            yield [file, body]


if __name__ == "__main__":
    corpus = Corpus()
    count = 0
    for fname, body in corpus.emails():
        print(fname)
        print(body)
        print('-------------------------')
        count += 1
    print('Finished: ', count, 'files processed.')
