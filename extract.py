#!/usr/bin/env python3

import csv
import icalendar
from datetime import date, timedelta

with open('contacts.csv', 'r', newline='', encoding='utf8') as file:
    reader = csv.reader(file)
    header = next(reader)
    firstname_index = header.index('First Name')
    lastname_index = header.index('Last Name')
    birthday_index = header.index('Birthday')
    birthdays = {f"{entry[firstname_index]} {entry[lastname_index]}": entry[birthday_index] for entry in reader if entry[birthday_index]}
    
    calendar = icalendar.Calendar()
    calendar.add('prodid', '-//Birthdays//Birthdays//DE')
    calendar.add('version', '2.0')
    for name, birthday in birthdays.items():
        event = icalendar.Event()
        event.add('summary', f"{name}'s Birthday")
        if birthday.strip().startswith('-'):
            birthday = f"{date.today().year}{birthday.strip()[1:]}"
        d = date.fromisoformat(birthday)
        event.add('dtstamp', d)
        event.add('dtstart', d)
        event.add('dtend', d + timedelta(days=1))
        event.add('rrule', {'freq': 'yearly'})
        event.add('uid', f"birthday-{name.lower().replace(' ', '-')}")
        calendar.add_component(event)
        
    with open('birthdays.ics', 'wb') as file:
        file.write(calendar.to_ical())