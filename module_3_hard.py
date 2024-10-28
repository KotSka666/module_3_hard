data_structure = [
                  [1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6,{'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

def calculate_structure_sum(data_structure,*args):
    total_sum = 0
    for i in data_structure:
        if isinstance(i, int):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            total_sum += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, str):
                    total_sum += len(key)
                else:
                    total_sum += key

                if isinstance(value, int):
                    total_sum += value
                elif isinstance(value, str):
                    total_sum += len(value)
                elif isinstance(value, list) or isinstance(value, tuple):
                    total_sum += calculate_structure_sum(value)
    return total_sum


result = calculate_structure_sum(data_structure)
print(result)
