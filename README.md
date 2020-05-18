# Data Hub 📈

![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)


## About

A demo hub where users can experiment with data science by graphing data sets in the browser then downloading them. Web monetized browsers won't see the ads on the page and can also experiment with additional graphing tools.

### How it works

<!-- Users can browse projects or create their own. After viewing a certain amount not all entries show up. When the browser in enabled with web monetization all experiments are visible.  -->


## Features

- [x] User csv upload 
- [x] Enhanced Plots 
- [x] Web Monetization enabled 
- [x] Image download 


## Set up

### Requirements

- [Python](https://www.python.org/) 3.7
- Browser with [coil wallet](https://chrome.google.com/webstore/detail/coil/locbifcbeldmnphbgkdigjmkbfkhbnca?hl=en) 
- [Pyodide Downloaded](https://github.com/iodide-project/pyodide/releases)
- [Bookmarklet for Testing: For testing coil without an account](https://testwebmonetization.com/)
  


### Local development

After the above requirements have been met:

1. Unzip the Pyodide package and add the /src/pyodide.py to your project  
2.  Clone this repository and `cd` into it

```bash
git clone https://github.com/ari-hacks/covid-chatbot.git
cd covid-chatbot
```

2. Install dependencies

```bash
pip3 install chatterbot==1.0.4
pip3 install twilio 
pip3 install pytest 
pip3 install uvicorn    
pip3 install fastapi  
pip3 install nltk   
pip3 install httpx
pip3 install requests_mock         
```

4. Run the application

```bash
uvicorn app.main:app --reload 

#uvicorn runs on http://127.0.0.1:8000    
```

5. Next we need to unzip the ngork [download](https://ngrok.com/download). Ngork creates a secure public tunnel for us to use when communicating with WhatsApp via the twilio API. From your terminal run the following command: 

```bash
./ngrok http 8000

#this port must match the app port
```
6. After you have created your [twilio account](https://www.twilio.com/whatsapp) navigate to the [dashboard's sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox) in the field titled ` when a message comes in ` enter the generated forwarding address from your terminal and save. The forwarding url will look like this: 

![Alt text](/ngork_ex.png?raw=true "Demo")

7. Next follow these [ twilio instructions](https://www.twilio.com/console/sms/whatsapp/learn) to connect your account to WhatsApp and send a message 🎉🎉🎉


### Cloud deployment

To try this application locally, you can deploy it to Heroku. 

```bash 
#check if app is running with this endpoint 
https://heroku-porject.herokuapp.com/twilio/health-check

#add this endpoint into your twilio snadbox
https://heroku-porject.herokuapp.com/twilio/bot
```


Please [Sign up](https://www.heroku.com/)  before Deploying. 

 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)                                               


## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.