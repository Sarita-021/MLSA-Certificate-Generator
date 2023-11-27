#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from certificate import *
from docx import Document
import csv
from docx2pdf import convert


# create output folder if not exist
try:
    os.makedirs("Output/Doc")
    os.makedirs("Output/PDF")
except OSError:
    pass


def get_participants(f):
    data = [] # create empty list
    with open(f, mode="r", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row) # append all results
    return data

def create_cert_files(filename, list_participants, host_Name, event_Name, event_Date):

    for participant in list_participants:
        # use original file everytime
        doc = Document(filename)

        name = participant["Full Name"]
        participant_name(doc, name)
        event_name(doc, event_Name)
        date_of_event(doc, event_Date)
        host_name(doc, host_Name)
        doc.save('Output/Doc/{}.docx'.format(name))

        # ! if your program working slowly, comment this two line and open other 2 line.
        print("Output/{}.pdf Creating".format(name))
        convert('Output/Doc/{}.docx'.format(name), 'Output/Pdf/{}.pdf'.format(name))

        # ! Open those lines and comment above 2 lines if your program working extremely slow
        # os.system("docx2pdf Output/Doc/")
        # os.system("move Output\Doc\*pdf Output\PDF")

    
# get certificate temple path
certificate_file = "Templates/Certificate Template.docx"
# get participants path
participants_file = "Templates/Event Participants.csv"

# Enter your name here [Ambassador Name]
host_Name = "Your Name"

#Enter event name
event_Name = "Your Event Name"

#Enter event date
event_date = "Your Event Date"

# get participants
list_participants = get_participants(participants_file)

# process data
create_cert_files(certificate_file, list_participants, host_Name, event_Name, event_date)



