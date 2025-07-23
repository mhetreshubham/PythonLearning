class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        for sentence in sentences:
            words_count = len(sentence.split(" "))
            max_words = max(max_words,words_count)
        return max_words

        
