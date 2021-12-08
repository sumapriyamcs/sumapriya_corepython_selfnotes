with open('add.text', 'w') as opened_file:
    opened_file.write('Hola!')
file = open('add.text', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

#implementing a context manager as generator
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

