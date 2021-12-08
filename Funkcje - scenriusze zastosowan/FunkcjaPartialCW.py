import requests
import os
import functools


def save_url_file(url, dir, file, msg):

    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://mobilo24.eu/spis'
file = 'spis.html'
#save_url_file(url, dir, file, msg)


SendFileToPython = functools.partial(
    save_url_file, msg="Please wait - the file {} will be downloaded", dir='d:/python')

SendFileToPython(url=url, file=file)
