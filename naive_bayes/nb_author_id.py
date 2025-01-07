#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess(
    words_file="/workspaces/ud120-projects/tools/word_data.pkl",
    authors_file="/workspaces/ud120-projects/tools/email_authors.pkl"
)



##############################################################
# Enter Your Code Here



##############################################################

##############################################################
'''
You Will be Required to record time for Training and Predicting 
The Code Given on Udacity Website is in Python-2
The Following Code is Python-3 version of the same code
'''
from sklearn.naive_bayes import GaussianNB
clf=GaussianNB()

t0 = time()
# # < your clf.fit() line of code >
clf.fit(features_train,labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
# # < your clf.predict() line of code >
print(clf.predict(features_test))
print("Predicting Time:", round(time()-t0, 3), "s")


acc=clf.score(features_test,labels_test)
print(acc)

# t0 = time()
# # < your clf.fit() line of code >
# print("Training Time:", round(time()-t0, 3), "s")

# t0 = time()
# # < your clf.predict() line of code >
# print("Predicting Time:", round(time()-t0, 3), "s")

##############################################################