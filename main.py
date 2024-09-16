from typing import TypedDict

class Entry():
    def __init__(self, key:str, value:int):
        self.key = key
        self.value = value
    
    def getKey(self):
        self.key

    def getValue(self):
        self.value


class bancoDados():
    def __init__(self):
        self.entries = {}
        self.openTransaction = False
        self.list = []

    def set(self, key, value):
        self.entries[key] = value

    def get(self, key):
        try:
            return self.entries[key]
        except KeyError:
            return None

    def start_transaction(self):
        self.openTransaction = True
        self.list = []
        print(1)

    def rollback(self):
        self.openTransaction = False
        self.list = []

    def isTransactionOpen(self):
        return self.openTransaction

    def add_to_transaction(self, key, value):
        result = self.get(key)
        if result:
            self.list.append([key,value])
            print("TRUE", 1)
            
        else:
            self.list.append([key,value])
            print("FALSE", 1)

    def save(self):
        with open("bdPython", "w") as file:
            for key, value in self.entries.items():
                file.write("{}:{}\n".format(key,value))


            

    def commit(self):
        print(self.list)
        for each in self.list:
            self.set(each[0],each[1])

        self.openTransaction = False
        self.list = []

    def print_trans(self):
        print(self.list, self.isTransactionOpen())

    def print(self,):
        print(self.entries)

class Prompt():
    def __init__(self):
        banco = bancoDados()
        while True:      
            banco.print()
            command = input("> ")
            print(command)
            commands =  command.split()
            if commands[0] == "exit!":
                    break
            if commands[0] == "print":
                    banco.print_trans()
            if commands[0] == "set":
                try:
                    if banco.isTransactionOpen():
                        key = commands[1]
                        value = commands[2]
                        banco.add_to_transaction(key, value)
                    else:
                        key = commands[1]
                        value = commands[2]
                        banco.set(key, value)
                except IndexError:
                    print("Usage: set <key> <value>")
            if commands[0] ==  "get":
                try:
                    key = commands[1]
                    result = banco.get(key)
                    print(result)
                except IndexError:
                    print("Usage: get <key> <value>")
            if commands[0] == "begin":
                banco.start_transaction()
            if commands[0] == "rollback":
                if banco.isTransactionOpen():
                    banco.rollback()
                else:
                    print("No transaction opened yet")
            if commands[0] == "commit":
                if banco.isTransactionOpen():   
                    banco.commit()
                else:
                    print("No transaction opened yet")

            banco.save()

            
if __name__ == "__main__":
    prompt = Prompt()
