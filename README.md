# Google Translate API for Localization
This is a short python script that will help reduce one step in the process of localization. Since I work majorly on flutter and use a JSON file for every different language to contain translated strings, the script generates a file of the target language in JSON format.

## Installation & Usage

You need python installed on your machine to use the script.

### ESSENTIAL STEPS 

```bash
1. Open the script.py file in a text editor
2. Find "apiKey = " and put your google translate API key that you will get from Google Cloud Console
3. Set the target code of the target language in line number 4. For eg. hi for Hindi, ar for Arabic.
4. Similarly, in line number 3, add the fromCode (language from which you are translating). 

5. Close this file and find strings.txt in the same directory.
6. Add all your "to-be-translated" strings here. One string in one line.

7. Run "python script.py" command in terminal/cmd in the same directory to generate translated files   
```

## Contributing
Pull requests are welcome.
