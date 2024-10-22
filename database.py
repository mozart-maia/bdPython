import os

class DataBase():
    def __init__(self):
        self.entries = self.open()
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
            
    def open(self):
        dic = {}
        
        if not os.path.exists("./bdPython"): 
            with open("bdPython", "w") as file:
                file.write("")
        
        with open("bdPython", "r") as file:
            lines = file.readlines()
            for l in lines:
                key, value = l.split(":")
                dic[key] = value[0:-1]
        
        return dic

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