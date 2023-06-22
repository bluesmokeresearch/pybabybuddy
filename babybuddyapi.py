import requests
import config

def apiRequest(endpoint, **parameters):
    '''Request data from BabyBuddy using url and 
        token auth method from config.py
    '''
    try:
        response = requests.get(
            url=config.serverURL + '/api/' + endpoint + '/', 
            headers={"Authorization": "Token {}".format(config.apiKey)},
            params = parameters
        )
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return response.json()['results']



def testRequest():
    solidDiapers = apiRequest('changes',limit=3,solid=True)

    for poop in solidDiapers:
        print(poop['time'])


if __name__ == '__main__':
    testRequest()