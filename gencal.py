""" gencal
Program to generate a rolling calendar, based on a schedule
"""
import csv
from datetime import date, timedelta
from typing import Optional

NOP_E = "x"
DAG_E = "Dag"
HEL_E = "Heldag"
KVALL_E = "Kväll"
NATT_E = "Natt"
KP_E = "KP"

# Mimic Google Calendar CSV format
IS_EMPTY = "empty"
SUB = "Subject"
START_DATE = "Start Date"
END_DATE = "End Date"
START_TIME = "Start Time"
END_TIME = "End Time"
# DESC = "Description"
# ALL_DAY = "All Day Event"

# Additional info for the program
ADD_DAYS = "_adddays"

EVENTS = {
    NOP_E: {IS_EMPTY: True},
    DAG_E: {
        SUB: DAG_E,
        START_TIME: "07:10",
        END_TIME:   "15:24",
        ADD_DAYS: 0,
        IS_EMPTY: False,
    },
    HEL_E: {
        SUB: HEL_E,
        START_TIME: "07:10",
        END_TIME:   "19:50",
        ADD_DAYS: 0,
        IS_EMPTY: False,
    },
    KVALL_E: {
        SUB: KVALL_E,
        START_TIME: "12:00",
        END_TIME:   "19:50",
        ADD_DAYS: 0,
        IS_EMPTY: False,
    },
    NATT_E: {
        SUB: NATT_E,
        START_TIME: "19:40",
        END_TIME:   "07:20",
        ADD_DAYS: 1,
        IS_EMPTY: False,
    },
    KP_E: {
        SUB: KP_E,
        START_TIME: "08:30",
        END_TIME:   "15:28",
        ADD_DAYS: 0,
        IS_EMPTY: False,
    }
}

SCHEDULE = [
    NATT_E, NATT_E,  NATT_E, NATT_E,    NOP_E,  NOP_E,  NOP_E,
    NOP_E,  NOP_E,   NOP_E,  NOP_E,     NATT_E, NATT_E, NATT_E,
    NOP_E,  NOP_E,   NOP_E,  NOP_E,     HEL_E,  HEL_E,  HEL_E,
    NOP_E,  KVALL_E, KVALL_E, KVALL_E, KP_E,    NOP_E,  NOP_E,
    HEL_E,  DAG_E,   DAG_E,  DAG_E,     NOP_E,  NOP_E,  NOP_E,
]
# When is the first element in SCHEDULE, when n = 0
SCHED_START = date(2024, 2, 12)

OUT_START = SCHED_START  # What date to output first
OUT_COUNT = 31*7-16 # How many days to output 

def event(n: int) -> dict[str, any]:
    mod = n % len(SCHEDULE)
    s = SCHEDULE[mod]
    return EVENTS[s]

def csv_row(n, n_shift, d) -> Optional[list]:
    e = event(n + n_shift)
    if e[IS_EMPTY]:
        return None

    subject = e[SUB]

    days_to_add = e[ADD_DAYS]
    start_d = OUT_START + timedelta(days=n)
    end_d = start_d + timedelta(days=days_to_add)

    start_t = e[START_TIME]
    end_t = e[END_TIME]
    return [subject, start_d, end_d, start_t, end_t]


def main():
    d = OUT_START
    n_shift = (d - SCHED_START).days % len(SCHEDULE)

    with open("sched.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([SUB, START_DATE, END_DATE, START_TIME, END_TIME])
        for n in range(OUT_COUNT):
            row = csv_row(n, n_shift, d)
            if row is not None:
                writer.writerow(row)
            d = d + timedelta(days=1)

if __name__ == "__main__":
    main()
