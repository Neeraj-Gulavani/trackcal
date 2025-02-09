import requests
import os
#API_KEY = os.getenv("CN_API_KEY")

def GetNutrition(query):
    url = "https://api.calorieninjas.com/v1/nutrition?query="
    r = requests.get(url+query, headers={'X-Api-Key': API_KEY})
    if r.status_code == requests.codes.ok:
        return r.text
    else:
        return "Error:" + str(r.status_code) + r.text


def GetRecipe(query):
    url="https://api.calorieninjas.com/v1/recipe?query="
    r=requests.get(url+query, headers={'X-Api-Key:': API_KEY})
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error:", r.status_code, r.text)
if __name__=='__main__':
    print(GetNutrition('mountain dew'))