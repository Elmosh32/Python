import ui

guests = {"Moshe": [], "Yosi": [], "Vitali": [], "Alon": [], "Matan": [], "Moran": [], "Maor": [], "Eden": [],
          "Nik": []}


def get_participants():
    return guests


def add_guests_to_meeting(start_t, end_t):
    participants = guests
    participants_names = ""
    at_least_one_guest_added = False
    guests_av = available_guest(participants, start_t, end_t)
    while True:
        if len(guests_av) == 0:
            print("No available guests in this time")
            return participants_names

        for ind in range(1, len(guests_av), 2):
            ui.print_participant_name(guests_av[ind], guests_av[ind - 1])

        if at_least_one_guest_added:
            name = input(ui.add_participant_end())
            if name == 'Q':
                break
        else:
            name = input(ui.enter_participant_name())
        if name.isnumeric():
            ind = int(name)
            if ind in guests_av:
                name = guests_av[guests_av.index(ind) + 1]
                time_tup = (start_t, end_t)
                if at_least_one_guest_added:
                    participants_names += ", " + name
                else:
                    participants_names += name
                participants[name].append(time_tup)
                add_guest(guests_av, name, ind)
                at_least_one_guest_added = True
                continue
            else:
                ui.participan_not_exist()
                continue
        elif name in participants:
            time_tup = (start_t, end_t)
            participants[name].append(time_tup)
            if at_least_one_guest_added:
                participants_names += ", " + name
            else:
                participants_names += name
            ind = guests_av[guests_av.index(name) - 1]
            add_guest(guests_av, name, ind)
            at_least_one_guest_added = True
            continue
        else:
            ui.participan_not_exist()
    return participants_names


def add_guest(guests, name, ind):
    i = guests.index(ind)
    ui.participant_added(name)
    guests.remove(ind)
    guests.remove(name)
    for guest_ind in range(i, len(guests), 2):
        guests[guest_ind] -= 1


def available_guest(participants, start_t, end_t):
    guests_av = []
    counter = 1
    for participants_name in participants.keys():
        result = check_if_participant_available(participants, participants_name, start_t, end_t)
        if result:
            guests_av.append(counter)
            guests_av.append(participants_name)
            counter += 1

    return guests_av


def check_if_participant_available(participants, guest_name, start_t, end_t):
    for meetings_time in participants[guest_name]:
        if end_t < meetings_time[0] or start_t > meetings_time[1]:
            continue
        else:
            return False
    return True


def delete_participant_meeting(participants, participants_names, start_t, end_t):
    names = participants_names.split(", ")
    for name in names:
        participants[name].remove((start_t, end_t))


def add_participant_meeting(participants, participants_names, start_t, end_t):
    for name in participants_names:
        participants[name].append((start_t, end_t))
