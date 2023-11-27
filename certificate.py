#!/usr/bin/env python3
import re

# Based on this link
# https://stackoverflow.com/a/42829667/11970836
# This function replace data and keeps style
def cert_replace_info(doc_obj, regex , replace):
    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                cert_replace_info(cell, regex , replace)
    


# call docx_replace_regex due to inputs
def replace_info(doc, name, string):
    reg = re.compile(r""+string)
    replace = r""+name
    cert_replace_info(doc, reg, replace)

#Change Participant Name Function
def participant_name(doc, name):
    string = "PARTICIPANT NAME"
    replace_info(doc, name, string)

#Change Event Name Function
def event_name(doc, event):
    string = "EVENT NAME"
    replace_info(doc, event, string)

#Change Event Date Function
def date_of_event(doc, date):
    string = "EVENT DATE"
    replace_info(doc, date, string)

#Change Host Name Function
def host_name(doc, name):
    string = "HOST NAME"
    replace_info(doc, name, string)

