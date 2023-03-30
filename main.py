from chatgpt import ChatGPT, colors # From my repo: https://github.com/onurravli/chatgpt-api
import requests
import json
import sys

while True:
    try:
        prompt = input(colors.HEADER + "Act like: " + colors.ENDC)
        resp = requests.get(
            f"https://awesome-chatgpt-prompts-api.vercel.app/act/{prompt}"
        ).text
        js = json.loads(resp)
        try:
            print(colors.OKBLUE + "Prompt: " + colors.ENDC + f"{js['prompt']}")
        except:
            print(f"<< Prompt couldn't found.")
    except (KeyboardInterrupt, EOFError):
        print("Exiting.")
        sys.exit(0)
