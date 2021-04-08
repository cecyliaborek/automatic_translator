import requests
from bs4 import BeautifulSoup


class Translator():

    def __init__(self, word):
        self.word = word
        self.english_definition = ""
        self.polish_definition = ""
        self.word_page = None

    def get_word_page(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        URL = f'https://dictionary.cambridge.org/dictionary/english-polish/{self.word}'
        self.word_page = requests.get(URL, headers=headers)

    def get_english_definition(self):
        english_definition = ""
        soup = BeautifulSoup(self.word_page.content, 'html.parser')
        html_definition = soup.find_all('div', class_=['def ddef_d db', 'query'])
        for definition_word in html_definition:
            self.english_definition += definition_word.text + "; "

    def get_polish_definition(self):
        soup = BeautifulSoup(self.word_page.content, 'html.parser')
        #definition_block = soup.find_all('div', class_='def-body ddef_b')
        definition_block = soup.find_all('span', class_='trans dtrans dtrans-se')
        for definition_word in definition_block:
            self.polish_definition += definition_word.text.strip() + "; "

    def translate(self):
        self.get_word_page()
        self.get_english_definition()
        self.get_polish_definition()
        return [self.english_definition, self.polish_definition]


if __name__ == "__main__":
    ablaze_translator = Translator('ablaze')
    print(ablaze_translator.translate())