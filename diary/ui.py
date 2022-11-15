def choose_room():
    print("\nEnter room number or room name: ", end="")
    return ''


def room_not_exist():
    print("No such room\nPlease try again")


def no_available_room():
    print("No eoom is available at the time you chose. try choosing another time.")


def start_time():
    print("Please enter start time: ", end="")
    return ''


def end_time():
    print("Please enter end time: ", end="")
    return ''


def invalid_time_parameters():
    print("Only numbers are allowed")


def invalid_selected_time(min_meeting_time, first_meeting, last_meeting):
    print("Invalid meeting time!\nThe minimum meeting time is ", str(int((min_meeting_time * 100))),
          " minutes,\nMeeting must be between ",
          int(first_meeting), ":00 and ", int(last_meeting), ":00\nPlease try again", sep="")


def available_participant():
    print("\nAvailable participants:")


def print_participant_name(participant_name, counter):
    if counter == 1:
        print("\nguest list:")
    print(counter, ". ", participant_name, sep="")


def print_available_guests(guests):
    print("\nguest list:")
    for guest in range(0, len(guests), 2):
        print(guest)


def enter_participant_name():
    print("Please enter participant name or participant number: ", end="")
    return ''


def participant_not_available():
    print("Participant not available please select other participant\n")


def add_participant_end():
    print("Please enter participant name/number or Q to exit: ", end="")
    return ''


def participan_not_exist():
    print("No such name/number\nPlease try again\n")


def participant_added(participant_name):
    print(participant_name, "added to the meeting\n")


def invalid_date():
    print("Invalid date! please try again\n\n")


def insert_date():
    print("Please insert date (dd.mm.yyyy): ", end="")
    return ''


def meeting_number():
    print("\nPlease enter meeting number or C(cancel deletion): ", end="")
    return ''


def invalid_choice():
    print("Invalid choice! please try again\n")


def meeting_deleted_s():
    print("Meeting deleted")


def deletion_canceled():
    print("The deletion canceled")


def meeting_deleted_f():
    print("Deleting meeting failed")


def search_by():
    print("\nSearch By:")
    print('\n'.join('{}. {}'.format(idx + 1, param)
                    for idx, param in enumerate(["Start time", "End time", "Room number/name", "Participant name"])))
    while True:
        search_p = input("\nPlease Choose Search Parameter: ")
        if not search_p.isnumeric():
            invalid_choice()
            continue
        search_p = int(search_p) - 1
        if search_p > 3 or search_p < 0:
            invalid_choice()
            continue
        search_key = input("Search For: ")
        if search_p == 0 or search_p == 1:
            return search_p, float(search_key)
        else:
            return search_p, search_key


def print_diary(date, meetings):
    if meetings:
        print("\n", "Appointment Diary For " + date, sep='', end=' ')
        meeting_f = "\n\nMeeting No. {0:^3}\nStarts At: {1:^4}\t\t\tEnds At: {2:^4}\nAt Room No. {3:^3}\nParticipants:"
        for idx, meet in enumerate(meetings):
            print(meeting_f.format(idx + 1, meet[0], meet[1], meet[2]), end=' ')
            print(*meet[3], sep='')
    else:
        print("\nAppointment Diary is Empty")


def available_rooms(rooms):
    room_names = []
    room_numbers = []
    print("\nAvailable Rooms:")
    for room in rooms:
        room_details = room.split()
        print("Room number:", room_details[0], end=" ")
        print("| Room name:", room_details[1])
        room_numbers.append(room_details[0])
        room_names.append(room_details[1])
    return room_numbers, room_names


def print_diary_list():
    print("\nAppointment Diary",
          "1. Create Appointment",
          "2. Delete Appointment",
          "3. Search Appointment",
          "4. Save Diary",
          "5. Load Diary",
          "6. Print Diary",
          "Q. Exit", sep="\n")


def input_diary_list():
    print("\nPlease enter number from the list or Q(EXIT): ", end="")
    return ''
