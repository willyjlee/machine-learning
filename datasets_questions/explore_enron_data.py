#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))

print(len(enron_data[enron_data.keys()[0]]))

c = 0
for key in enron_data:
    if enron_data[key]["poi"] == 1:
        c = c + 1
print(c)

fd = open("../final_project/poi_names.txt", 'r')
print(len(fd.readlines()))
fd.close()

print enron_data["SKILLING JEFFREY K"]