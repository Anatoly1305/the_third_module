def print_params(a = 1, b = "string", c = True):
    print(a, b, c)

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

# Распаковка параметров:
values_list = ["house", 7, False]
values_dict = {"a" : True, "b" : 10, "c" : "coffee"}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [54.32, "string"]
print_params(*values_list_2, 42)