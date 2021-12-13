import os
import zipfile
import requests
import contextlib


class FileFromWeb:
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        self.response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(self.response.content)
        return self

    def __exit__(self, exc_type, exc_value, trace):
        pass


with contextlib.closing(FileFromWeb("https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip", r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\eurofrex.zip")) as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(
            'D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager')
        z.extract(a_file, '.', None)
