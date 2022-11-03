import json
import logging
import os

import azure.functions as func
import azure.cosmos.container as cosmos_container
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.database as cosmos_database
import azure.cosmos.exceptions as exceptions

HOST = os.environ.get('ACCOUNT_HOST')
MASTER_KEY = os.environ.get('ACCOUNT_KEY')
DATABASE_ID = os.environ.get('COSMOS_DATABASE')

CONTAINER_ID = 'testcon'
USER_AGENT = 'functions'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    client = cosmos_client.CosmosClient(
        HOST,
        {'masterKey': MASTER_KEY},
        user_agent=USER_AGENT,
        user_agent_overwrite=True,
    )

    try:
        database = read_database(client, DATABASE_ID)
        container = read_container(database, CONTAINER_ID)
        item = read_item(container, 'ce1dcee4-73ec-4461-b1e9-11b3cbbc1cd7')
        logging.info(item)
        return func.HttpResponse(json.dumps(item), status_code=200)

    except Exception as e:
        logging.exception(e)
        return func.HttpResponse(
             "The item is not found.",
             status_code=404
        )

def read_database(client: cosmos_client.CosmosClient, id: str) -> cosmos_database.DatabaseProxy:
    try:
        database = client.get_database_client(id)
        database.read()
        print('Database with id \'{0}\' was found, it\'s link is {1}'.format(id, database.database_link))
        return database

    except exceptions.CosmosResourceNotFoundError:
        print('A database with id \'{0}\' does not exist'.format(id))

def read_container(database: cosmos_database.DatabaseProxy, id: str) -> cosmos_container.ContainerProxy:
    try:
        container = database.get_container_client(id)
        container.read()
        print('Container with id \'{0}\' was found, it\'s link is {1}'.format(container.id, container.container_link))
        return container

    except exceptions.CosmosResourceNotFoundError:
        print('A container with id \'{0}\' does not exist'.format(id))

def read_item(container: cosmos_container.ContainerProxy, doc_id: str) -> dict:
    # TODO: パーティションキーの役割を明確に把握できていない
    try:
        response = container.read_item(item=doc_id, partition_key=doc_id)
        return response

    except exceptions.CosmosHttpResponseError:
        raise
