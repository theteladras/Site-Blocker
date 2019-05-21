from datetime import datetime as date


def initialSetup():
    input_not_in_order = True
    while input_not_in_order:
        print("Odaberite nacin redirekcije: \n")
        print("1) ka -> www.google.com \n")
        print("2) ka -> www.github.com \n")
        print("3) ka -> www.codewars.com \n")
        print("4) bez redirekcije \n")
        print("5) unesite zeljenu adresu za redirekciju \n")
        print("0) odustani \n")
        redirect_page = int(input('Unesite broj opciju: '))
        if (redirect_page > 4):
            print("Niste uneli validnu opciju. Pokusajte ponovo.")
        elif (redirect_page == 1):
            redirect = "www.google.com"
            input_not_in_order = False
            return redirect
        elif (redirect_page == 2):
            redirect = "www.github.com"
            input_not_in_order = False
            return redirect
        elif (redirect_page == 3):
            redirect = "www.codewars.com"
            input_not_in_order = False
            return redirect
        elif (redirect_page == 4):
            redirect = "127.0.0.1"
            input_not_in_order = False
            return redirect
        elif (redirect_page == 5):
            input_not_in_order = False
            chosen_url = input('Unesite zeljeni web domen: ')
            redirect = chosen_url
            return redirect
        elif (redirect_page == 0):
            exit()


def hourCheck(start_time, end_time):
    current_time = date.now()
    if start_time < current_time < end_time:
        return True
    else:
        return False
