age = int(input("Hur gammal är du? "))

def get_price_type(age):
    if age <= 15:
        print("barn")
    if age <= 19:
        print("ungdom")
    elif age >= 19:
        print("vuxen")
   
get_price_type(age)