"""
As corrotinas não são executadas quando as chamamos diretamente. É criado um objeto
de co-rotina que pode ser executado posteriormente. Para executar precisamos executá-las
explicitamente em loop de eventos...
"""


async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(1)
coroutine_result = coroutine_add_one(1)

print(f"Function resul is {function_result} and the types is {type(function_result)}")
print(f"Coroutine resul is {function_result} and the types is {type(coroutine_result)}")
