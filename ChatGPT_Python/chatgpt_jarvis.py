import sys
import subprocess
import json
import pyttsx3
from colorama import *

# Set the OpenAI API token
#openai_api_key = os.getenv("CHATGPT_TOKEN")
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_ZiraDesktop"
# Set the properties for the pyttsx3 engine
engine.setProperty("voice", voice_id)
engine.setProperty("rate", 180) # you can change the speaking rate to fit your preference
# Get the prompt from the command line argument
if len(sys.argv) < 2:
    print("Please provide a prompt as a command line argument.")
    sys.exit(1)

prompt = sys.argv[1]

# Set up the curl command
curl_command = [
    "curl", "-s", "https://api.openai.com/v1/completions",
    "-H", "Content-Type: application/json",
    "-H", f"Authorization: Bearer Chatgpt_api",
    "-d", json.dumps({
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 4000,
        "temperature": 1.0
    })
]

# Run the curl command and get the response
output = subprocess.check_output(curl_command).decode("utf-8")

response = json.loads(output)
generated_text = response["choices"][0]["text"]
# Print the generated text

print(Fore.RED + Style.BRIGHT + "\n[+] Input:", Fore.WHITE + prompt)
print(Fore.GREEN + Style.BRIGHT + "\n[+] Output:", Fore.WHITE + generated_text)
print("")

engine.say(generated_text)
engine.runAndWait()
