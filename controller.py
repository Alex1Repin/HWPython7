import model
import model02
import view
import test_keys

def start():
    view.showinfo("Введите данные абонента")
    while True:
        abonent = view.getNumb("input --> ")
        abon = model02.abonent(abonent)
        if test_keys.test_k(abon, model.dictions1.keys()):
            result = model.dictions1[abon]
            view.showinfo(result)
        elif test_keys.test_k(abon, model.antidict.keys()):
            result = model.antidict[abon]
            view.showinfo(result)
        else:
            view.showinfo('Нет такого абонента')

    

    

    # result = model.antidict[abon]
    
    # view.showinfo(result)
    


