import string


class Parser():

    def __init__(self, file, file_type):
        self.file = file
        self.file_type = file_type

    def parse_file(self):
        if self.file_type == 'kindle_clippings':
            return self.parse_kindle_clippings()
        else:
            print('No parsing for given file type')

    def parse_kindle_clippings(self):
        parsed_words = []
        punctuation_to_none_table = str.maketrans(
            {key: None for key in string.punctuation})
        try:
            with open(self.file) as clippings:
                clippings_lines = clippings.readlines()
                for line in clippings_lines[3::5]:
                    line_words = line.split()
                    if len(line_words) != 1:
                        continue
                    found_word = line_words[0].translate(
                        punctuation_to_none_table).lower()
                    parsed_words.append(found_word)
            return parsed_words
        except Exception as e:
            print('problems with parsing file: ', e)


if __name__ == "__main__":
    clippings_parser = Parser('My_Clippings.txt', 'kindle_clippings')
    words = clippings_parser.parse_file()
    print((words))
