import ui

MIN_MEETING_TIME = 0.15
OPENING_TIME = 9.00
CLOSING_TIME = 18.00


def check_time_legality(start_t, end_t):
    if ((OPENING_TIME <= start_t) and (start_t < end_t) and (end_t <= CLOSING_TIME)) and (
            end_t - start_t) >= MIN_MEETING_TIME:
        return True
    return False


def ask_for_time():
    while True:
        try:
            start_t = float(input(ui.start_time()))
            end_t = float(input(ui.end_time()))
            if not check_time_legality(start_t, end_t):
                ui.invalid_selected_time(MIN_MEETING_TIME, OPENING_TIME, CLOSING_TIME)
                continue
            return start_t, end_t
        except ValueError:
            ui.invalid_time_val()
