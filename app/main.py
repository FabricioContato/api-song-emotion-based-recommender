import json
from unittest import async_case
from fastapi import FastAPI
from pydantic import BaseModel
import requests as rq

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#from .routers import image

app = FastAPI()

class Chating(BaseModel):
    conversation: str

@app.post("/test")
async def test(chating: Chating):

    # Authentication via IAM
    authenticator = IAMAuthenticator('ABf8Yn1k0d2o_2o53IJESFS19hvokaXAJXzmRA5zquNE')
    service = NaturalLanguageUnderstandingV1(
        version='2018-03-16',
        authenticator=authenticator)
    service.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/075911f6-c082-4c09-8d44-761bddec1c2d')

    print(chating.conversation)
    ibm_response = service.analyze(
        text=chating.conversation,
        features=Features(
            emotion=EmotionOptions())).get_result()

    emotions = ibm_response["emotion"]["document"]["emotion"]
    highest_emotion = sorted(emotions.items(), key=lambda item: item[1], reverse=True)[0][0]
    print(highest_emotion)

    json = rq.get("https://ws.audioscrobbler.com/2.0/" +
            f"?method=tag.gettoptracks&tag={highest_emotion}&" +
            "api_key=fc9fb6f781e2d3a575784f9b98e37b99&format=json").json()

    #print(json)
    name = json["tracks"]["track"][0]["name"]
    url = json["tracks"]["track"][0]["url"]

    return {"name": name, "url": url}