from apikey import key
import requests
'''TODO:
-Implement headers
-Implement german as well as english
-catch bad status codes
'''


'''Bad responses:
400: Bad request
401: Unauthorized
429: Rate limit exceeded
500: internal server error
503: service unavailable
'''

'''Request headers:
User-Agent: Riot-Games-Developer-Portal
Accept-Language: en-US
Accept-Charset: ISO-8859-1,utf-8
Origin: https://developer.riotgames.com'''

'''Sample url:
https://euw.api.pvp.net/api/lol/euw/v1.2/champion?api_key=c501e28e-8fc8-42ab-9739-6643ce1337dd
https://%REGION%.api.pvp.net/api/lol/%REGION%/%VERSION%/%APICARD%?%APIKEY
'''
class riotapi():
    '''This class should be the responsible for all the Api calls.
It imports the private api key which does get shared over git'''
    def request(url : str) -> requests:
        '''Adds headers to the request to be valid and executes it'''
        if '?' in url:
            url += '&api_key=' + key.apikey
        else:
            url += '?api_key=' + key.apikey
        #Set headers
        headers = {'user-agent': 'Riot-Games-Developer-Portal',
                   'accept-language': 'en-US',
                   'accept-charset': 'ISO-8859-1,utf-8',
                   'origin': 'https://developer.riotgames.com'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            pass
        else:
            print('[ERROR] Status code {}'.format(r.status_code))
            r = None            
        return r
        
    class champion():
        def champion(id = '', **kwargs):
            r = riotapi.request('https://euw.api.pvp.net/api/lol/euw/v1.2/champion')

            return r


json = riotapi.champion.champion()
