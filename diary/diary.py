import datetime

import meeting
import participants
import room
import ui


def create_diary():
    diary_date = ".".join(str(datetime.date.today()).split("-")[::-1])
    members = participants.get_participants()
    rooms = room.get_rooms()
    diary = {"meetings": [],
             "date": diary_date,
             "participants": members,
             "rooms": rooms}
    return diary


def create_appointment(_diary):
    result, appointment = meeting.create_meeting()
    if result:
        add_meeting(_diary, appointment)


def delete_appointment(_diary):
    ui.print_diary(_diary["date"], _diary["meetings"])
    result = False
    if _diary["meetings"]:
        user_choice = meeting_number_to_delete(len(_diary["meetings"]))

        if user_choice == "cancel":
            ui.deletion_canceled()
            return
        meeting = _diary["meetings"].pop(user_choice)
        room.delete_room_meeting(_diary["rooms"], meeting[2], meeting[0], meeting[1])
        participants.delete_participant_meeting(_diary["participants"], meeting[3], meeting[0], meeting[1])
        result = True
    if result:
        ui.meeting_deleted_s()
    else:
        ui.meeting_deleted_f()


def meeting_number_to_delete(num_of_meetings):
    while True:
        meeting = input(ui.meeting_number())
        if meeting.isnumeric():
            meeting_num = int(meeting) - 1
            if 0 <= meeting_num < num_of_meetings:
                return meeting_num
        else:
            if meeting == 'C':
                return "cancel"
        ui.invalid_choice()


def save_diary(diary):
    num_of_meetings = len(diary["meetings"])

    if num_of_meetings:
        file_name = "{0}"
        meeting_f = "{0}\n{1}\n{2}\n"
        file = open(file_name.format(diary["date"]), "w")
        file.write('\n')
        for counter, meeting in enumerate(diary["meetings"]):
            file.write(str(meeting_f.format(meeting[0], meeting[1], meeting[2])))
            print(*meeting[3], file=file, sep="")
            if counter != num_of_meetings - 1:
                file.write("\n")
        file.close()
        print("The diary was saved successfully")
        return True
    return False


def load_diary(old_diary):
    file_name = get_file_date()
    counter = 1
    try:
        file = open(file_name, "r")
        diary = create_diary()
        ch = file.readline()
        while ch:
            ch = file.readline()
            if not ch:
                break
            if counter == 1:
                start_t = float(ch)
            if counter == 2:
                end_t = float(ch)
            if counter == 3:
                meeting_room = ch.strip("\n")
            if counter == 4:
                guests = ch.strip("\n")
                guests = guests.split(", ")
            counter += 1
            if counter % 5 == 0:
                result, meet = meeting.check_meeting(diary["rooms"], diary["participants"], start_t, end_t,
                                                     meeting_room,
                                                     guests)
                if result:
                    add_meeting(diary, meet)
                    participants.add_participant_meeting(diary["participants"], guests, start_t, end_t)
                    room.add_room_meeting(diary["rooms"], meeting_room, start_t, end_t)
                    counter = 0
                    continue

        old_diary["date"] = file_name
        old_diary["meetings"] = diary["meetings"]
        old_diary["participants"] = diary["participants"]
        old_diary["rooms"] = diary["rooms"]
        print("File loading completed successfully")
        return True
    except FileNotFoundError:
        print("File not found")


def get_file_date():
    while True:
        date = input(ui.insert_date())
        counter = date.count('.')
        if counter == 2:
            year = date.split(".")[2]
            if year.isnumeric() and len(year) == 4 and int(year) > 0:
                month = date.split(".")[1]
                if month.isnumeric() and len(month) == 2 and 12 >= int(month) > 0:
                    day = date.split(".")[0]
                    if day.isnumeric() and len(day) == 2 and 31 >= int(day) > 0:
                        return date
        ui.invalid_date()


def add_meeting(_diary, _meeting):
    for counter, meet in enumerate(_diary["meetings"]):
        if _meeting[0] < meet[0]:
            _diary["meetings"].insert(counter, _meeting)
            break
    else:
        _diary["meetings"].append(_meeting)


def print_diary(_diary):
    ui.print_diary(_diary["date"], _diary["meetings"])


def search_appointment(diary):
    if diary["meetings"]:
        param, key = ui.search_by()
        meetings = []
        if param == 0 or param == 1:
            for meet in diary["meetings"]:
                if meet[param] == key:
                    meetings.append(meet)
        elif param == 2:
            room_num, room_name = room.get_room(diary["rooms"])
            if key.isnumeric():
                if key in room_num:
                    ind = room_num.index(key)
                    for meet in diary["meetings"]:
                        if meet[param] == key + " " + room_name[ind]:
                            meetings.append(meet)
            elif key in room_name:
                ind = room_num.index(key)
                for meet in diary["meetings"]:
                    if meet[param] == room_num[ind] + " " + key:
                        meetings.append(meet)
        else:
            for meet in diary["meetings"]:
                if key in meet[param]:
                    meetings.append(meet)
        if meetings:
            print("'" + str(key) + "'" + " Search Results:\n", meetings)
            status = "Searching appointment finished successfully"
        else:
            status = "No Results Found For " + "'" + str(key) + "'."
    else:
        status = "Diary is Empty."
    print(status)


def manage_diary():
    diary = create_diary()
    ui.print_diary_list()
    while True:
        user_choice = diary_user_choice()
        if user_choice == 'exit':
            break
        elif user_choice == 1:
            create_appointment(diary)
        elif user_choice == 2:
            delete_appointment(diary)
        elif user_choice == 3:
            search_appointment(diary)
        elif user_choice == 4:
            save_diary(diary)
        elif user_choice == 5:
            load_diary(diary)
        elif user_choice == 6:
            print_diary(diary)
        ui.print_diary_list()


def diary_user_choice():
    while True:
        user_choice = input(ui.input_diary_list())
        if user_choice.isnumeric():
            user_choice = int(user_choice)
            if user_choice < 1 or user_choice > 6:
                ui.invalid_choice()
                continue
            return user_choice
        elif user_choice == 'Q':
            return "exit"
        else:
            ui.invalid_choice()


manage_diary()
