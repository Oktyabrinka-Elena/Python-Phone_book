from os.path 
from create_csv import creating
from write_csv import writing_scv

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
