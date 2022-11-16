import model
import view
#import test_int

def start():
    view.showinfo("Введите данные абонента")
    #while True:
    abonent = view.getNumb("input --> ")

    #model.dict_book()
    

    result = model.dictions1[abonent]

    view.showinfo(result)
