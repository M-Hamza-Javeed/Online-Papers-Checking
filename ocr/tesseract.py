import pytesseract
from .filters import dirlist
import re
import json
from pytesseract import Output
from .filters import *
from django.conf import settings
import time
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from gensim.models.word2vec import Word2Vec


path=settings.BASE_DIR
ocrpath=path+"\\tessdata"
tessdata_dir_config = r'--tessdata-dir '+ocrpath
configuration = cloudmersive_ocr_api_client.Configuration()
configuration.api_key['Apikey'] = 'a4fb3f40-6ad8-4eb9-8101-9e63b7885c8a'
api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
recognition_mode = 'Normal';language = 'ENG' ;preprocessing = 'None' 


def Read_Setting():
    f=open(settings.BASE_DIR+"\setting.json",'r')
    data=json.load(f);print(data)
    return data


'''first read Setting file (json) then if OCR_MODE is online then use online mode otherwise offline '''
def ExtractText(_img):
    try:
        ocr=Read_Setting()['OCR_MODE']
        try:
            if ocr =='online':
                return text(api_call(_img))
        except:
            return text(offline_ocr(_img))
        if ocr == 'offline':
            return text(offline_ocr(_img))
    except:
        return "500 internal Server Error !"


def text(data):
    text= re.sub("[^a-zA-z]"," ",str(data));print(text,path)
    return (text)
    

def offline_ocr(img):
    custom_config = r'-l eng-2+eng --psm 6 -c tessedit_char_white=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    data = pytesseract.image_to_string(imagefilter(img),config=custom_config)
    return data


def api_call(_img):
    image=path+_img;st=""
    try:
        api_response = api_instance.image_ocr_photo_to_text(image, recognition_mode=recognition_mode, language=language)
        return (api_response.text_result)
    except ApiException as e:
        print("Cloudmersive error",e)
