from googletrans import Translator, LANGUAGES

def text_trans(text, src_lan='en', des_lan='de'):
    translator = Translator()
    try:
     translation = translator.translate(text, src=src_lan, dest=des_lan)
     return translation.text
    except Exception as e:
       print(e)


#Convert Language Name to code
def lan_code(language_name):
    for code, name in LANGUAGES.items():
       if name.lower() == language_name.lower():
            return code
    return None

main_text = input("Enter your message:")
des_text = input("Enter the language you want your message to get translated:")

#Get language code
dest_code = lan_code(des_text)

if dest_code:
    translated_text = text_trans(main_text, 'en', dest_code)
    print(f"Translated text: {translated_text}")
else:
    print("Error: Language not supported or invalid input.")


