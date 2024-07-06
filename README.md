<p align="center"> <img width="150" style="float:right" alt="logoCardioLife" src="https://github.com/VioreliaM/Capstone_may2024/assets/170043188/4d3ffa2f-1dc4-4d6a-8540-20f9f49b44d2"> </p>

### <p align="center"> A predictive model that forecasts the risk of having a cardiovascular disease </p>

### Project Overview  
#### Problem area :anatomical_heart:
According to the World Health Organization, cardiovascular diseases (CVD) are the leading cause of global death, representing between 31-32% of global deaths. 
The area of interest is the prevention of cardiovascular diseases, by predicting the risk of having a CVD and by making recommendations on how to minimize the risk. It is primordial to detect the population with the higher risk of CVD and prevent the apparition of the disease, by adjusting and changing the lifestyle of the population at risk and by implementing preventive measures such as taking medication, or treating the conditions that will further lead to CDV. 

#### The user
First of all, the potential users could be everyone, who wants to check if they will be at risk of having a cardiovascular disease in the future. Each of us will be able to check the probability of having a CVD, and to decide which measures we can take to prevent it and to reduce the risk.  
Another potential user is the healthcare provider, who can use the prediction to understand how likely his patient is to develop CVD in the future, and what are the risks that will lead to CVD. After that, the healthcare provider can identify the steps that his patient should take in order to prevent the CVD and if needed, to provide with appropriate treatments to lower the risk. 
Last but not least, public agencies and authorities should also be interested in the well-being of their population and identify the population that is at risk of having CVD and the preventive measures that should be taken.

#### The impact
The project has both societal and business value. First of all, the prevention of CVD will contribute to the overall well-being of the population, will increase the healthy habits of the population and will improve the demography of the population, by decreasing the death levels.    
Also, the prevention of CVD is an investment towards increased welfare, productivity and economic growth. The economic impact that has the project:
* the costs of treating patients for heart attack and stroke will decrease
* the loss of money through premature death or due to decreased productivity of people who have CVD will be less; 
* the preventive medication will reduce hospitalization costs;
* the income of people will increase if they will prevent having a CVD in the future.

#### Proposed data solution
In this project, we will use different machine learning techniques (logistic regression, decision tree, etc.) to build the best model that will resolve our problem: to predict what is the risk of having a cardiovascular disease in the future. We will compare the accuracy of the models and will choose the best one. Also, our goal is to find the model with the minimum False Negative predictions. Using the result of the prediction, we will display the reccomendation that the person should consider, in order to minimize the risk of having a CVD. 

#### Description of the dataset
`cardio_dataset.csv` is an open source dataset from Kaggle.com, named: 'Cardiovascular Disease dataset`, that contains 70,000 records of patients. There are three types of information about patients:
* Personal- includes personal data of the patients (age, height, weight, etc.)
* Medical- includes data from medical examinations (blood pressure, cholesterol, etc.)
* Lifestyle- includes lifestyle data of patients (if they smoke, if they are active)
  
*Data dictionary:*

| **Column name** | **Feature**              | **Description**                                                                     | **Data type** |
|-----------------|--------------------------|-------------------------------------------------------------------------------------|---------------|
| `id`            | ID                       | a unique id number for each patient                                                 | float64       |
| `age`           | Age                      | age of the patient, in days                                                         | float64       |
| `gender`        | Gender                   | 1- female, 2-male                                                                   | int64         |
| `height`        | Height                   | in cm                                                                               | float64       |
| `weight`        | Weight                   | in kg                                                                               | float64       |
| `ap_hi`         | Systolic blood pressure  | first number of the blood pressure                                                  | float64       |
| `ap_lo`         | Diastolic blood pressure | second number of the blood pressure                                                 | float64       |
| `cholesterol`   | Cholesterol              | from the result of the blood test:  1- normal, 2-above normal, 3-well  above normal | int64         |
| `gluc`          | Glucose                  | from the result of the blood test:  1- normal, 2-above normal, 3-well  above normal | int64         |
| `smoke`         | Smoking                  | if yes-1, if no-0                                                                   | int64         |
| `alco`          | Drinking alcohol         | if yes-1, if no-0                                                                   | int64         |
| `active`        | Active lifestyle         | if yes-1, if no-0                                                                   | int64         |
| `cardio`        | Cardiovascular disease   | Having a CVD, if yes-1, if no-0                                                     | int64         |


#### Exploratory Data Analysis findings
After doing the Exploratory Data Analysis, we could find that: 
* The older patients have a higher risk of having a CVD
* Men has higher risk of having a CVD, compared to women
* Being overweight and obese, makes you more prone to having a cardiovascular disease
* Patients with a high blood pressure are more at risk to have a CVD
* Having high cholesterol and glucose in the blood, increases the risk of having a CVD
* Smoking and drinking alcohol doesn't influence too much the probability of having a CVD
* Having an active lifestyle decreases the risk of having a CVD

#### Model building and evaluation
After doing data pre-processing, setup, splitting the train and test data, we built four models with parameters that were searched through GridSearch. We can see in the table bellow the models evaluation: 

|                 | **Logistic regression** | **Decision Tree** | **Knearest neighbors** | **Random Forest** |
|-----------------|-------------------------|-------------------|------------------------|-------------------|
| **Train score** | 0.73                    | 0.73              | 0.74                   | **0.76**          |
| **Test score**  | 0.73                    | 0.73              | 0.73                   | 0.73              |
| **Accuracy**    | 0.73                    | 0.73              | 0.73                   | 0.73              |
| **Precision**   | 0.75                    | 0.73              | 0.74                   | **0.76**          |
| **Recall**      | 0.68                    | **0.72**          | 0.69                   | 0.68              |
| **F-1 score**   | 0.71                    | 0.72              | 0.72                   | 0.72              |
| **Test AUC**    | 0.79                    | 0.79              | 0.78                   | **0.80**          |
| **Train AUC**   | 0.79                    | 0.78              | 0.81                   | **0.83**          |

We can observe that Random Forest Classifier has better Train score, Precision, and AUC scores. But Decision Tree has highest Recall. 
I decided to *Optimize* the Random Forest Classifier with setiing a y threshold of 0.44 and we got better results:
* Precision - 0.72
* Recall - **0.74**
* Train score - 0.75
* Test score - 0.73
  
In conclusion, I choosed the best model - **Random Forest Classifier**.
The top features that contribute to the positive prediction are: 
* High blood pressure
* Age
* High Body Mass Index (weight/(height(m)*height(m)))
* A very high cholesterol

### CardioLife Streamlit Web app Demo
Using the best model, I developed a Streamlit web app, where user can insert his data, and check the risk of having a CVD in the future. 
<img width="1214" alt="Demo_app_1" src="https://github.com/VioreliaM/Capstone_may2024/assets/170043188/d0aa62e2-4caa-4cbe-b1bb-cc8e2ab19527">

Here is the CardioLife Streamlit web app. On the sidebar you can see the project's logo and description. On this page, user can enter his data and press the buton `Predict` that will use the Random Forest Model to predict the risk of having a CVD. 
<img width="671" alt="Demo_app_2" src="https://github.com/VioreliaM/Capstone_may2024/assets/170043188/afecef79-873c-40d7-bb30-26d72fcfde42">

On this example, we have an obese user, that has a high blood pressure and a high cholesterol. Therefore, the model predicted that this user is at high risk to have a CVD and displayed the reccomandations on how to minimize the risk. 
<img width="668" alt="Demo_app_3" src="https://github.com/VioreliaM/Capstone_may2024/assets/170043188/980ea18a-76b6-4cd3-86b8-24477e61ce19">
<img width="647" alt="Demo_app_4" src="https://github.com/VioreliaM/Capstone_may2024/assets/170043188/3583431e-0473-4d13-865c-54d6863fbaca">

This is another example, when we have a healthy user, and his risk of having a CVD is low!

### Project Flowchart

1. Description of the problem (Sprint 1)
2. Data gathering (Sprint 1)
3. Data cleaning (Sprint 1)
4. Exploratory Data Analysis (Sprint 1)
5. Data pre-processing (Sprint 2)
6. Data Modelling (Sprint 2,3)
7. Data Evaluation (Sprint 2,3)
8. Data deploying/ CardioLife web app (Sprint 3)


### Project Organization
The project is organized in the following parts:

* `app`
    - the python script for the Streamlit web app: `CardioLife_app.py`
    - the saved model for the web app: `final_rf_model.pkl`
      
* `data` 
    - the public dataset from kagle: `cardio_dataset.csv`
    - the cleaned dataset: `cardio_ds.csv`
    - the dataset that was used for modelling: `cardio_model.csv`

* `images`
    - contains all the images used in the project

* `notebooks`
    - `01-data-cleaning-eda.ipynb` - Sprint 1, contains data cleaning and exploratory data analysis steps
    - `02-pre-processing-base-modelling.ipynb` - Sprint 2, contains data pre-processing and baseline modelling
    - `03-modelling-evaluation.ipynb` - Sprint 3, final model and evaluation, optimization

* `reports`
    - contains Power Points 

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

--------
