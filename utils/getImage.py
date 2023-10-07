from .strict_gpt import strict_output
import requests
import json
def getImage(title):
    """  image = strict_output(
   
        "you are an AI capable of finding the most relevant image for a course",
        'Please provide a good image search term for the title of a course about'+title+' with following units: '+" ".join(units)+'. This search term will be fed into the unsplash API, so make sure it is a good search term that will return related results',
        {
            "image_search_term": "a good search term for the title of the course",
        }
        )
    image=json.loads(image)  """

    data=requests.get("https://api.unsplash.com/search/photos?page=1&query="+title+'&client_id=4l0ovgicAVAqgSDhyXRfsmj2cQmcNhf2EXEcrhSBXGg')

    data=data.json()
    print(data["results"][0]["urls"]["regular"])
