import csv
import math

directory = "C:\\Users\\ADMIN\\Desktop\\CVRAMAN\\project-Rishav-Agarwal-AU13\\application\\Database\\"


def display_title_bar():
    print("**********************************************")
    print("***  WELCOME TO CAR BOOKING SYSTEM  ***")
    print("***HAMARI CAB HAI SABSE HATKE, JISME NAI LAGTE HAI JHATKE***")
    print("**********************************************")


def display_menu_bar():
    print("PLEASE SELECT BELOW MENU")
    print("1. ADD RIDER")
    print("2. ADD DRIVER/CAB")
    print("3. UPDATE CAB LOCATION")
    print("4. UPDATE AVAILABILITY")
    print("5. BOOK A CAB")
    print("6. FETCH RIDER HISTORY")
    print("7. END TRIP")
    print("8. EXIT APPLICATION")


def add_rider():
    print("PLEASE ADD RIDER DETAILS")
    Name = input("Please Enter Your Name: ")
    Age = input("Please Enter Your Age: ")
    Gender = input("Please Enter Your Gender: ")
    Contact = input("Please Enter Your Contact: ")
    filename = directory+"Rider.csv"
    header = ("Name", "Age", "Gender", "Contact")
    data = [(Name, Age, Gender, Contact)]
    writer(header, data, filename, "write")
    print("!!!Welcome", Name, "Have a Great Experience!!!")
    main()


def add_driver_cab():
    print("PLEASE ADD DRIVER/CAB DETAILS")
    Name = input("Please Enter Your Name: ")
    Age = input("Please Enter Your Age: ")
    Gender = input("Please Enter Your Gender: ")
    Location_X = input("Please Enter Your Location X: ")
    Location_Y = input("Please Enter Your Location Y: ")
    CabNumber = input("Please Enter Your Cab Number: ")
    CabName = input("Please Enter Your Cab Name: ")
    DLNumber = input("Please Enter Your DL Number: ")
    Switch = input("Please Enter Your Availability: ")
    Contact = input("Please Enter Your Contact: ")
    filename = directory+"Driver_Cab.csv"
    header = ("Name", "Age", "Gender", "Location_X",
              "Location_Y", "CabNumber", "CabName", "DLNumber", "Switch", "Contact")
    data = [(Name, Age, Gender, Location_X, Location_Y,
             CabNumber, CabName, DLNumber, Switch, Contact)]
    writer(header, data, filename, "write")
    print("!!!Welcome", Name, "Have a Great Experience")
    main()


def update_cab_location():
    print("PLEASE UPDATE CAB LOCATION")
    CabNumber = input("Please Enter Your Cab Number: ")
    Location_X = input("Please Enter Your Location X: ")
    Location_Y = input("Please Enter Your Location Y: ")
    filename = directory+"Driver_Cab.csv"
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]

    for val in readData:
        if(val['CabNumber'] == CabNumber):
            readHeader = val.keys()
            val['Location_X'] = Location_X
            val['Location_Y'] = Location_Y
            writer(readHeader, readData, filename, "update")
    print("Location Updated Sucessfully!!!")
    main()


def update_cab_switch():
    print("PLEASE UPDATE CAB AVAILABILITY")
    Name = input("Please Enter Your Name: ")
    Switch = input("Please Enter Your DL Number: ")
    filename = directory+"Driver_Cab.csv"
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]

    for val in readData:
        if(val['Name'] == Name):
            readHeader = val.keys()
            val['Switch'] = Switch
            writer(readHeader, readData, filename, "update")
    print("!!!Availability Updated Successfully!!!")
    main()


def update_trip_end():
    print("PLEASE END THE TRIP")
    CabName = input("PLEASE ENTER THE CAB NUMBER FOR TRIP: ")
    filename = directory+"Booking.csv"
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]

    for val in readData:
        if(val['CabNumber'] == CabName):
            readHeader = val.keys()
            val['TripEnd'] = "YES"
            writer(readHeader, readData, filename, "update")
    print("Trip Ended Successfully!!!")
    main()


def update_fetch_history():
    print("PLEASE FETCH THE HISTORY")
    Name = input("PLEASE ENTER THE NAME FOR HISTORY: ")
    filename = directory+"Booking.csv"
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]

    for val in readData:
        if(val['Name'] == Name):
            print(val)

    print("End Of History!!!")
    main()


def book_cab():
    print("PLEASE BOOK CAB")
    Name = input("Please Enter Your Name: ")
    Location_X = input("Please Enter Your Location X: ")
    Location_Y = input("Please Enter Your Location Y: ")
    Date = input("Please Enter Date: ")
    Time = input("Please Enter Time: ")
    filename = directory+"Booking.csv"
    header = ("Name", "Location_X",
              "Location_Y", "Date", "Time", "TripEnd", "CabNumber")

    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]

    filenameDrive = directory+"Driver_Cab.csv"
    with open(filenameDrive, newline="") as file:
        readDataDriver = [row for row in csv.DictReader(file)]

    outDict = []
    for val in readDataDriver:
        for valItem in readData:
            if(valItem['TripEnd'] == "NO"):
                valueroot = math.sqrt((int(Location_X) - int(val['Location_X'])) ** 2 + (
                    int(Location_Y) - int(val['Location_Y'])) ** 2)
                outDict.append(val['CabNumber'] + "|" + str(valueroot))

    Cabnumber = ''
    distance = 0.0
    for obj in outDict:
        if(distance < float(obj.split("|")[1])):
            distance = float(obj.split("|")[1])
            Cabnumber = obj.split("|")[0]

    data = [(Name,  Location_X, Location_Y, Date, Time, "NO", Cabnumber)]
    writer(header, data, filename, "write")
    print("Booking Added Successfully!!!")
    main()


def execute_operation():
    menuvalue = int(input("PLEASE ENTER THE OPTION: "))
    if(menuvalue == 1):
        add_rider()
    elif(menuvalue == 2):
        add_driver_cab()
    elif(menuvalue == 3):
        update_cab_location()
    elif(menuvalue == 4):
        update_cab_switch()
    elif(menuvalue == 5):
        book_cab()
    elif(menuvalue == 6):
        update_fetch_history()
    elif(menuvalue == 7):
        update_trip_end()
    elif(menuvalue == 8):
        exit()


def writer(header, data, filename, option):
    with open(filename, "w", newline="") as csvfile:
        if option == "write":

            movies = csv.writer(csvfile)
            movies.writerow(header)
            for x in data:
                movies.writerow(x)
        elif option == "update":
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
        else:
            print("Option is not known")


def main():
    display_title_bar()
    display_menu_bar()
    execute_operation()


if __name__ == "__main__":
    main()
