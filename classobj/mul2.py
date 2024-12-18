from tabulate import tabulate
for i in range(1,11):
    data=[(5,i,5*i)]
    table=tabulate(data,tablefmt="grid")
    print(table)
    