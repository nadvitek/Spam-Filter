from corpus import Corpus
from utils import write_classification_to_file
from quality import compute_quality_for_corpus
# Ahoj Vítku :D

# ten seznam slov by možná bylo fajn dát do konstruktoru?
spam_words = ['%', '$', 'free', 'best', 'price', 'cash', 'debt', 'earn', 'extra', 'money', 'credit', 'gift', 'fast', 'investment', 'refund', 'giveaway', 'on sale',
              'low', 'miracle', 'prize', 'profit', 'risk', 'save', 'special', 'now', 'limited', 'click here', 'sign', 'instant', 'exclusive',
              'deal', 'act', 'apply', 'order', 'win', 'congratulations', 'lose', 'weight', ' no ', 'cost', 'fees', 'hidden', 'interest',
              'invest', 'password', 'scam', ' spam ', 'junk', 'security', 'number', 'credit', 'debt', ' ad ', 'bargain', 'cheap', 'discount', 'rates',
              'score', 'warranty', 'highest', 'promo', 'last chance', 'larger', 'limit', 'viagra', 'weight loss', 'no tricks', '!!!', 'millions', 'billions', 'bonus']

ham_words = ["Mr", "Mrs", "Sir", "Madam", "writing", "look forward", "looking forward", "Please", "Thanks", "Best regards", "Kind regards", "Hello", "Regards",
             "Yours faithfully", "Yours sincerely", "Hi", "Cheers", "Sincerely", "Thank you", "...", "Posted", "wrote"]


class MyFilter:
    def probability_of_being_spam(self, path_to_directory_with_emails):
        corpus = Corpus(path_to_directory_with_emails)
        spam_percentage = {}
        for name, body in corpus.emails():
            count = 0
            for spam_word in spam_words:
                if spam_word in body.lower():
                    count += body.lower().count(spam_word)
            spam_percentage[name] = count/(len(body.split())) # tohle taky neni uplne domysleny, pokud budeme do toho seznamu spam slov nejaka slova pridavat, tak to bude hazet cim dal tim vetsi cisla a uz ted to (u jednoho myslim) hazi > 1
            for ham_word in ham_words:
                if ham_word in body.lower():
                    count += body.lower().count(ham_word)
            spam_percentage[name] -= 0.1*count
        return spam_percentage


    def compare_spam_ham_percentage(self, path_to_directory_with_emails):
        prediction = {}
        spam_percentage = self.probability_of_being_spam(path_to_directory_with_emails)
        for email in spam_percentage:
            if spam_percentage[email] > 0.037: # viz random cislo :))) - s timhle cislem to na tech testovacich sadach bylo +- nejlepsi :D ale stejne se sem prida ta cast, kde se zjistuje pravdepodobnost hamovosti, coz to asi dost zmeni
                prediction[email] = 'SPAM'
            else:
                prediction[email] = 'OK'
        return prediction

    def test(self, path_to_directory_with_emails):
        prediction = self.compare_spam_ham_percentage(path_to_directory_with_emails)
        write_classification_to_file(path_to_directory_with_emails + '/!prediction.txt', prediction)

    def train(self, path_to_directory_with_emails):
        pass


if __name__ == "__main__":
    # tady jsem to jen zkousela na tech testovacich sadach, kdyby to fakt bylo kolem 60 %, tak je to podle me pohoda, sice to neni uplne terno, ale nejaky bodiky za to jsou :)
    filtr = MyFilter()
    filtr.test('dataset/1')
    filtr.test('dataset/2')
    print(compute_quality_for_corpus('dataset/1'))
    print(compute_quality_for_corpus('dataset/2'))
