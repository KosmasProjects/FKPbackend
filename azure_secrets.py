from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
import os

def get_secret(secret_name):
    load_dotenv()

    client_id = os.getenv('AZURE_CLIENT_ID')
    tenant_id = os.getenv('AZURE_TENANT_ID')
    client_secret = os.getenv('AZURE_CLIENT_SECRET')
    vault_url = os.getenv("AZURE_VAULT_URL")

    # create a credential 
    credentials = ClientSecretCredential(
        client_id = client_id, 
        client_secret= client_secret,
        tenant_id= tenant_id
    )

    # create a secret client object
    secret_client = SecretClient(vault_url= vault_url, credential= credentials)

    # retrieve the secret value from key vault
    secret = secret_client.get_secret(secret_name)
    print('This is secret code:' + secret.value)

    return secret.value