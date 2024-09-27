# openspace-organizer

## Description
Our company moved to a new office at the Gent Zuiderport. As many of us are new colleagues, we come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. As they are testing the seating plan in the office, the tables and chairs will change everyday, so you will be prompted to import the current seating possibilities before starting.

Just be aware we have some colleagues working from home. If they would all come to the office there won't be sufficient seating space. We will notifiy if that is the case. So if you want to come and work at the office, you better come on time!

This script runs everyday to re-assign everybody to a new seat.

## Installation
```
.
├── utils/
│   ├── openspace.py
│   ├── table.py
│   └── file_utils.py
├── main.py
├── new_colleagues.csv
├── output.csv
├── README.md
|
new_table_chart.csv
```

## Usage
Before you start, please decide if you want to upload an excel or if you want to give a list of people.

You'll be asked a couple of questions:

* Do you want to add someone to the room or create a new floor plan
* Do you want to use an excel file or do you want to import a list of names
* How many tables to you have?
* How many chairs does each table have?

The program will tell you if there are not enough seats available, randomly divide the people to the seats and, if there are more people than available seats, give back the people which should work from home.

The division per table will also be put into a csv file.

## Visuals
There will be a division per table, with the names of the persons sitting per table.
The names of the people not fitting the tables will be displayed as well.

## (Contributors)

## Timeline
This project took a day for completion

## Personal situation
This was a fun excercise with nice options to explore the user friendliness.
