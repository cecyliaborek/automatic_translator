import string


class Parser():

    @staticmethod
    def parse_kindle_clippings(kindle_clippings_file):
        parsed_words = []
        punctuation_to_none_table = str.maketrans(
            {key: None for key in string.punctuation})
        try:
            with open(kindle_clippings_file) as clippings:
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
    words = Parser.parse_kindle_clippings('My_Clippings.txt')
    print((words))
