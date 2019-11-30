# Desktop Assistant
Siri like desktop assistant written in Python which uses google's speech-to-text library to process voice input.

* Install the dependencies in a virtual environment (using conda or virtualenv) to avoid any issues. Use either pip2 or pip3 for python2 and python3 respectively.

If you are a linux user install the [say](https://askubuntu.com/questions/501910/how-to-text-to-speech-output-using-command-line) command using
```
sudo apt-get install gnustep-gui-runtime
```

```bash
pip2 install -r requirements.txt
pip3 install -r requirements.txt
```

* Usage

```bash
python desktopAssistant.py
````

* Requirement
``` Requirement
certifi==2017.11.5
chardet==3.0.4
gTTS==1.2.2
gTTS-token==1.1.1
idna==2.6
mpg123==0.4
PyAudio==0.2.11
pytz==2017.3
requests==2.18.4
SpeechRecognition==3.8.1
urllib3==1.22
beautifulsoup4==4.6.0
weather-api==0.0.4
```

Supported commands :
* Open google
* Open youtube
* Tell a joke/another joke : Says a random dad joke.
* What's up
* who invented you
