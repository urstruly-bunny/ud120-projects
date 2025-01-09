#!/usr/bin/python3

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

import joblib

enron_data = joblib.load(open("/workspaces/ud120-projects/final_project/final_project_dataset.pkl", "rb"))
values=enron_data.values()

#print(values)

#for finding no of datapoints len(enron_data)
#to find no of features in each datapoint let values=data.values() print(len(values[0]))
#to find count of poi=1 in each datapoint
"""count =0
for x in values:
    if(x["poi"]==1):
        count=count+1
    
print(count)"""
#query dataset1
#print(enron_data["PRENTICE JAMES"]["total_stock_value"])
#query dataset2
#print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
#QUERY DATASET 3
#print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
#DEALING WITH UNFILLED FEATURES
