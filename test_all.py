import glob
import os

root = os.path.dirname(os.path.abspath(__file__))
years = ['2022']

for year in years:
    for path in sorted(glob.glob(f'{root}/{year}/*')):
        os.chdir(path)
        filepath = os.path.join(path, 'main.py')
        print(filepath)
        exec(open(filepath).read())
        os.chdir(root)
