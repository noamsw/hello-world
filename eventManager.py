import event_manager as EM
def getFirstDate(events):
    first_date = events[0]["date"]
    for event in events:
        if EM.dateCompare(event["date"] , first_date) < 0:
            first_date = event["date"]
    return first_date   


def printEventsList(events, file_path):
    em = EM.createEventManager(getFirstDate(events))
    for event in events:
        EM.emAddEventByDate(em, event["name"], event["date"], event["id"])
    EM.emPrintAllEvents(em, file_path)
    return em

def testPrintEventsList(file_path):
    events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
                    {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
                                 {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
                                     {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    em = printEventsList(events_lists,file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)

testPrintEventsList("/home/noamwolf/cheeck.txt")
