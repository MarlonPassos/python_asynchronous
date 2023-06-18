# I/O-bound and CPU-bound operation

from pathlib import Path
import requests

"""
Primeiro, fazemos uma solicitacao vinculada a I/O para baixar o conteudo de https://jsonplaceholder.typicode.com/users. 
Assim que tivermos a resposta, executamos um loop vinculado a CPU para formatar os cabecalhos
da resposta e transforma-los em um string separada por novas linhas.
Em seguda, abrimos um arquivo e escrevemos a string nesse arquivo, ambas operacoes vinculadas
a I/O.

I/O-bound e CPU-bound geralmente vivem lado a lado.
"""

response = requests.get("https://jsonplaceholder.typicode.com/users")  # io-bound
items = response.headers.items()
headers = [f"{key}: {header}" for key, header in items]  # io-cpu
formatted_headers = "\n".join(headers)  # io-bound

file_path = Path("./results/headers.txt")

with file_path.open(mode="w") as file:  # io-bound
    file.write(formatted_headers)
