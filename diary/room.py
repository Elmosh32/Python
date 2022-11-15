import ui


def get_rooms():
    rooms = {"127 Maldives": [], "101 Krabi": [], "202 Hawaii": [], "255 Iceland": [], "32 Machu-Picchu": [],
             "7 Lapland": [], "24 Antarctica": [], "1 Jerusalem": []}

    return rooms


def available_rooms(rooms, start_t, end_t):
    available = []
    for room_name, meet_time in rooms.items():
        for time in meet_time:
            if end_t <= time[0] or start_t >= time[1]:
                continue
            else:
                break
        else:
            available.append(room_name)
    return available


def choose_available_room(start_t, end_t):
    rooms = get_rooms()
    available = available_rooms(rooms, start_t, end_t)
    if available:
        room_numbers, room_names = ui.available_rooms(available)
        while True:
            room = input(ui.choose_room())
            if room.isnumeric():
                if room in room_numbers:
                    ind = room_numbers.index(room)
                    return room + " " + room_names[ind]
            elif room in room_names:
                ind = room_names.index(room)
                return room_numbers[ind] + " " + room
            else:
                ui.room_not_exist()
    else:
        ui.no_available_room()
        return False


def get_room(rooms):
    room_numbers = []
    room_names = []
    for room in rooms:
        room_details = room.split()
        room_numbers.append(room_details[0])
        room_names.append(room_details[1])
    return room_numbers, room_names


def delete_room_meeting(rooms, room_id, start_t, end_t):
    rooms[room_id].remove((start_t, end_t))


def add_room_meeting(rooms, room_id, start_t, end_t):
    rooms[room_id].append((start_t, end_t))
