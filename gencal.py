""" gencal
Program to generate a rolling calendar, based on a schedule
"""
from datetime import date, timedelta

NOP_E = "x"
DAG_E = "Dag"
HEL_E = "Heldag"
KVALL_E = "Kväll"
NATT_E = "Natt"
KP_E = "KP"

# Mimic Google Calendar CSV format
IS_EMPTY = "empty"
START_DATE = "Start Date"
END_DATE = "End Date"
START_TIME = "Start Time"
END_TIME = "Start Time"
# DESC = "Description"
# ALL_DAY = "All Day Event"

# Additional info for the program
ADD_DAYS = "_adddays"

EVENTS = {
    NOP_E: {IS_EMPTY: True},
    DAG_E: {
        IS_EMPTY: False,
        START_TIME: "07:10",
        END_TIME:   "15:24",
        ADD_DAYS: 0,
    },
    HEL_E: {
        IS_EMPTY: False,
        START_TIME: "07:10",
        END_TIME:   "19:50",
        ADD_DAYS: 0,
    },
    KVALL_E: {
        IS_EMPTY: False,
        START_TIME: "12:00",
        END_TIME:   "19:50",
        ADD_DAYS: 0,
    },
    NATT_E: {
        IS_EMPTY: False,
        START_TIME: "19:40",
        END_TIME:   "07:20",
        ADD_DAYS: 1,
    },
    KP_E: {
        IS_EMPTY: False,
        START_TIME: "08:30",
        END_TIME:   "15:28",
        ADD_DAYS: 0,
    }
}

SCHEDULE = [
    NATT_E, NATT_E,  NATT_E, NATT_E,    NOP_E,  NOP_E,  NOP_E,
    NOP_E,  NOP_E,   NOP_E,  NOP_E,     NATT_E, NATT_E, NATT_E,
    NOP_E,  NOP_E,   NOP_E,  NOP_E,     HEL_E,  HEL_E,  HEL_E,
    NOP_E,  KVALL_E, KVALL_E, KVALL_E, KP_E,    NOP_E,  NOP_E,
    HEL_E,  DAG_E,   DAG_E,  DAG_E,     NOP_E,  NOP_E,  NOP_E,
]
S_START = date(2024, 2, 12)

def event(n: int) -> dict[str, any]:
    mod = n % len(SCHEDULE)
    s = SCHEDULE[mod]
    return EVENTS[s]

def start_date(n: int) -> date:
    return S_START + timedelta(days=n)

def main():
    exp = [EVENTS[s] for s in SCHEDULE]
    res = [event(n) for n in range(len(SCHEDULE))]
    print(exp == res)

if __name__ == "__main__":
    main()
