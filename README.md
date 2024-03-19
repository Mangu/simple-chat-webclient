# Vue.js Azure Video Indexer Sample Application

This is a Vue.js application that provides a user interface for generating additonal insights on Azure Video Indexer indexed videos. The UI allows you to modify the prompts that generate scene analyzist and summary.

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

Features
Logs Prompt: A form field that allows the user to enter a logs prompt.
Summary Prompt: A form field that allows the user to enter a summary prompt.
Model Temperature: A slider that allows the user to adjust the model temperature.
Environment Variables
This project uses the following environment variables:

VUE_APP_CLIENT_ID: Your client ID.
VUE_APP_API_ENDPOINT: The API endpoint.
VUE_APP_ACCOUNT_ID: Your account ID.
VUE_APP_LOCATION: The location.
VUE_APP_SUBSCRIPTION_KEY: Your subscription key.
VUE_APP_AZURE_OPEN_AI_KEY: Your Azure Open AI key.
VUE_APP_AOAI_ENDPOINT: The Azure Open AI endpoint.
To set these variables, create a file named .env in the root of your project and add the variables like this:

Replace your_client_id, your_api_endpoint, etc. with your actual values.

Contributing
Contributions are always welcome! 