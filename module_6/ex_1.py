'''
Читання та запис у файл.
'''


file = open('test.txt', 'w', encoding='utf-8')  #  кодування потрібно використовувати завжди для windows.
file.write('Hello world!\n')
file.write('Hello Ukraine!\n')
file.writelines(['Hi Bob!\n', 'Hi Dima!\n', 'Test', 'ups\n'])
file.close()

file = open('test.txt', 'r', encoding='utf-8')
# result = file.read()  # читає одразу весь файл у пам’ять
# result = file.readline()  # читає одну строку
result = file.readlines()  # читає всі строки і записує їх у список
print(result)
file.close()