from array import array
from hmac import new
import xlrd
# location = ('ESC glotext.xlsx', on_demand=True)
workbook = xlrd.open_workbook('glotext.xls')
# shl = workbook.get_sheets()
sh1 = workbook.sheet_by_name('Sheet1')
ar = sh1.col_values(3)
# print(len(ar))

# print(int(ar[-2]))

# # print(ar)
newlist = []
ar.pop(0)
print(len(ar))
file = open("numbers.txt", "a")
for i in ar:
    if i!= '':
        i = int(i)
        i = str(i)
        # print(i)
        i = i.zfill(11)
        # print(i)
        # i = int(i)
        newlist.append(i)
        file.write(i + ", ")
file.close()        
# print(newlist) 

# with open("numbers.txt", "w") as f:
#     f.write(newlist)
#     f.close()

# s = '9090909090'
# s.zfill(11)
# print(s)


