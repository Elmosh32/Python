import meeting_time
import participants
import room


def create_meeting():
    while True:
        start_t, end_t = meeting_time.ask_for_time()
        room_to_return = room.choose_available_room(start_t, end_t)
        if not room_to_return:
            continue
        participants_in_meeting = participants.add_guests_to_meeting(start_t, end_t)
        break
    return True, (start_t, end_t, room_to_return, participants_in_meeting)


def check_meeting(_rooms_d, _participants_d, _start_t, _end_t, _room_n, _guests):
    num_of_guests = len(_guests)
    if meeting_time.check_time_legality(_start_t, _end_t):
        if _room_n in room.available_rooms(_rooms_d, _start_t, _end_t):
            for counter, guest in enumerate(_guests):
                if participants.check_if_participant_available(_participants_d, guest, _start_t,
                                                               _end_t) and counter == num_of_guests - 1:
                    _guests = ", ".join(_guests)
                    return True, (_start_t, _end_t, _room_n, _guests)
                elif participants.check_if_participant_available(_participants_d, guest, _start_t, _end_t):
                    continue
                else:
                    return False, ()

    return False, ()
