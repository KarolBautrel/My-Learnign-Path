
text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']


def f(x): return len(x)  # f = lambda x: len(x)


print(list(map(f, text_list)))

print(list(map(lambda x: len(x), text_list)))
