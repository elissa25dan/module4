string_one = input("Введите строку в нижнем регистре и без пробелов: ")
def polindrom():
    string = string_one[::-1]
    if string == string_one:
        return True
    else:
        return False
print(polindrom())