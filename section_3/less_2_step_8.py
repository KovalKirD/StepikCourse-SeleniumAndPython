# Задание: составные сообщения об ошибках
expected = 8
actual = 11
# ваша реализация, напишите assert и сообщение об ошибке
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
    f'expected {expected_result}, got {actual_result}'

test_input_text(expected, actual)
print('Значения равны')
