#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import os
import joblib
import sys
sys.path.append(os.path.abspath("../tools/"))
from feature_format import featureFormat, targetFeatureSplit

data_dict = joblib.load(open("/workspaces/ud120-projects/final_project/final_project_dataset_modified.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
#sort_keys='/workspaces/ud120-projects/tools/python2_lesson14_keys.pkl'


### your code goes here 

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test=train_test_split(features,labels,test_size=0.3, random_state=42)

### it's all yours from here forward!  

from sklearn import tree
clf=tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)
print(clf.predict(features_test))
sc=clf.score(features_test,labels_test)
print(sc)
#print(features_test,labels_test)
n=len(features_test[1])
print(n)