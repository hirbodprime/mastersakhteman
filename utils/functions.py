import os
import locale

def number_seprator(a):
    locale.setlocale(locale.LC_ALL, 'en_US')
    value = a 
    pure_value = locale.format("%d", value, grouping=True)
    return pure_value


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
