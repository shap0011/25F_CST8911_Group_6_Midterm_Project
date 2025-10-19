import azure.functions as func
import os
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
import json


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

account_uri = os.environ.get("CosmosDBURI")
database_name = "members"
container_name = "member-cont"

@app.route(route="httpget", methods=["GET"])
def http_get(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Use Managed Identity to get token for Cosmos
        credential = DefaultAzureCredential()

        # CosmosClient automatically uses the token if credential provided
        client = CosmosClient(url=account_uri, credential=credential)

        # Access DB and container
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)

        # Query top 10 items
        query = "SELECT * FROM c"
        items = list(container.query_items(query=query, enable_cross_partition_query=True))

        return func.HttpResponse(
            json.dumps(items, indent=2),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(f"Error: {e}", status_code=500)
