import time
import bcrypt
from nltk.corpus import words
import datetime

passwords = {
    "Bilbo": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq",
    "Gandalf": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC",
    "Thorin": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q",
    "Fili": "$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm",
    "Kili": "$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im",
    "Balin": "$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom",
    "Dwalin": "$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be",
    "Oin": "$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK",
    "Gloin": "$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q",
    "Dori": "$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq",
    "Nori": "$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12",
    "Ori": "$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O",
    "Bifur": "$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK",
    "Bofur": "$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O",
    "Durin": "$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"
}

users = ["Bilbo", "Gandalf", "Thorin", "Fili", "Kili", "Balin", "Dwalin", "Oin", "Gloin", "Dori", "Nori", "Ori", "Bifur", "Bofur", "Durin"]

def findPassword(user):
    print(f"Cracking {user}'s password...")
    startTime = time.time()
    datetime_object = datetime.datetime.fromtimestamp(startTime)
    readable_time = datetime_object.strftime("%Y-%m-%d %H:%M:%S")[11:]
    print(f"Start time: {readable_time}")
    targetValue = passwords[user].encode("utf-8")
    password = None
    for word in words.words():
        if 6 <= len(word) <= 10:
            password = word
            word = word.encode('utf-8')
            eq = bcrypt.checkpw(word, targetValue)
            if eq:
                break

    endTime = time.time()
    totalTime = endTime - startTime
    timeInMins = round(totalTime / 60, 2)
    print(f"{user}'s password: {password}")
    print(f"Took {timeInMins} minutes to crack")
    print()
    return timeInMins

def findAllPasswords(startIdx, endInx):
    times = []
    for user in users[startIdx:endInx]:
        t = findPassword(user)
        times.append(t)
    print(times)

if __name__ == '__main__':
    # findAllPasswords(3, 8)
    findPassword("Thorin")
# Times (minutes):
# Bilbo: 43.5
# Gandalf: 9.82
# Thorin: 9.81
# Fili: 19.31
# Kili: 47.73
# Balin: 61.79
# Dwalin: 42.84





