from parser import Parser
from scrap_dictionary import Translator
import pandas as pd

parser = Parser()
translator = Translator()

extracted_clippings = parser.parse_kindle_clippings('My_Clippings.txt')

translated_words = []

for word in extracted_clippings:
    translations = translator.translate(word)
    translated_words.append([word] + translations)

translated_words_df = pd.DataFrame(
    translated_words, columns=['word', 'english definition', 'polish definition'])

print(translated_words_df)
translated_words_df.to_csv('translated_words.csv',
                           sep=',', index=None)
