from prettytable import PrettyTable

# creating an object
table = PrettyTable()
print(table)

# object methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# object attributes
table.align = "c"

print(table)


