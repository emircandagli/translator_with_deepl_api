import json
import deepl
import os

#api key
DEEPL_API_KEY = "API-KEY-GOES-HERE"

for index in [1,2,3]
#open and select the "Email" keys in given JSON file
    with open("database"{index}".json", "r", encoding="utf-8") as file:
        json_data = json.load(file)
    emails = [item["Email"] for item in json_data if "Email" in item]

    if not emails:
        raise ValueError("'Email' dict not found in given JSON file.")

    languages = ['TR', 'AR', 'RU', 'DE', 'FR', 'PT-PT', 'ES']#deepl does not support azarbaijani language 

    translator = deepl.Translator(DEEPL_API_KEY) #open translator
    output_folder = "translated_htmls"
    os.makedirs(output_folder, exist_ok=True) #create folder

    for index2, email in enumerate(emails, 1):  
        for lang in languages:
            translated_text = translator.translate_text(email, target_lang=lang).text #translate each given data


            #html content creation
            html_content = f"""
            <!DOCTYPE html>
            <html lang="{lang}">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Email {index2} - Translated ({lang})</title>
            </head>
            <body>
                <p>{translated_text}</p>
            </body>
            </html>
            """

            
            txt_filename = os.path.join(output_folder, f"email_{index2}_{lang}.txt") #txt file creation

            with open(txt_filename, "w", encoding="utf-8") as txt_file:
                txt_file.write(html_content) #put translated emails into the text file

print(f"All of the html files will be saved in {output_folder}")
