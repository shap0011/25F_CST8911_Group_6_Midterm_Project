# 25F_CST8911 Group 6: Midterm Project

## Students:

- Durham Olga - 040687883 - shap0011@algonqionlive.com
- Heallis Dom - heal0076@algonquinlive.com
- Mendoza Jediael - 041208322 - mend0214@algonquinlive.com
- Parsons Matthew - 040909129 - pars0230@algonquinlive.com
- Saini Saizal - 041168394 - sain0225@algonquinlive.com

## Report

### Virtual machine

![Region US East is not available](./screenshots/image-35.png)

Creating a virtual machine for the `US East` region is not available for some services. So, we are going to use `Canada Central` region and keep it consistent for **Azure Function App** and **Cosmos DB** as well.

![Filled up the basic information for VM](./screenshots/image-8.png)

We filled up the _basic information_ for the virtual machine:

- selected our student subscription,
- created a new resource group named **"CST8911-Group6"**,
- named our virtual machine **Group6-VM1**,
- selected **Canada Central**,
- chosen **Windows Server 2022**.

We're using this image because it is _cheap_ and also _allows us_ to install _Postman_ to test our **Function App** later.

![Selected image size & created administrator account](./screenshots/image-9.png)

The **"Standard_B2als"** image size, which has _2 vCPUs_ and _4 GiB_ of memory, was selected. We chose this image and size because it is the most affordable option that still allows us to install Postman to test our **Function App** later and log in to the Azure portal to manage our _database_. We tested cheaper image sizes, but the virtual machines crashed when opening a browser. We also created an _administrator account_ to log in through **Bastion** later.

![Virtual network created](./screenshots/image-10.png)

We created a _virtual network_ named `Group6-VM1-vnet` and left the other options as default.

![VM created and deployed](./screenshots/image-11.png)

The virtual machine has been created and deployed.

---

### Cosmos DB Setup

![Create Azure Cosmos DB Account](./screenshots/image.png)

We created a **Cosmos DB** for **NoSQL** database, we used Learning workload type because we are only going to handle small amount of data for _testing_, put the database in the same resource group as before, named it `"group6cosmodb"`, and select **Canada Central** region. We use _serverless_ to minimize cost because we're only going to be using the database when the function application is running and will be paused for most of the time.

![alt text](./screenshots/image-2.png)

Leave these default.

![alt text](./screenshots/image-3.png)

For connectivity method, we selected private endpoint so that only services that are in the same virtual network such as our virtual machine and function, can access it. Communication between these services are done within a private IP address in the Azure network avoiding public internet access thus providing more security.

![alt text](./screenshots/image-4.png)

Backup policy is set to periodic as we are not planning to keep the database for a long time. We selected zone-redundant backup storage to keep a replicate of the database with in the same region making it still availabe in case of an outage while geo-redundant backup would be too excessive.

![alt text](./screenshots/image-41.png)

We selected key-based authentication to add security so that access is limited by using the private key and connection. This is in addition to Entra ID managed identity we're using for the function app.

---

### Function App

![alt text](./screenshots/image-6.png)

We created a function app with Flex consumption plan as it gives performance while being inexpensive  with scale to zero and pay-as-you-go rate.

![alt text](./screenshots/image-12.png)

Fill up the basic information for the function app:
- selected our student subscription,
- select resource group named **"CST8911-Group6"**,
- named our function app **Group6FunctionApp**,
- selected **Canada Central**,
- chosen **Python 3.12** as it is a programming language we're very familiar with. 

![alt text](./screenshots/image-43.png)

Leave storage accounts default.

![alt text](./screenshots/image-44.png)

Same with our database, we turn off public access and created a new private endpoint for accessing the function app.

![alt text](./screenshots/image-45.png)

For deployment, leave it default as it is unavailable while using private endpoint.

![alt text](./screenshots/image-16.png)

Leave these dafault as well to limit access to these resources.

![alt text](./screenshots/image-46.png)

We've created our function app in which we can deploy our Azure function REST API.

---

### Networking

![alt text](./screenshots/image-17.png)

We created a subnet in the vnet for the Cosmos DB, this is where the private endpoint of the database is connected.

![alt text](./screenshots/image-18.png)

We also created a subnet for the function app and connected the private endpoint.

![alt text](./screenshots/image-19.png)

We separated the virtual machine, Cosmos DB, and Function App in different subnets to improve security by isolating the services and also improving performance by suing segmented IP addresses by providing more direct routes and decreasing traffic.

![alt text](./screenshots/image-47.png)

These are the private endpoints for each services.


---

### Environment Setup
We set up our database and created a python function app.

![alt text](./screenshots/image-26.png)

We connect to our virtual machine through Bastion in the Azure portal. 

![alt text](./screenshots/image-27.png)

We check our connection to the function app to verify that our VM is connected to the same vnet.

![alt text](./screenshots/image-34.png)

Since access to our Cosmos DB is only allowed through the private endpoint, we accessed and created a new database and new container using the Azure portal in the virtual machine which is in the same VNet.

![alt text](./screenshots/image-32.png)

We created new items in the container we can access while testing the function.

![alt text](./screenshots/image-33.png)

We installed Postman to test the Azure funtion REST API.

![alt text](./screenshots/image-42.png)

For creating a function we used VS Code and installed the following extensions:
 - Azure Resources
 - Azure Functions

![alt text](./screenshots/image-37.png)

This is the code for our function, which sends a JSON of the items in our Cosmos DB. It uses DefaultAzureCredential from Azure SDK to check authentication by checking the managed identity assigned to the Function App and performing an OAuth 2.0 token exhange which then allows the function to access and read the contents of the database. This is more secure than using the database connection string which involves storing the primary key in the application. To deploy this function to the Function App in the Azure portal, we allowed public access for a short period of time so VS Code can gain access to the Function App for simplicity's sake but in real world situations, we can set up a point to site (P2S) VPN from our computer to the VNet.

![alt text](./screenshots/image-39.png)

We created an environment variable to store the Cosmos DB URI as an additional security precaution. This avoids hardcoding the value in the app.

![alt text](./screenshots/image-36.png)

We created a user-managed identity for the Function App manually through Azure portal CLI because our subscription does not allow us to see "Cosmos DB Built-in Data Contributor" role in the list of available roles. This role is required to allow our Function App read our database.

![alt text](./screenshots/image-30.png)

We deployed the function in the function app to start our REST API.

---

### Testing
![alt text](./screenshots/image-40.png)

We tested the function in the azure portal to make sure that the function is working properly.

![alt text](./screenshots/image-29.png)

We properly tested the function by using Postman to send HTTP GET request to the Function App default domain "group6functionapp-e6huapcubacahdcf.canadacentral-01.azurewebsites.net". Note that Postman is running in the VM since any other requests from IPs outside of the virtual network will be denied, this is one of the security parameters.

![alt text](./screenshots/image-31.png)

We successfully made an HTTP GET request and received an HTTP response containing a JSON of items in the Cosmos DB.
