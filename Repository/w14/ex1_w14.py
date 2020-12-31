import requests
import zipfile
import os
from pathlib import Path
import re
import shutil


class TextLoader():

    def __init__(self, url):

        r = requests.get(url, allow_redirects=True)
        open('temp.zip', 'wb').write(r.content)

        with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
            zip_ref.extractall('./temp')
        os.remove('temp.zip')
        self.master_path = Path('temp')
        self.files_list = [x for x in list(self.master_path.glob('**/*'))
                           if x.is_file()]
        self.iterable = iter(self.files_list)

    def __len__(self):
        return len(self.files_list)

    def normalize(self, string):
        s = re.sub(r'[^\w\s]', '', string)
        s = re.sub(r'[\n]', ' ', s)
        s = re.sub(r'  ', ' ', s)
        s = s.strip(' ').lower()
        return s

    def __iter__(self):
        return self

    def __next__(self):

        filepath = next(self.iterable)


        with filepath.open('r', encoding='utf-8') as f:
            string_read = f.read()

        with filepath.open('w', encoding='utf-8') as f:
            string_normalized = self.normalize(string_read)
            f.write(string_normalized)
        f = filepath.open('r', encoding='utf-8')
        return f

    def __del__(self):
        shutil.rmtree(self.master_path)

    def __getstate__(self):
        print("I'm being pickled")
        return self.__dict__

    def __setstate__(self, d):
        print("I'm being unpickled with these values: " + repr(d))
        self.__dict__ = d
        self.files_list = [x for x in list(self.master_path.glob('**/*'))
                           if x.is_file()]


if __name__ == '__main__':

    href = 'http://cs.mipt.ru/advanced_python/extra/lab9/sample.zip'
    a = TextLoader(href)


    print(f'Files found: {len(a)}\n----------\n')


    for i in range(102):
        try:
            one = next(a)
            if ((i < 3) | (i > 96)):
                print(one.read()[:50])
                print('---')
        except StopIteration:
            print('There you go')