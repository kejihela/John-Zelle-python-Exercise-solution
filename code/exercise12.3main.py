from interface import Interface
from attendeeapp import AttendeeApp

def main():
    inter = Interface()
    filename = "ok.txt"
    files = AttendeeApp( filename, inter)
    files.run()

main()

    

