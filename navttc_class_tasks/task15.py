
class HotelManagementSystem:
    def __init__(self, status):
        self.list = []
        self.status = status


    def check_in(self):
        if self.status:
            print('Available rooms:', self.list)
            add_room = int(input('Enter the room number to check-in: '))
            self.list.append(add_room)
            print('Updated room list:', self.list)
        else:
            print('All rooms are occupied')

    def check_out(self):
        if self.list:
            remove_room = int(input('Enter the room number to check-out: '))
            if remove_room in self.list:
                self.list.remove(remove_room)
                print('Updated room list:', self.list)
            else:
                print('Room number not found')
        else:
            print('All rooms are empty')

    def check_status(self, chkstatus):
        if chkstatus in self.list:
            print(f"room {chkstatus} already available ")
        else:
            print(f"Room {chkstatus} not available, I called the check in function add the room.")
            self.check_out()



room_status = input('Enter status (True or False): ')
object_for_HMS = HotelManagementSystem(room_status)

while True:
    print('Enter your choice:')
    print('1. Check-in a room')
    print('2. Check-out a room')
    print('3. Check room status')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        object_for_HMS.check_in()
    elif choice == 2:
        object_for_HMS.check_out()
    elif choice == 3:
        chkstatus=int(input("Enter room no:"))
        object_for_HMS.check_status(chkstatus)
    else:
        print('You entered the wrong choice')
