
countryDb={}
while True:
    print("1 insert")
    print("2 display countrys")
    print("3 display capitals")
    print("4 get capital")
    print("5 delet")

    choice=int(input("enter your choice(1-5)"))
    if choice==1:
        country=input("enter country :").upper()
        capital=input("enter capital :").upper()
        countryDb[country]=capital

    elif choice==2:
        print(list(countryDb.keys()))

    elif choice==3:
        print(list(countryDb.values()))

    elif choice==4:
        country=input("enter country").upper()
        print(countryDb.get(country))

    elif choice==5:
        country=input("enter contry :").upper()
        del countryDb[country]

    else:
        break