from utils import read_classification_from_file
from confmat import BinaryConfusionMatrix


def quality_score(tp, tn, fp, fn):
    tp = int(tp)
    tn = int(tn)
    fp = int(fp)
    fn = int(fn)
    quality = (tp + tn) / (tp + tn + 10*fp + fn)
    return quality


def compute_quality_for_corpus(corpus_dir):
    truth = read_classification_from_file(corpus_dir + '/!truth.txt')
    pred = read_classification_from_file(corpus_dir + '/!prediction.txt')
    matrix = BinaryConfusionMatrix('SPAM', 'OK')
    matrix.compute_from_dicts(truth, pred)
    matrix1 = matrix.as_dict()
    return quality_score(float(matrix1['tp']), float(matrix1['tn']), float(matrix1['fp']), float(matrix1['fn']))
