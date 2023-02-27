import subprocess
import json
import pyttsx3
import speech_recognition as sr
from colorama import *

engine = pyttsx3.init()
r = sr.Recognizer()
engine.setProperty('rate', 150)

with sr.Microphone() as source:
    print("Speak now")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said: ", text)
    #engine.say(text)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Could not understand")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
# Get the prompt from the command line argument

# Set up the curl command
curl_command = [
    "curl", "-s", "https://api.openai.com/v1/completions",
    "-H", "Content-Type: application/json",
    "-H", f"Authorization: Bearer ChatGPT_apikey",
    "--insecure",
    "-d", json.dumps({
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 4000,
        "temperature": 1.0
    })
]

# Run the curl command and get the response
output = subprocess.check_output(curl_command).decode("utf-8")

# Parse the response with jq
response = json.loads(output)
generated_text = response["choices"][0]["text"]
# Print the generated text

print(Fore.RED + Style.BRIGHT + "\n[+] Input:", Fore.WHITE + text)
print(Fore.GREEN + Style.BRIGHT + "\n[+] Output:", Fore.WHITE + generated_text)
print("")

engine.say(generated_text)
engine.runAndWait()
