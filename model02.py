def abonent(abonent):
    lst = abonent.lower().split('.')
    return ''.join(lst)

print (abonent('Василий А. М.'))
