class BinaryConfusionMatrix:
    def __init__(self, pos_tag="SPAM", neg_tag="OK"):
        self.pos = pos_tag
        self.neg = neg_tag
        self.tp = 0
        self.tn = 0
        self.fp = 0
        self.fn = 0

    def as_dict(self):
        dict_of_matrix = dict()
        dict_of_matrix["tp"] = self.tp
        dict_of_matrix["tn"] = self.tn
        dict_of_matrix["fp"] = self.fp
        dict_of_matrix["fn"] = self.fn
        return dict_of_matrix

    def update(self, truth, prediction):
        if truth == self.pos and prediction == self.pos:
            self.tp += 1
        elif truth == self.neg and prediction == self.neg:
            self.tn += 1
        elif truth == self.neg and prediction == self.pos:
            self.fp += 1
        elif truth == self.pos and prediction == self.neg:
            self.fn += 1
        else:
            raise ValueError

    def compute_from_dicts(self, truth_dict, pred_dict):
        for email in truth_dict:
            if truth_dict[email] == self.pos and pred_dict[email] == self.pos:
                self.tp += 1
            elif truth_dict[email] == self.neg and pred_dict[email] == self.neg:
                self.tn += 1
            elif truth_dict[email] == self.neg and pred_dict[email] == self.pos:
                self.fp += 1
            elif truth_dict[email] == self.pos and pred_dict[email] == self.neg:
                self.fn += 1


if __name__ == "__main__":
    cm1 = BinaryConfusionMatrix(pos_tag=True, neg_tag=False)
    cm1.as_dict()
    cm1.update(True, True)
    cm1.as_dict()
