


file_name = "fm.txt"
try:
    file  = open(file_name,'a')
    data = file.write('\ntototo')

except Exception as e:
    print(e)
    print('error')
finally:
    file.close()

print('fin')


