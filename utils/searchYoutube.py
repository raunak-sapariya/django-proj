from youtube_api import YouTubeDataAPI
from youtube_transcript_api import YouTubeTranscriptApi 
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  

api_key="AIzaSyB00x-Q36iveVfeFnn8EF95_FiURsH4AuQ&"

def searchYoutube(query):
    yt = YouTubeDataAPI(api_key)
    search=yt.search(q=query,max_results=25,video_duration="medium")

    for i in range(len(search)):
        if (search[i]["channel_id"] not in ["UCBwmMxybNva6P_5VmxjzwqA","UCeVMnSShP_Iviwkknt83cww"]):
            try:
                script=YouTubeTranscriptApi.get_transcript(search[i]["video_id"])   
                translate=""
                for j in range(len(script)):
                    translate+=script[j]["text"]+" "
                
                return getCaption(search[i]["video_id"])
                return {"videoId":search[i]["video_id"],"transcript":transcript}
            except Exception:
                pass

def getCaption(id):

    chrome_options = Options()

    chrome_options.add_argument("--headless")
    url = "https://youtubesummarizer.com/"

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    input=driver.find_element(By.CLASS_NAME,value="form-control")
    input.send_keys("https://www.youtube.com/watch?v="+id)
    submit=driver.find_element(By.CLASS_NAME,value="btn-solid-lg")
    size=driver.find_element(By.CLASS_NAME,"form-control-range")    
    driver.execute_script("arguments[0].value = '10';", size)
    submit.click()
    time.sleep(8)
    text=driver.find_element(By.CLASS_NAME,"summary").text
    driver.quit()
    print(text)
    return text

    


print(searchYoutube("pixel 8"))