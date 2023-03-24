"""
This module provides functions for translating text between English and French.

The functions in this module require an IBM Watson Language Translator API key 
and URL. The key and URL should be stored as environment variables with the 
names 'IBM_API_KEY' and 'IBM_API_URL', respectively.

"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

def english_to_french(english_text):
    """
        Translate English to French.
        Args:
            english_text(string).
        Returns:
            string : the french trnaslation of input english text.
    
    """
    if english_text is None:
        return "Error: No input provided"
    french_text = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    return french_text["translations"][0]['translation']


def french_to_english(french_text):
    """
        Translate French to  English 
        Args:
            french_text(string)
        Returns:
            string : the english trnaslation of input french text
    """
    if french_text is None:
        return "Error: No input provided"
    english_text = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    return english_text["translations"][0]['translation']


apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-03-23',
    authenticator=authenticator
)

language_translator.set_service_url(url)
