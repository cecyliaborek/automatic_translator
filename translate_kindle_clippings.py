from parser import Parser
from scrap_dictionary import Translator
import pandas as pd

clippings_parser = Parser('My_Clippings.txt', 'kindle_clippings')

extracted_clippings = clippings_parser.parse_file()

translated_words = []

for word in extracted_clippings:
    word_translator = Translator(word)
    translations = word_translator.translate()
    translated_words.append([word] + translations)

translated_words_df = pd.DataFrame(
    translated_words, columns=['word', 'english definition', 'polish definition'])

print(translated_words_df)
translated_words_df.to_csv('translated_words.csv',
                           sep=',', index=None)
