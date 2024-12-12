import requests
def sendinfoTiktok(name):
    

    url = "https://tiktok-api6.p.rapidapi.com/user/details"

    querystring = {"username":"mrbeast"}

    headers = {
        "x-rapidapi-key": "b28d2ceb18mshf318642e9225b01p19150cjsndc248bf6ef6e",
        "x-rapidapi-host": "tiktok-api6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    res=response.json()
    print(response.json())
    # resFollowers=res['stats']['followerCount']
    # resnbrV=res['stats']['videoCount']
    
    # done={
    #     'follower':resFollowers,
    #     'VideosCount':resnbrV
    # }
    
    return {'res':'res'}
