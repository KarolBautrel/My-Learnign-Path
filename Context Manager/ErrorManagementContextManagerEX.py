import os
import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        # download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError:
            print("File not found")
            return True
        if exc_type == KeyError:
            print("KEy error")
            return True
        else:
            return False


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\eurofrex.zip') as f:

    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(
            'D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager')
        z.extract(a_file, '.', None)
