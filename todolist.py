todolist = []
while True:
    x = input("")
    if x == "add":
        y = input("What to add ")
        todolist.append(y)
    if x == "remove":
        y = input("which item to delete? ")
        todolist.remove(y)
    if x == ("print"):
        print(*todolist, sep="\n")