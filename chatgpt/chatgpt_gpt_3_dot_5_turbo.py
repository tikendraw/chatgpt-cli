import os
import openai
import argparse
import json
import logging
from termcolor import colored
from pathlib import Path
from utils import indent


FILE_PATH = Path(os.path.dirname(__file__))
API_FILE = FILE_PATH / "openai_api.json"
LOG_FILE = FILE_PATH / "chatgpt_history.log"


def main():

    logging.basicConfig(
        filename=LOG_FILE,
        filemode="a",
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.INFO,
    )

    parser = argparse.ArgumentParser(prog="CHATGPT CLI", description="Cli for chatgpt")
    parser.add_argument("prompt", help="The prompt to send to the OpenAI API")

    args = parser.parse_args()

    # Reading api_key
    try:
        with open(API_FILE, "r") as f:
            api_key = json.load(f)["api_key"]

    except FileNotFoundError:
        api_key = input("Enter OpenAI API key: ")

        with open(API_FILE, "w+") as f:
            f.write('{"api_key":"' + api_key + '"}')

    except Exception as e:
        print("Exception occurred while reading API key from file:", e)
        return

    os.environ["OPENAI_API_KEY"] = api_key

    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": args.prompt}]
    )

    write_output(completion, args)


def write_output(completion, args):
    # response_text = completion.choices[0].message["content"]
    response_text = completion.strip("\n")
    logging.info(f"\nPrompt : {args.prompt} \nChatgpt : \n{response_text}")

    print("\n")

    print(colored(f"YOU     :  {args.prompt}\n", "blue"))

    print(colored("CHATGPT : \n", "green"))
    print(colored(f"{indent(response_text, 10)}", "green"))

    print("\n")


if __name__ == "__main__":
    main()
