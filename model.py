
dictions1 = {
    'иванов иван иванович' : '88883883826',
    'васильев василий алибобаевич' : '33332454567',
    'петров петр петрович' : '22226789879',
}

def antidictions(dictions):
    return {v:k for k, v in dictions.items()}

antidict = antidictions(dictions1)

#antidictions = dict(zip(dictions.values(), dictions.keys()))