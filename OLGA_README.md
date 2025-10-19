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

Creating a new storage account

<table>
  <tr>
    <td><img src="./screenshots/3_create_storage_account.png" alt="Creating a new storage account" title="Creating a new storage account" width="550" /></td>
    <td></td>
    <td><img src="./screenshots/4_deployment_in_progress.png" alt="Deployment in progress" title="Deployment in progress" width="400" /></td>
  </tr>
</table>

Connecting terminal to Azure Cloud Shell

<img src="./screenshots/5_welcome_to_azure_cloud_shell_terminal.png" alt="Connecting terminal to Azure Cloud Shell" title="Connecting terminal to Azure Cloud Shell" width="1000" />
