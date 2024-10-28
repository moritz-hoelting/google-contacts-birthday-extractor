# Google contacts birthdays extractor

Created because birthdays saved in contacts do not show up in the calendar anymore in Germany.

Extracts the birthdays from all contacts in the `contacts.csv` file and outputs a `birthdays.ics` file that contains recurring events for all the birthdays of the contacts.

## Usage
1. Export contacts from Google to `csv` and place it at `contacts.csv`.
2. Run `pip install`
3. Run `python3 extract.py`
4. Import the generated `birthdays.ics` into your calendar.