import requests
import argparse
import json
import logging
from termcolor import colored
import os
from pathlib import Path

API_ENDPOINT = "https://api.openai.com/v1/completions"

FILE_PATH = Path(os.path.dirname(__file__))
API_FILE = FILE_PATH / "openai_api.json"
LOG_FILE = FILE_PATH / "chatgpt_history.log"


def write_output(response, args):
    response_text = response.json()["choices"][0]["text"]
    logging.info(f"\tPrompt : {args.prompt} \n\tChatgpt : {response_text}")

    print("\n")

    print("YOU     : ", args.prompt)

    print("CHATGPT : ")
    print(colored(f"{response_text}\n", "green", "on_black"))

    print("\n")


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
    parser.add_argument(
        "--max_tokens",
        type=int,
        default=500,
        help="Maximum number of tokens to generate in the response",
    )
    parser.add_argument(
        "-t",
        type=float,
        default=0.5,
        help="Sampling temperature to use for generating the response",
    )

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

    request_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    request_data = {
        "model": "text-davinci-003",
        "prompt": args.prompt,
        "max_tokens": args.max_tokens,
        "temperature": args.t,
    }

    response = requests.post(API_ENDPOINT, headers=request_headers, json=request_data)

    if response.status_code == 200:
        write_output(response, args)
    else:
        logging.error(f"Request failed with status code: {response.status_code}")


if __name__ == "__main__":
    main()
