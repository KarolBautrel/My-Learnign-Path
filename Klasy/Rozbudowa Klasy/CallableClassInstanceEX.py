class NoDuplicates:

    def __init__(self, list):
        self.list = []

    def __call__(self, new_items):
        for i in new_items:
            if not i in self.list:
                self.list.append(i)


my_no_dup_list = NoDuplicates([])

my_no_dup_list(['keyboard', 'mouse'])

print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'pendrive'])
print(my_no_dup_list.list)
