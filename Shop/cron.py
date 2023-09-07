def num_sep(a):
    print("did it again!")
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US')
    value = a 
    value1 = locale.format("%d", value, grouping=True)
     
    return value1