# ChatGPT CLI
This project provides a command-line interface to interact with OpenAI's ChatGPT API. With this tool, you can easily send prompts to the API and receive responses right from your terminal.
**Note: This is a free tool. DO NOT ABUSE IT OR YOUR API KEYS WILL BE REVOKED 1-2 request/Hour**

## Prerequisites
Before you can start using this tool, you'll need an OpenAI API key. You can sign up for an account and obtain an API key by visiting the OpenAI website.
[Get api key here](https://platform.openai.com/account/api-keys)



## Installation
Clone the repository to your local machine:
```
git clone https://github.com/yourusername/chatgpt-cli.git
```
Install the required dependencies:
```
python3 -m pip install chatgpt-cli
```

## Usage
To use the ChatGPT CLI, simply call `chatgpt` followed by a prompt argument:

To use chatgpt with `text_davinci_003` model
```
chatgpt your_prompt_here -t [temperature] 
```
To use chatgpt 3.5 turbo model
```
chatgptplus your_prompt_here  
```

This will send the specified prompt to the OpenAI API and print the response to your terminal. The tool will also log the interaction history to chatgpt_history.log file.

You can also customize the OpenAI model used by modifying the model parameter in the openai.ChatCompletion.create() method call.

Acknowledgements
This project was inspired by the official OpenAI API examples and uses the OpenAI Python library for API communication.

License
This project is just for fun and is under No license .
