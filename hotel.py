def menue_p():
    global order_total
    global another_order
    menue = {
        'Pizza':40,
        'Pasta':50,
        'Burger':60,
        'Chola_chaumin':40,
        'Tea':15,
        'Chana_murai':45
    }
    #Greeating the custumer
    print("Welcome to chamali ko dhava")
    print("Pizza:Rs40\nPasta:50\nBurger:60\nChola_chaumin:40\nTea:15\nChana_murai:45")
    order_total=0
    iteam_1=input("Enter the name of order you want to order= ")
    if iteam_1 in menue:
        order_total+=menue[iteam_1]
        print(f"Your iteam {iteam_1}is added on your order and your bill is:{order_total}")
    else:
        print(f"Your order{iteam_1}is not avalable on our resturent")

    for i in range(10):
        another_order=input("Do you want to order another iteam ?(Yes/No):")
        if another_order=="Yes":
            iteam_2=input("Enter the name of second iteam=")
            if iteam_2 in menue:
                order_total+=menue[iteam_2]
                print(f"Your second iteam{iteam_2}added on order and your toral bill is:{order_total}")
            else:
                print(f"this iteam{iteam_2}is not avalable on our resturent.")
        else:
            print("thenk you for comming our resturent and")
            break
    print(f"The total amount of iteams is{order_total}.")
menue_p()
    