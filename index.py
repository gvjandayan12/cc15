print("--------------------------------------------------------------------------")
print("WELCOME TO GIRLYBEAR TINDAHAN STORE EATRY HARDWARE HOLLOWBLOCKS CEMETERY!"); print()


class Menu:
    lauya = "Lauya"
    pancitGuisado = "Pancit Guisado"
    baguioBeans = "Baguio Beans"
    rm = "RM"
class FoodPrice:
    lauyaPrice = 100
    pancitGuisadoPrice = 120
    baguioBeansPrice = 25
    rmPrice = 50

menu = Menu(); foodPrice = FoodPrice()

def Ordering():
    while True:
        enterOrder = input("Enter Order : ")

        if enterOrder == menu.lauya:
            print(enterOrder)
            quantity = int(input("Enter Quantity : "))
            result = foodPrice.lauyaPrice * quantity
            print("Total Price : ", result)
            amount = int(input("Amount : "))

            
            if amount >= result:
                print("Change : ", amount - result)
                text = str(input("Dine-in or Take-out? : "))
                print(f"puryagaba customera")
            
            if amount < result:
                print(f"Palit-palit kag {amount} ra imong kwarta?! pauli oi!")
                continue

            break
        elif enterOrder == menu.pancitGuisado:
            print(enterOrder)
            quantity = int(input("Enter Quantity : "))
            result = foodPrice.pancitGuisadoPrice * quantity
            print("Total Price : ", result)
            amount = int(input("Amount : "))


            if amount >= result:
                print("Change : ", amount - result)
                text = str(input("Dine-in or Take-out? : "))
                print(f"puryagaba customera")
            elif amount < result:
                print(f"Palit-palit kag {amount} ra imong kwarta?! pauli oi!")
                continue
            break


        elif enterOrder == menu.baguioBeans:
            print(enterOrder)
            quantity = int(input("Enter Quantity : "))
            result = foodPrice.baguioBeansPrice * quantity
            print("Total Price : ", result)
            amount = int(input("Amoung : "))


            if amount >= result:
                print("Change : ", amount - result)
                text = str(input("Dine-in or Take-out? : "))
                print(f"puryagaba customera")

            elif amount < result:
                print(f"Palit-palit kag {amount} ra imong kwarta?! pauli oi!")
                continue
            break

        
        elif enterOrder == menu.rm:
            print(enterOrder)
            quantity = int(input("Enter Quantity : "))
            result = foodPrice.rmPrice * quantity
            print("Total Price : ", result)
            amount = int(input("Amount : "))
            

            if amount >= result:
                print("Change : ", amount - result)
                text = str(input("Dine-in or Take-out? : "))
                print(f"puryagaba customera")
            
            elif amount < result:
                print(f"Palit-palit kag {amount} ra imong kwarta?! pauli oi!")
                continue
            break
        else:
            print("Order not found! Naniguwang nalang kas kalibutan di paka kabalog order?")
    

print(menu.lauya, " = ", foodPrice.lauyaPrice); print(menu.pancitGuisado, " = ", foodPrice.pancitGuisadoPrice)
print(menu.baguioBeans, " = ", foodPrice.baguioBeansPrice); print(menu.rm, " = ", foodPrice.rmPrice)
print(); print()

Ordering()