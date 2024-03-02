def study_schedule(permanence_period, target_time):
    if target_time is None:
        return

    students = 0

    for entry_start, entry_end in permanence_period:
        if type(entry_start) is not int or type(entry_end) is not int:
            return
        if entry_start <= target_time <= entry_end:
            students += 1

    return students
