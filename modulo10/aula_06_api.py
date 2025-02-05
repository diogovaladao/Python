import requests
from pprint import pprint

#GET
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

#GET com id
resultado_get_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_id.json())

#POST - criar novo recurso
nova_tarefa = {'completed': False,
 'title': 'pegar moto',
 'userId': 1}
result_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_tarefa)
#pprint(result_post.json())

#PUT - alterar um recurso existente
tarefa_alterada = {'completed': False,
 'title': 'pegar carro',
 'userId': 1}
result_put = requests.put('https://jsonplaceholder.typicode.com/todos/200', tarefa_alterada)
#pprint(result_put.json())

#DELETE - excluir recurso
result_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
print(result_delete.json())