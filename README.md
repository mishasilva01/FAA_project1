# FAA_project1

To start, we can devide the dataset according to categorical and interger features.
Integer:
  1. age
  2. trestbps (resting blood pressure)
  3. chol (serum cholestoral)
  4. thalach (maximum heart rate achieved)
  5. oldpeak (ST depression induced by exercise relative to rest)
  6. ca (number of major vessels (0-3) colored by flourosopy) - HAS NAN VALUES

Dealing with NaN:
  - Since from our 303 observations we only have 6 observations, one way to deal with NaN values could be just *removing* those observations

Relevant papers:
  1. Nassif A. (*et al*). 2018. *Machine Learning Classifications of Coronary Artery Disease*. DOI: 10.1109/iSAI-NLP.2018.8692942
  2. Nashif S. (*et al*). 2018. *Heart Disease Detection by Using Machine Learning Algorithms and a Real-Time Cardiovascular Health Monitoring System*. DOI: 10.4236/WJET.2018.64057
  3. Sati N. 2017. *A collective learning approach for semi-supervised data classification*. DOI: 10.5505/pajes.2017.44341
  4. Liu X. (*et al*). 2017. *A Hybrid Classification System for Heart Disease Diagnosis Based on the RFRS Method*. DOI: 10.1155/2017/8272091
  5. Liska G. (*et al*). 2017. *Monte Carlo Evaluation of Classification Algorithms Based on Fisher's Linear Function in Classification of Patients With CHD*. DOI: 10.9790/5728-130104104109
  6. Seenivasagam V. (*et al*). 2014. *MYOCARDIAL INFARCTION DETECTION USING INTELLIGENT ALGORITHMS*. DOI: 10.14311/NNW.2016.26.005
  7. Sidey-Gibbons J. (*et al*). 2019. *Machine learning in medicine: a practical introduction*. DOI: 10.1186/s12874-019-0681-4

What I (Miguel) have done on 17/10/2023:
  1. Tested random forest and decision tree for all features raw features: accuracy was practically 0.50
  2. Selected 6 features ('sex','trestbps','chol','fbs','restecg','slope') through Spearman correlation and threshold of 0.20. The labels weren't 0,1,2,3, and 4, but 0 and 1, where 1 represents presence of disease. The training set was 85%
  3. The Decision Tree classifier started with standard hyperparameters and accuracy was around 0.6-0.65. Some hyperparameters were changed and the only that proved to increase accuracy was the maximum depth of the Tree: the parameter was set to 3. This way, accuracy was 0.73. Code is in project1_experiment.
