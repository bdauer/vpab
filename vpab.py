from bin import terminterface

def main():

    main_is_active = False

    while True:
        print("start of while loop")
        
        if main_is_active == False:
            active_menu = terminterface.main_menu
            main_is_active = True
        terminterface.print_menu(active_menu)
        active_menu = terminterface.menu_selection(active_menu)
        print(active_menu)
        print("end of while loop")




if __name__ == "__main__":
    main()
