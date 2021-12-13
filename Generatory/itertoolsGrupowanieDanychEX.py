import os
import itertools as it


dir = "D:\Coding\Python\Python\Kody nauka"


def scantree(path):
    for i in os.scandir(path):
        if i.is_dir():
            yield i
            yield from scantree(i.path)
        else:
            yield i


for d in scantree(dir):
    print(d)

listing = scantree(dir)

for i in listing:
    if i.is_dir():
        print("DIR", i.path)
    else:
        print("FILE", i.path)


listing = scantree(dir)

listing = sorted(listing, key=lambda x: x.is_dir())

for is_dir, element in it.groupby(listing, key=lambda x: x.is_dir()):
    print("DIR" if is_dir else "FILE", len(list(element)))
