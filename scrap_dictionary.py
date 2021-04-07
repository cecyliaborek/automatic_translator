import requests
from bs4 import BeautifulSoup


class Translator():

    @staticmethod
    def get_word_page(word):
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        URL = f'https://dictionary.cambridge.org/dictionary/english-polish/{word}'
        word_page = requests.get(URL, headers=headers)
        return word_page

    @staticmethod
    def get_english_definition(word_page):
        english_definition = ""
        soup = BeautifulSoup(word_page.content, 'html.parser')
        html_definition = soup.find_all('div', class_=['def ddef_d db', 'query'])
        for definition_word in html_definition:
            english_definition += definition_word.text + "; "
        return english_definition

    @staticmethod
    def get_polish_definition(word_page):
        polish_definition = ""
        soup = BeautifulSoup(word_page.content, 'html.parser')
        #definition_block = soup.find_all('div', class_='def-body ddef_b')
        definition_block = soup.find_all('span', class_='trans dtrans dtrans-se')
        for definition_word in definition_block:
            polish_definition += definition_word.text.strip() + "; "
        return polish_definition

    @staticmethod
    def translate(word):
        word_page = Translator.get_word_page(word)
        english_definition = Translator.get_english_definition(word_page)
        polish_definition = Translator.get_polish_definition(word_page)
        return [english_definition, polish_definition]


if __name__ == "__main__":
    print(Translator.translate('ablaze'))