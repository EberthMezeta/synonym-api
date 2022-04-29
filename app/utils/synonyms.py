from nltk.corpus import wordnet
import traceback


class synonyms_generator:

    def get_synonyms(self, word, languaje):
        try:
            results = []
            for syn in wordnet.synsets(word, lang=(languaje)):
                for name in syn.lemma_names(languaje):
                    results.append(name)
            return results
        except BaseException as ex:
            print(traceback.format_exc())
        return []
