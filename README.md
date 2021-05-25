# Temporary Email genration with Telegram Bot: Project Overview 
* Created a bot to generate username ,  temporary email and password for websites that could potentially track your personal data.
* It uses the 10minmail service to generate a new email instance and returns back to the user. 
* Users can easily interact with the bot with the Markup Keyboard that primarily focuses on the Bot's features

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** python-telegram-bot requests beautifulsoup4 python-dotenv urllib3   
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Pyhton-telegram-bot Github:** https://github.com/python-telegram-bot/python-telegram-bot
**Telegram Bot API:** https://core.telegram.org/bots/api#message 
**Telegram Bot Documentation:** https://python-telegram-bot.readthedocs.io/en/stable/index.html


## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/salary_by_job_title.PNG "Salary by Position")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/positions_by_state.png "Job Opportunities by State")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/correlation_visual.png "Correlations")

## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 11.22
*	**Linear Regression**: MAE = 18.86
*	**Ridge Regression**: MAE = 19.67

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 
