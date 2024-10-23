wordsearchcsv = open('wordsearch.csv')
wordsearch = list()
unacceptable_characters = ['\n', ',', ' ']
for lineid, line in enumerate(wordsearchcsv):
    wordsearch.append(list())
    for character in line:
        if character not in unacceptable_characters:
            wordsearch[lineid].append(character.strip())



wordlisttxt = open('wordlist.txt')
wordlist = []
for word in wordlisttxt:
    wordlist.append(word.strip())

print(wordsearch)
print(wordlist)

class Line:
    def __init__(self, line, line_number):
        self.line = line
        self.line_number = line_number

class Coordinate:
    def __init__(self, position, x, y):
        self.position = position
        self.x = x
        self.y = y

class Letter:    
    def __init__(self, position: (int, int), character: str):
        self.location = Coordinate(
                                   position,
                                   position[0],
                                   position[1]
                               )
        self.character = character


def scan_for_instances_of_letter(wordsearch: list, letter: str) -> str:
    positions_to_scan = (-1, 0, 1)
    instances_of_letter = list()
    for line_number, line in enumerate(wordseach):
        instances_in_line = scan_line(
                                      Line(line, line_number),
                                      letter
                                  )
        for instance in instances_in_line:
            instances_of_letter.append(instance)

        
def search_for_word(wordsearch: list, word: str) -> list:
    instances = []
    for letter in word:
        scan_for_instances_of_letter #TODO: make this do someting
        

    
def main():
    for word in wordlist:
        search_for_word(wordsearch, word)


if __name__ == "__main__":
    main()
