import re

def main():
    finder('RIP.txt', 'essay.txt')

class finder:
    def __init__(self, RIP, essay):
        self.RIP = RIP
        self.essay = essay

        self.read_RIP()
        self.read_essay()

        self.search()

        print(self)

    def __str__(self):
        endstring = ''
        for word, occurances in self.bad_words.items():
            if not occurances == 0:
                endstring += f'\n{word:<15}{occurances}'
        return endstring

    def read_RIP(self):
        with open(self.RIP, 'r') as RIP_words:
            bad_words_list = re.split(r'\W+', RIP_words.read())
            self.bad_words = {}
            for word in bad_words_list:
                if not word == '':
                    self.bad_words[word.lower()] = 0
            
    def read_essay(self):
        with open(self.essay, 'r') as essay_body:
            self.essay_words = re.split(r'\W+', essay_body.read())

    def search(self):
        for word in self.essay_words:
            if word.lower() in self.bad_words:
                self.bad_words[word.lower()] += 1

if __name__ == '__main__':
    main()
