import requests
import os

def createManagementToken(tokenRequestBody, tokenRequestHeaders, tokenBaseURL):
        """
            Uses Our Service Principal Credentials To Generate Azure Active Directory Tokens
        """

        tokenRequestBody['resource'] = 'https://management.core.windows.net/'
        
        response = requests.get(tokenBaseURL, headers=tokenRequestHeaders, data=tokenRequestBody)
        
        if response.status_code == 200:
            print(response.status_code)
        
        else:
            raise Exception(response.text)
        
        return response.json()['access_token']

def createBearerToken(tokenRequestBody, tokenRequestHeaders, tokenBaseURL):
        """
            Uses Our Service Principal Credentials To Generate Azure Active Directory Tokens
        """
        
        tokenRequestBody['resource'] = '2ff814a6-3304-4ab8-85cb-cd0e6f879c1d'
        
        response = requests.get(tokenBaseURL, headers=tokenRequestHeaders, data=tokenRequestBody)
        
        if response.status_code == 200:
            print(response.status_code)
        
        else:
            raise Exception(response.text)
        
        return response.json()['access_token']


if __name__ == "__main__":
    tokenRequestBody = {
        'grant_type': 'client_credentials',
        'client_id': 'c6cb48dd-9e1f-45b6-a0b7-2006b911b0b9',
        'client_secret': 'BWH8Q~g2NJPmCKtMgs0k1vbhilu_7S6cVVo6QaFV'
    } 
    tokenRequestHeaders = {'Content-Type': 'application/x-www-form-urlencoded'}
    tokenBaseURL = 'https://login.microsoftonline.com/' + '7ae1883b-83f0-42cb-a513-17fa352588a5' + '/oauth2/token'

    bearerToken = createBearerToken(tokenRequestBody=tokenRequestBody, 
                                    tokenRequestHeaders=tokenRequestHeaders, 
                                    tokenBaseURL=tokenBaseURL
                    )
    
    managementToken = createManagementToken(tokenRequestBody=tokenRequestBody,
                                            tokenRequestHeaders=tokenRequestHeaders,
                                            tokenBaseURL=tokenBaseURL
                    )

    os.environ['DATABRICKS_AAD_TOKEN'] = bearerToken 
    os.environ['DATABRICKS_MANAGEMENT_TOKEN'] = managementToken 

    print("DATABRICKS_AAD_TOKEN",os.environ['DATABRICKS_AAD_TOKEN'])
    print("DATABRICKS_MANAGEMENT_TOKEN",os.environ['DATABRICKS_MANAGEMENT_TOKEN'])

    with open(os.getenv('GITHUB_ENV'), 'a') as env:
        print(f'DATABRICKS_AAD_TOKEN={bearerToken}', file=env)
        print(f'DATABRICKS_MANAGEMENT_TOKEN={managementToken}', file=env)


    
    #print("##vso[task.setvariable variable=DATABRICKS_AAD_TOKEN;isOutput=true;]{b}".format(b=bearerToken))
    #print("##vso[task.setvariable variable=DATABRICKS_MANAGEMENT_TOKEN;isOutput=true;]{b}".format(b=managementToken))
