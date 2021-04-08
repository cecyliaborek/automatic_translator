import requests
from bs4 import BeautifulSoup


class Translator():
    """
    A class to handle translating a word, by scrapping its page at Cambridge dictionary.

    ...

    Attributes
    ----------
    word: str
        word to be translated
    english_definition: str
        english definiotion of a word, scrapped from dictionary
    polish_definition: str
        polish translation of a word, scrapped from dictionary
    word_page: requests.models.Response
        http response from Cambridge Dictionary for given word, used to derive its definition

    Methods
    -------
    get_word_page()
        Gets the response with the word Cambridge page and assigns it to word_page
    get_english_definition()
        Derives english definition from word_page
    get_polish_definition()
        Derives polish translation from word_page
    translate() -> list
        Translates a word and returns its english ang polish definitions in a list 
    """

    def __init__(self, word):
        """
        Args:
            word (str): word to be translated
        """
        self.word = word
        self.english_definition = ""
        self.polish_definition = ""
        self.word_page = None

    def get_word_page(self):
        """Gets the response with the word Cambridge page and assigns it to word_page
        """
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        URL = f'https://dictionary.cambridge.org/dictionary/english-polish/{self.word}'
        self.word_page = requests.get(URL, headers=headers)

    def get_english_definition(self):
        """Derives english definition from word_page
        """
        soup = BeautifulSoup(self.word_page.content, 'html.parser')
        html_definition = soup.find_all('div', class_=['def ddef_d db', 'query'])
        for definition_word in html_definition:
            self.english_definition += definition_word.text + "; "

    def get_polish_definition(self):
        """Derives polish translation from word_page
        """
        soup = BeautifulSoup(self.word_page.content, 'html.parser')
        #definition_block = soup.find_all('div', class_='def-body ddef_b')
        definition_block = soup.find_all('span', class_='trans dtrans dtrans-se')
        for definition_word in definition_block:
            self.polish_definition += definition_word.text.strip() + "; "

    def translate(self):
        """Translates a word and returns its english ang polish definitions in a list

        Returns:
            list: contains eglish definition and polish definition, in that order
        """
        self.get_word_page()
        self.get_english_definition()
        self.get_polish_definition()
        return [self.english_definition, self.polish_definition]


if __name__ == "__main__":
    ablaze_translator = Translator('ablaze')
    print(ablaze_translator.translate())