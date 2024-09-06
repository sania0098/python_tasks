class HotelManagementSystem:
    def __init__(self, available_rooms):
        self.available_rooms = available_rooms
        self.occupied_rooms = []

    def check_in(self):
        if self.available_rooms:
            print('Available rooms:', self.available_rooms)
            add_room = int(input('Enter the room number to check-in: '))
            if add_room in self.available_rooms:
                self.available_rooms.remove(add_room)
                self.occupied_rooms.append(add_room)
                print(f'Room {add_room} has been checked in.')
            else:
                print(f'Room {add_room} is not available.')
        else:
            print('All rooms are occupied.')

    def check_out(self):
        if self.occupied_rooms:
            print('Occupied rooms:', self.occupied_rooms)
            remove_room = int(input('Enter the room number to check-out: '))
            if remove_room in self.occupied_rooms:
                self.occupied_rooms.remove(remove_room)
                self.available_rooms.append(remove_room)
                print(f'Room {remove_room} has been checked out.')
            else:
                print(f'Room {remove_room} is not currently occupied.')
        else:
            print('All rooms are empty.')

    def check_status(self):
        if self.occupied_rooms:
            print('Rooms currently occupied:', self.occupied_rooms)
        else:
            print('No rooms are currently occupied.')
        if self.available_rooms:
            print('Rooms currently available:', self.available_rooms)
        else:
            print('No rooms are currently available.')

# Example usage
available_rooms = [101, 102, 103, 104, 105]
hms = HotelManagementSystem(available_rooms)

while True:
    print('Enter your choice:')
    print('1. Check-out a room')
    print('2. Check-in a room')
    print('3. Check room status')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        hms.check_out()
    elif choice == 2:
        hms.check_in()
    elif choice == 3:
        hms.check_status()
    else:
        print('You entered a wrong choice.')
