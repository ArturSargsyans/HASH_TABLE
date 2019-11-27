import json

class Chapter:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories


class HashTable:
    def __init__(self):
        self.size = 0
        self.chapters = []
        self.table = []

    def LoadChapters(self):
        with open("data.json") as data_file:
            chapters = json.load(data_file)
            for key in chapters:
                tmpchapter = Chapter(key, chapters[key])
                self.chapters.append(tmpchapter)
                self.size = self.size + 1

    def HashFunction(self, key):
        return key % self.size

    def Insert(self):
        self.table = [None] * self.size
        for chapter in self.chapters:
            number = 0
            for letter in chapter.name:
                number = (number + ord(letter))

            self.table[self.HashFunction(number)] = chapter

        print(self.table)


def main():
    table = HashTable()
    table.LoadChapters()
    table.Insert()

main()