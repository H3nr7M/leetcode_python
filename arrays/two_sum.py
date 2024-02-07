'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

def two_sum(nums, target):
    # Crear un diccionario para almacenar los índices de los números ya vistos
    num_indices = {}

    # Iterar sobre el array
    for i, num in enumerate(nums):
        complemento = target - num
        # Verificar si el complemento está en el diccionario
        if complemento in num_indices:
            # Si encontrado, devolver los índices de los dos números
            return [num_indices[complemento], i]
        # Almacenar el índice del número actual en el diccionario
        num_indices[num] = i

    # Si no se encuentra ninguna pareja que sume al objetivo
    return None

# Ejemplo de uso:
nums_example = [2, 7, 11, 15]
target_example = 9
result = two_sum(nums_example, target_example)
print(result)  # Output: [0, 1] (ya que nums[0] + nums[1] = 2 + 7 = 9)
