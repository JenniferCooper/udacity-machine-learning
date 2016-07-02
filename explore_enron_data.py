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

#transform the data into features and the list of distributions
feature_dict = {}
for person in enron_data:
    for feature in enron_data[person]:
        if feature_dict.has_key(feature):
            feature_dict[feature].append(enron_data[person][feature])
        else:
            feature_dict[feature] = [enron_data[person][feature]]

for key, value in feature_dict.iteritems():
    print key, value
    print

#print 
#count_poi = 0
#count_nan = 0
#for k in enron_data:
#    if enron_data[k]['poi'] == True:  #  '== True' can be suppressed
#        count_poi += 1
#        if enron_data[k]['total_payments'] == "NaN":
#            count_nan += 1
#            print k

# print count 
#print count_nan
#print count_poi