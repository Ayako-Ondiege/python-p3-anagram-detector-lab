# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        sorted_original = sorted(self.word.lower())  # Normalize to lowercase
        matches = []

        for candidate in word_list:
            if candidate.lower() != self.word.lower() and sorted(candidate.lower()) == sorted_original:
                matches.append(candidate)

        return matches
