# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 14:29:46 2016

@author: jcoop
"""

Enron Submission Free-Response Questions

A critical part of machine learning is making sense of your analysis process and communicating 
it to others. The questions below will help us understand your decision-making process and 
allow us to give feedback on your project. Please answer each question; your answers should 
be about 1-2 paragraphs per question. If you find yourself writing much more than that, 
take a step back and see if you can simplify your response!

When your evaluator looks at your responses, he or she will use a specific list of rubric items
to assess your answers. Here is the link to that rubric: Link to the rubric Each question has 
one or more specific rubric items associated with it, so before you submit an answer, take a 
look at that part of the rubric. If your response does not meet expectations for all rubric 
points, you will be asked to revise and resubmit your project. Make sure that your responses 
are detailed enough that the evaluator will be able to understand the steps you took and your 
thought processes as you went through the data analysis.

Once you’ve submitted your responses, your coach will take a look and may ask a few more focused 
follow-up questions on one or more of your answers.  

We can’t wait to see what you’ve put together for this project!

Summarize for us the goal of this project and how machine learning is useful in trying to accomplish 
it. As part of your answer, give some background on the dataset and how it can be used to answer the 
project question. Were there any outliers in the data when you got it, and how did you handle those?  
[relevant rubric items: “data exploration”, “outlier investigation”]

The goal of this project is to create an algorithm that identifies enron employees that have 
committed fraud. This dataset, in particular the email data, is too large for any one 
person to digest. I removed the "total" outlier from the data dictionary, since it was throwing off 
the money numbers.


What features did you end up using in your POI identifier, and what selection process did you use 
to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should 
attempt to engineer your own feature that does not come ready-made in the dataset -- explain what 
feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in 
the final analysis, only engineer and test it.) In your feature selection step, if you used an 
algorithm like a decision tree, please also give the feature importances of the features that you 
use, and if you used an automated feature selection function like SelectKBest, please report the 
feature scores and reasons for your choice of parameter values.  
[relevant rubric items: “create new features”, “properly scale features”, “intelligently select 
feature”]

My feature list focused on money and email parameters, assuming the money matters most, 
and that communications would be next. I picked some set of the features, but the accuracy went down.
Later, I added many more and then ran PCA on them.
My entire features_list = ['poi','salary', 'deferral_payments', 'exercised_stock_options', 
'bonus', 'restricted_stock', 'long_term_incentive', 'shared_receipt_with_poi', 
'from_this_person_to_poi', 'from_poi_to_this_person']
I then used PCA(n_components=2) to find the principle components of these features.
Later, I added ratios for email sent to POIs and from POIs this vaulted my p/r scores
up quite a bit.


What algorithm did you end up using? What other one(s) did you try? How did model performance differ 
between algorithms?  [relevant rubric item: “pick an algorithm”]

GaussianNB had a .95 accuracy
SVC(C=10000.0, kernel="rbf") had a .9 accuracy, but no P/R. When I returned, I could not get 
this classifier to not return a divide by 0 error.
I got good results with a Decision Tree using PCA and the new ratio features.


What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this 
well?  How did you tune the parameters of your particular algorithm? (Some algorithms do not have 
parameters that you need to tune -- if this is the case for the one you picked, identify and briefly 
explain how you would have done it for the model that was not your final choice or a different model 
that does utilize parameter tuning, e.g. a decision tree classifier).  [relevant rubric item: 
    “tune the algorithm”]

You can overrfit or not get as good results from the algorithm. For my Decision Tree, I tuned 
the min_split and the random_state parameters. 


What is validation, and what’s a classic mistake you can make if you do it wrong? How did you 
validate your analysis?  [relevant rubric item: “validation strategy”]

Validation is the testing and statistical analysis done to make sure the algorithm is working well.
The classic mistake is to overfit your classifier. This means your number look great, but
the classifier will not work well on new data. 


Give at least 2 evaluation metrics and your average performance for each of them.  Explain an 
interpretation of your metrics that says something human-understandable about your algorithm’s 
performance. [relevant rubric item: “usage of evaluation metrics”]

Accuracy: 0.83500       Precision: 0.45455      Recall: 0.36250 F1: 0.40334     F2: 0.37780
Are the eval metrics for my Decision Tree classifier. 

