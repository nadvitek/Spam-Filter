from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix


def quality_score(tp, tn, fp, fn):
    q = (tp+tn)/(tp+tn+10*fp+fn)
    return q


def compute_quality_for_corpus(corpus_dir):
    truth = read_classification_from_file(corpus_dir + "/!truth.txt")
    pred = read_classification_from_file(corpus_dir + "/!prediction.txt")
    m1 = BinaryConfusionMatrix(pos_tag="SPAM", neg_tag="OK")
    m1.compute_from_dicts(truth, pred)
    vals = m1.as_dict()
    quality = quality_score(vals["tp"], vals["tn"], vals["fp"], vals["fn"])
    return quality
