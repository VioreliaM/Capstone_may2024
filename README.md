## - CardioLife - 
#### A predictive model that forecasts the risk of having a cardiovascular disease
=========================

### Project Overview  
##### Problem area
According to the World Health Organization, cardiovascular diseases (CVD) are the leading cause of global death, representing between 31-32% of global deaths. 
The area of interest is the prevention of cardiovascular diseases, by predicting the risk of having a CVD and by making recommendations on how to minimize the risk. It is primordial to detect the population with the higher risk of CVD and prevent the apparition of the disease, by adjusting and changing the lifestyle of the population at risk and by implementing preventive measures such as taking medication, or treating the conditions that will further lead to CDV. 

##### The user
First of all, the potential users could be everyone, who wants to check if they will be at risk of having a cardiovascular disease in the future. Each of us will be able to check the probability of having a CVD, and to decide which measures we can take to prevent it and to reduce the risk.  
Another potential user is the healthcare provider, who can use the prediction to understand how likely his patient is to develop CVD in the future, and what are the risks that will lead to CVD. After that, the healthcare provider can identify the steps that his patient should take in order to prevent the CVD and if needed, to provide with appropriate treatments to lower the risk. 
Last but not least, public agencies and authorities should also be interested in the well-being of their population and identify the population that is at risk of having CVD and the preventive measures that should be taken.

##### The impact
The project has both societal and business value. First of all, the prevention of CVD will contribute to the overall well-being of the population, will increase the healthy habits of the population and will improve the demography of the population, by decreasing the death levels.    
Also, the prevention of CVD is an investment towards increased welfare, productivity and economic growth. The economic impact that has the project [3]:
* the costs of treating patients for heart attack and stroke will decrease
* the loss of money through premature death or due to decreased productivity of people who have CVD will be less; 
* the preventive medication will reduce hospitalization costs;
* the income of people will increase if they will prevent having a CVD in the future.

##### Proposed data solution
In this project, we will use different machine learning techniques (logistic regression, decision tree, etc.) to build the best model that will resolve our problem: to predict if a person will have a cardiovascular disease. We will compare the accuracy of the models and will choose the best one. Using the result of the prediction, we will display the reccomendation that the person should consider, in order to minimize the risk of having a CVD. 

##### Description of the dataset
`cardio_dataset.csv` is an open source dataset from Kaggle.com, named: 'Cardiovascular Disease dataset`, that contains 70,000 records of patients. There are three types of information about patients:
* Personal- includes personal data of the patients (age, height, weight, etc.)
* Medical- includes data from medical examinations (blood pressure, cholesterol, etc.)
* Lifestyle- includes lifestyle data of patients (if they smoke, if they are active) 
Data dictionary:
1. ID - a unique id number for each patient (type: float64)
2. Age - age of the patient, in days (type: float64)
2. Gender - the gender of the patient: 1-female, 2-male (type: int64)
3. Height - the height of the patient in cm (type: float64)
4. Weight - the weight of the patient in kg (type: float64)
5. Systolic blood pressure (`ap_hi`) - the systolic blood pressure of the patient (type: float64)
6. Diastolic blood pressure (`ap_lo`) - the diastolic blood pressure of the patient (type: float64)
7. Cholesterol - the level of the cholesterol in the blood: 1-normal, 2-above normal, 3-well above normal (type: int64)
8. Glucose (`gluc`) - the level of glucose in the blood: 1-normal, 2-above normal, 3-well above normal (type: int64)
9. Smoking (`smoke`) - if the patient is smoking: 0- no, 1-yes (type: int64)
10. Alcohol (`alco`) - if the patient is drinking alcohol: 0-no, 1-yes (type: int64)
11. Active - if the patient is active or sedentary: 0-it's not active, 1- is active (type: int64)
12. Cardio - if the patient has a cardiovascular disease: 0-no, 1-yes (type: int64)
 
### Walkthrough Demo

...
...
...

### Project Flowchart

...
...
...

### Project Organization

...
...
...

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible Google Drive folder)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - joblib dump of final model / model object

* `notebooks`
    - contains all final notebooks involved in the project

* `reports`
    - contains final report which summarises the project

* `references`
    - contains papers / tutorials used in the project

* `images`
    - contains all the images used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `capstine_env.yml`
    - Conda environment specification

* `Makefile`
    - Automation script for the project

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

### Dataset

...
...
...

### Credits & References

...
...
...

--------