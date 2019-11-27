class HashTable:
    def __init__(self):
        self.hash_table = [None] * 10

    def HashFunction(self, item):
        return item % len(self.hash_table)

    def insert(self, item):
        self.hash_table[self.HashFunction(item)] = item

def main():
    my_Hashtable = HashTable()

    my_Hashtable.insert(20)
    my_Hashtable.insert(17)
    my_Hashtable.insert(23)
    my_Hashtable.insert(30)
    my_Hashtable.insert(14)
    my_Hashtable.insert(66)

    print(my_Hashtable.hash_table)

main()