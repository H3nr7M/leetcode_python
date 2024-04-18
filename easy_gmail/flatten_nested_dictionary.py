'''
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
'''

def flatten_dict(dic, parent_key='', sep='.'):
    items = []
    for k, v in dic.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict): #saber si v es un diccionario
            flattened_dict = flatten_dict(v, new_key, sep=sep)
            # Esto devuelve un diccionario que representa el diccionario v aplanado.
            flattened_items = flattened_dict.items()
            # Llama al método .items() en este diccionario aplanado para obtener una lista de tuplas (clave, valor).
            # Extiende la lista de items actual con estas tuplas.
            items.extend(flattened_items)
        else:
            items.append((new_key, v))
    return dict(items)

# Diccionario de ejemplo
nested_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

# Aplicar la función para aplanar el diccionario
flattened_dict = flatten_dict(nested_dict)

# Imprimir el diccionario aplanado
print(flattened_dict)
