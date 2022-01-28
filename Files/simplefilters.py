import os
import random
from basefilter import BaseFilter


class NaiveFilter(BaseFilter):
    def train(self, path_of_dict):
        pass

    def test(self, path_of_emails):
        list_dir = os.listdir(path_of_emails)
        with open(path_of_emails + "/" + self.pred, "w", encoding="utf-8") as f:
            for email in list_dir:
                f.write(email + " OK\n")


class ParanoidFilter(BaseFilter):
    def train(self, path_of_dict):
        pass

    def test(self, path_of_emails):
        list_dir = os.listdir(path_of_emails)
        with open(path_of_emails + "/" + self.pred, "w", encoding="utf-8") as f:
            for email in list_dir:
                f.write(email + " SPAM\n")


class RandomFilter(BaseFilter):
    def train(self, path_of_dict):
        pass

    def test(self, path_of_emails):
        list_dir = os.listdir(path_of_emails)
        random_evaluation = random.choice(["OK", "SPAM"])
        with open(path_of_emails + "/" + self.pred, "w", encoding="utf-8") as f:
            for email in list_dir:
                f.write(email + " " + random_evaluation + "\n")
