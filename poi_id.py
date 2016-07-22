#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from copy import deepcopy

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
#$ only: 'salary', 'exercised_stock_options', 'bonus'
#features_list = ['poi','salary', 'deferral_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'long_term_incentive', 
#'shared_receipt_with_poi', 'from_this_person_to_poi', 'from_poi_to_this_person']
#ratios for to/from emails
#, 'to_poi_ratio', 'from_poi_ratio'

features_list = ['poi', 'salary', 'exercised_stock_options', 'bonus', 'shared_receipt_with_poi', 'to_poi_ratio', 'from_poi_ratio']
# You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop( "TOTAL", 0 )

### Task 3: Create new feature(s)
temp = deepcopy(data_dict)

for person in temp:
    for feature in temp[person]:
        if (isinstance(temp[person]['from_this_person_to_poi'], int) and (isinstance(temp[person]['from_messages'], int))):
            to_ratio = float(temp[person]['from_this_person_to_poi']) / float(temp[person]['from_messages'])
            data_dict[person]['to_poi_ratio'] = to_ratio
        else:
            data_dict[person]['to_poi_ratio'] = 'NaN'
        if (isinstance(temp[person]['from_poi_to_this_person'], int) and (isinstance(temp[person]['to_messages'], int))):
            from_ratio = float(temp[person]['from_poi_to_this_person']) / float(temp[person]['to_messages'])
            data_dict[person]['from_poi_ratio'] = from_ratio
        else:
            data_dict[person]['from_poi_ratio'] = 'NaN'

#print data_dict['DELAINEY DAVID W']

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)
    
#from sklearn.decomposition import PCA
#pca = PCA(n_components=2)
#pca_features_train = pca.fit_transform(features_train)
#pca_features_test = pca.fit_transform(features_test)

from sklearn.svm import SVC
clf = SVC(C=10000.0, kernel="rbf")
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

# Example starting point. Try investigating other evaluation techniques!
print "accuracy", accuracy_score(labels_test, pred)
precision = precision_score(labels_test, pred)
print "precision", precision
recall = recall_score(labels_test, pred)
print "recall", recall
f1 = f1_score(labels_test, pred)
print "F1", f1

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)