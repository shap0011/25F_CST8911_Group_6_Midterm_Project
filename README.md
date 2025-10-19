# 25F_CST8911 Group 6 Midterm Project (Olga Durham draft)

## Scenario 1

In azure, deploy virtual machines(select the cheapest options) then manage them using the respective platform's management tools.

Students must then create an Azure Function app and configure it to use a database (e.g., Cosmos DB).

Then, implement a RESTful API using Azure Functions to interact with the database.

Implement an authentication mechanism for the API using Azure Active Directory (AAD) and OAuth 2.0.

Finally, deploy the Azure Function app and test the API using a tool like Postman.

The students will be evaluated on their ability to configure, secure, and optimize the virtual machines, azure functions, and databases. Following correct security protocols and best practices.

---

## Pre Requirements

- Azure subscription with _Azure for Stugents_
- Install:
  - Azure CLI
  - Functions Core Tools
  - Git
  - Postman
- Pick the closest region to reduce latency/cost: _Canada Central_

## Set up the Resource Group

The resource group created

<table>
  <tr>
    <td><img src="./screenshots/1_PS_resource_group_created.png" alt="Resource Group, location Canada Central, PS output" title="Resource Group, location Canada Central, PS output" width="500" /></td>
    <td></td>
    <td><img src="./screenshots/2_AZ_resource_group_created.png" alt="Resource Group, Azure Dashboard" title="Resource Group, Azure Dashboard" width="450" /></td>
  </tr>
</table>

---

## Creating a new storage account

<table>
  <tr>
    <td><img src="./screenshots/3_create_storage_account.png" alt="Creating a new storage account" title="Creating a new storage account" width="550" /></td>
    <td></td>
    <td><img src="./screenshots/4_deployment_in_progress.png" alt="Deployment in progress" title="Deployment in progress" width="400" /></td>
  </tr>
</table>

Connecting terminal to Azure Cloud Shell

<img src="./screenshots/5_welcome_to_azure_cloud_shell_terminal.png" alt="Connecting terminal to Azure Cloud Shell" title="Connecting terminal to Azure Cloud Shell" width="1000" />

Switch subscription in Cloud Shell and register provider

<img src="./screenshots/6_switch_subscription_in_cloud_shell_and_register_provider.png" alt="Switch subscription in Cloud Shell and register provider" title="Switch subscription in Cloud Shell and register provider" width="1000" />

---

## Create a Standard Public IP and run the Virtual Machine

Public IP created, VM is running

<img src="./screenshots/7_public_ip_created_vm_running.png" alt="Public IP created, VM is running" title="Public IP created, VM is running" width="1000" />

---

## Add the PC’s SSH key to the VM + lock NSG to the home IP

### Create an SSH key

Public key generated

<img src="./screenshots/8_generated_public_key.png" alt="Public key generated" title="Public key generated" width="1000" />

The entire public key

<img src="./screenshots/9_entire_public_key.png" alt="Entire public key" title="Entire public key" width="1000" />

### Add key to VM + lock NSG to the home IP

**Key added - IP locked to 23.233.24.110/32**

---

## SSH to the VM and harden SSH

Verify VM power state

<img src="./screenshots/10_vm_running.png" alt="VM running" title="VM running" width="1000" />

---

## Create Cosmos DB (Serverless)

### Register the Cosmos DB resource provider

Registered

<img src="./screenshots/11_cosmos_db_registered.png" alt="Cosmos DB resource provider registered" title="Cosmos DB resource provider registered" width="1000" />

### Create the Cosmos DB account

Cosmos DB account created

<img src="./screenshots/12_cosmos_account_created.png" alt="Cosmos DB account created" title="Cosmos DB account created" width="1000" />

### Create DB and container

<table>
  <tr>
    <td><img src="./screenshots/13_db_created.png" alt="DB created" title="DB created" width="475" /></td>
    <td></td>
    <td><img src="./screenshots/14_container_created.png" alt="Container created" title="Container created" width="475" /></td>
  </tr>
</table>

---

## Create Function App (Python) + enable Managed Identity

### Grant the Function’s Managed Identity Cosmos DB Data Contributor (data-plane)

Function App is ready

<img src="./screenshots/15_function_app_is_ready.png" alt="Function App is ready" title="Function App is ready" width="1000" />

---

## Deploy a minimal GET function (Python) via zip deploy

### Set app setting, (re)zip, deploy, restart, verify

```
curl "https://${HOST}/api/items_get"
[
  {
    "name": "FUNCTIONS_WORKER_RUNTIME",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "FUNCTIONS_EXTENSION_VERSION",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "AzureWebJobsStorage",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "WEBSITE_CONTENTAZUREFILECONNECTIONSTRING",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "WEBSITE_CONTENTSHARE",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "APPLICATIONINSIGHTS_CONNECTION_STRING",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "COSMOS_ENDPOINT",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "WEBSITE_RUN_FROM_PACKAGE",
    "slotSetting": false,
    "value": null
  },
  {
    "name": "SCM_DO_BUILD_DURING_DEPLOYMENT",
    "slotSetting": false,
    "value": null
  }
]
updating: host.json (stored 0%)
updating: requirements.txt (deflated 16%)
updating: items_get/ (stored 0%)
updating: items_get/function.json (deflated 49%)
updating: items_get/__init__.py (deflated 58%)
 - Uploading ============================== 100.0% ..
olga [ /tmp/midterm-api ]$
```

### Verifying the function is running and call it

```
curl -i "https://${HOST}/api/items_get"
== Functions registered ==

== Curling ==
HTTP/2 404
date: Sun, 19 Oct 2025 11:42:43 GMT
server: Kestrel
content-length: 0
```

### Troubleshooting

### New Function App created

<img src="./screenshots/16_new_function_created.png" alt="New Function App created" title="New Function App created" width="1000" />
