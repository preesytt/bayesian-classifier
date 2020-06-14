Naive Bayesian Classifier
=========================
This is an implementation of a Naive Bayesian Classifier written in Python. It is currently updated to Python 3.8. The utility uses statistical methods to classify documents, based on the words that appear within them. A common application for this type of software is in email spam filters.

The utility must first be 'trained' using large numbers of pre-classified documents,  ̶d̶u̶r̶i̶n̶g̶ ̶t̶h̶e̶ ̶t̶r̶a̶i̶n̶i̶n̶g̶ ̶p̶h̶a̶s̶e̶ ̶a̶ ̶d̶a̶t̶a̶b̶a̶s̶e̶ ̶i̶s̶ ̶p̶o̶p̶u̶l̶a̶t̶e̶d̶ ̶w̶i̶t̶h̶ ̶i̶n̶f̶o̶r̶m̶a̶t̶i̶o̶n̶ ̶a̶b̶o̶u̶t̶ ̶h̶o̶w̶ ̶o̶f̶t̶e̶n̶ ̶c̶e̶r̶t̶a̶i̶n̶ ̶w̶o̶r̶d̶s̶ ̶a̶p̶p̶e̶a̶r̶ ̶i̶n̶ ̶e̶a̶c̶h̶ ̶t̶y̶p̶e̶ ̶o̶f̶ ̶d̶o̶c̶u̶m̶e̶n̶t̶. Once training is complete, unclassified documents can be submitted to the classifier which will return a value between 0 and 1, indicating the probablity that the document belongs to one class of document rather than another.

Training
--------

To train the utility, use the following command:

    python bayes.py learn <class label> <file>  ̶<̶c̶o̶u̶n̶t̶>̶
    
    (count variable no longer required, however entering it will not affect program function)

+ The *class label* argument can be any non-empty value - this is just the name what the document is classified as
+ The *file* argument indicates the location of the file containing the training data that you wish to use
+ [Not needed, here for archive purposes]The *count* argument is a numeric value indicating the number of separate documents contained in the training data file

For example:
    
    
    python bayes.py learn spam all_my_spam.txt
    python bayes.py learn ham inbox.txt 
    
    OR
    [Ignore, for archival purposes only]
    python bayes.py learn spam all_my_spam.txt  ̶1̶0̶0̶0̶0̶
    python bayes.py learn ham inbox.txt  ̶1̶0̶0̶0̶0̶
    

Classification
--------------

Once training is complete, classification is performed using this command:

    python bayes.py classify <file> <class label> <class label>

+ The *file* argument indicates the location of the file containing the document to be classified
+ The two *class label* arguments are the names of the document types against which the input file will be compared

For example:

    python bayes.py classify nigerian_finance_email.txt spam ham
    > Probability that document is spam rather than ham is 0.98

