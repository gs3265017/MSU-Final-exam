# 1 Задание
# Строки в Питоне сравниваются на основании значений символов.
# Требуется создать класс RealString в котором реализовать сравнение строк по количеству входящих в них символов.
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
# Реализовать метод isPalindrom(), возвращающий True или False в зависимости от того, является ли слово палиндромом.

# 2 Задание:
# Реализовать класс Real_text. Элементом которого является список из элементов RealString.
# Реализовать в этом классе конструктор чтения слов из файла.
# Реализовать метод + сумма двух экземпляров, т.е.Real_text = Real_text + Real_text.
# Реализовать метод сохранения Real_text в файл. Не забываем слова сохранять через пробел.


class RealString(object):

    input_string = None

    def __init__(self, input_string):
        self.input_string = str(input_string)

    def isPalindrom(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return ((str(self.input_string)) == (str(self.input_string[::-1]))) or ((str(other)) == (str(other[::-1])))

    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        print("method eq")
        return len(self.input_string) == len(other.input_string)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.input_string) < len(other.input_string)

    def __le__(self, other):
        return self == other or self < other


class Real_Text(object):

    def __init__(self, input_file=open('input.txt', 'r', encoding='utf-8')):
        self.input_file = input_file
        x = input_file.read()
        # try:
        #     file = open(self.input_file)
        #     file.read()
        # except IOError:
        #     print('Cannot read the file!')
        # string = file.read()
        # temp_list = string.split('\n')

    # def sum(self, other: object):
    #     if isinstance(other, list):
    #         return RealString(self.a + [other])

    def new_file(self, string_list=open('output.txt', 'w', encoding='utf-8')):
        f_1 = string_list
        f_1.writelines(line + ' ' for line in string_list)
        f_1.close()


string_1 = RealString('Съешь еще этих мягких французских булок да выпей чаю')
string_2 = RealString('Съешь еще этих мягких')
string_3 = 'еще этих мягких'
string_4 = [22, 1242, 23]
print(string_1 < string_4)
print(string_1 >= string_2)
print(string_1 == string_3)
print(string_1.isPalindrom())
print(string_2.isPalindrom())
print(string_3.isPalindrom())
print(string_4.isPalindrom())
