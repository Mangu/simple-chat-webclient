# OpenAI Assitant UI sample

This is a Vue.js application that provides a user interface for a OpenAI Asisstant 

## Installation 

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/yourrepository.git
```
Navigate to the project directory:

```bash
cd yourrepository
```

Install the project dependencies:

```bash
npm install
```

Usage
To start the application, run:

```bash
npm run serve
```

Then, open your web browser and navigate to http://localhost:8080.

Navigate to Settings and add an API endpoint and key.

API should provide two function. 1. Create a new thread 2. Send a message. Bellow is the signatures of the APIa

```
POST http://127.0.0.1:8000/thread
Content-Type: application/json
access_token: yourkeyhere
 
###

POST http://127.0.0.1:8000/message
Content-Type: application/json
access_token: yourkeyhere

{
    "message": "Your message / question here",
    "thread_id": "thread_idhere"
}
```
