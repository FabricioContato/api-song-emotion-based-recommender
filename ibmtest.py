import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authentication via IAM
authenticator = IAMAuthenticator('ABf8Yn1k0d2o_2o53IJESFS19hvokaXAJXzmRA5zquNE')
service = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    authenticator=authenticator)
service.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/075911f6-c082-4c09-8d44-761bddec1c2d')


response = service.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
    'Superman fears not Banner, but Wayne.',
    features=Features(
        sentiment=SentimentOptions(),
        emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))