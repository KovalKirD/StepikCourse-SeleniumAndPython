# Задание: составные сообщения об ошибках и поиск подстроки
string1 = 'fulltext'
string2 = 'some_value'

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, \
    f"expected '{substring}' to be substring of '{full_string}'"

test_substring(string1, string2)
print(f'"{string1}" входит в "{string2}"')
