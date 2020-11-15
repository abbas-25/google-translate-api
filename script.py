import requests

fromCode = 'en'
target = 'ar'

originalFileName = 'strings.txt'

# // constants
apiKey = ''
baseUri = "https://translation.googleapis.com/language/translate/v2?target=" + \
    target + "&key=" + apiKey
variableUri = ''
translations = []


originals = [

]


def prepareString(value):
    return value.replace(' ', '%20')


def makeUri(variableUri):
    for item in originals:
        tempText = prepareString(item)
        part = '&q=' + tempText
        variableUri = variableUri + part

    uri = baseUri + variableUri
    return uri


def fetchOriginalsFromFile():
    file = open(originalFileName, 'r+')
    content = file.readlines()
    for item in content:
        newItem = item.replace('\n', '')
        newItem = newItem.strip()
        if newItem != '' and originals.__contains__(newItem) == False:
            originals.append(newItem)


def writeToFile(data):
    originalFile = open(fromCode + '.json', 'a+')
    translatedFile = open(target + '.json', 'a+')
    originalFile.read()
    translatedFile.read()
    originalFile.seek(0)
    translatedFile.seek(0)
    originalFile.truncate()
    translatedFile.truncate()

    originalFile.write('{')
    translatedFile.write('{')

    for item in originals:
        originalFile.write(f"\"{item}\":\"{item}\",")
    originalFile.write('}')

    for orig, translated in zip(originals, data):
        translatedFile.write(
            f"\"{orig}\":\"{translated['translatedText']}\",")
    translatedFile.write('}')


def translate(variableUri):
    fetchOriginalsFromFile()
    uri = makeUri(variableUri)
    print(uri)
    response = requests.get(uri)
    data = response.json()['data']['translations']
    for original, translated in zip(originals, data):
        translations.append({
            'original': original,
            'translated': translated['translatedText']
        })
    print(translations)
    writeToFile(data)


translate(variableUri)
