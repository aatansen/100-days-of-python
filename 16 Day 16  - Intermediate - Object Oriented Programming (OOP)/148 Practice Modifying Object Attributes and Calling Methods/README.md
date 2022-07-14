Creating object `table` from `PrettyTable` Class
```
from prettytable import PrettyTable
table = PrettyTable()
```
Creating table column by column:
```
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",
["Pikachu","Squirtle","Charmander"])
table.add_column("Type",
["Electric","Water","Fire"])
table.align = "l"
print(table)
```
Learned:
- How to use `PrettyTable Package` Method and Attribute