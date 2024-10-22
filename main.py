import database as bd

class Prompt():
    def __init__(self):
        banco = bd.DataBase()
        while True:      
            banco.print()
            command = input("> ")
            print(command)
            commands =  command.split()
            if commands[0] == "exit":
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
