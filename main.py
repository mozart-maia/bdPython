import database as bd


class Prompt():
    def __init__(self):
        database = bd.DataBase()
        while True:
            database.print()
            command = input("> ")
            print(command)
            commands = command.split()
            if commands[0] == "exit":
                break
            if commands[0] == "print":
                database.print_trans()
            if commands[0] == "set":
                try:
                    if database.isTransactionOpen():
                        key = commands[1]
                        value = commands[2]
                        database.add_to_transaction(key, value)
                    else:
                        key = commands[1]
                        value = commands[2]
                        database.set(key, value)
                except IndexError:
                    print("Usage: set <key> <value>")
            if commands[0] == "get":
                try:
                    key = commands[1]
                    result = database.get(key)
                    print(result)
                except IndexError:
                    print("Usage: get <key>")
            if commands[0] == "begin":
                database.start_transaction()
            if commands[0] == "rollback":
                if database.isTransactionOpen():
                    database.rollback()
                else:
                    print("No transaction opened yet")
            if commands[0] == "commit":
                if database.isTransactionOpen():
                    database.commit()
                else:
                    print("No transaction opened yet")

            database.save()


if __name__ == "__main__":
    prompt = Prompt()
