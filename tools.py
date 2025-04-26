def simple_calculator(query: str) -> str:
    try:
        result = eval(query)
        return str(result)
    except Exception as err:
        return f'Ошибка в вычислении: {str(err)}'


def fake_search(query: str) -> str:
    return f'Представим что мы погуглили и нашли ответ на "{query}"'

