import openpyxl

book1 = openpyxl.open("Лист1", read_only=True)
sheet1 = book1.active

for row in range(1, 20):
    print(sheet1[row])

book2 = openpyxl.open("Лист2", read_only=True)
sheet2 = book2.active

for row in range(1, 23):
    print(sheet2[row])

book3 = openpyxl.open("Лист3", read_only=True)
sheet3 = book2.active

for row in range(1, 25):
    print(sheet3[row])

for i in range(1, 20 + 1):
    for j in range(1):
        c = sheet1.cell(row=i, column=j)
        sheet2.cell(row=i, column=j).value = c
        
        
 у меня ничего не получилось с экселем, времени не было, поэтому пришлось делать как-то приблизительно
