import model
import model02
import view
#import test_int

def start():
    view.showinfo("Введите данные абонента")
    #while True:
    abonent = view.getNumb("input --> ")
    abon = model02.abonent(abonent)
    #model.dict_book()
    

    result = model.dictions1[abon]

    view.showinfo(result)


