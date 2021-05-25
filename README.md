[![Forks][forks-shield]][https://github.com/karthikmprakash/Temp_email_Telegram_bot/network/members]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


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

## Working Model  

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 
