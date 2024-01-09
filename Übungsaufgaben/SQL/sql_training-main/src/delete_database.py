"""remove test.db"""
from os import remove as os_remove

try:
    os_remove("./test.db")
    print("DB deleted!")
except FileNotFoundError:
    print("DB not Found.")
