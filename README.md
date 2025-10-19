# 25F_CST8911 Group 6: Midterm Project

## Students:

- Durham Olga - 040687883 - shap0011@algonqionlive.com
- Heallis Dom - 040728287 heal0076@algonquinlive.com
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

![Global distribution settings](./screenshots/image-2.png)

Leave the **Global distribution** settings default.

![Connectivity method](./screenshots/image-3.png)

For connectivity method, we selected a **private endpoint** so that only services within the same virtual network, such as our virtual machine and function, can access it. Communication between these services occurs over **private IP address** in the Azure network, avoiding public internet access and thereby providing greater security.

![Backup policy](./screenshots/image-4.png)

The **backup policy** is set to **periodic**, as we do not plan to keep the database for a long time. We selected **zone-redundant backup storage** to maintain a replica of the database within the same region ensuring availability in case of an outage, while **geo-redundant backup** would be excessive for our needs.

![Security settings](./screenshots/image-41.png)

We selected **key-based authentication** to enhance security by restricting access through the use of a private key and secure connection. This is in addition to **Entra ID managed identity** used for the Function App.

---

### Function App

![A hosting option selected](./screenshots/image-6.png)

We created a **Function App** with **Flex Consumption Plan**, as it offers strong performance while remaining cost-effective, with **scale-to-zero** capability and a **pay-as-you-go** pricing model.

![Project Details](./screenshots/image-12.png)

Fill up the _basic information_ for the Function App:

- selected our student subscription,
- select resource group named **"CST8911-Group6"**,
- named our function app **Group6FunctionApp**,
- selected **Canada Central**,
- chosen **Python 3.12** as it is a programming language we're very familiar with.

![Storage](./screenshots/image-43.png)

Leave **storage account** default.

![Create Function App](./screenshots/image-44.png)

Similar to our database, we **turned off public access** and **created a new private endpoint** to access the **Function App**.

![Deployment](./screenshots/image-45.png)

For deployment, the setting has been left at its **default value**, as it is **unavailable when using a private endpoint**.

![Authentication](./screenshots/image-16.png)

The settings were left at their **default values** to **limit access** to the resources.

![The Function App created](./screenshots/image-46.png)

We’ve created our **Function App**, where we can deploy our **Azure Function REST API**.

---

### Networking

![Subnets](./screenshots/image-17.png)

A **subnet** was created in the **VNet** for **Cosmos DB**, which hosts the **private endpoint** connection for the database.

![Subnets for the Function App](./screenshots/image-18.png)

A **subnet** was also created for the **Function App**, and its **private endpoint** was connected.

![Security improvement](./screenshots/image-19.png)

We separated the **Virtual Machine**, **Cosmos DB**, and **Function App** into different subnets to improve security by isolating the services and to enhance performance by using segmented IP addresses, which provide more direct routes and reduce network traffic.

![Private endpoints configuration](./screenshots/image-47.png)

Screenshot showing the **private endpoints** configured for each **service**.

---

### Environment Setup

We set up our **database** and created a **Python Function App**.

![Connect through Bastion](./screenshots/image-26.png)

We **connect to our virtual machine** through **Azure Bastion** in the Azure portal.

![The Command Prompt output](./screenshots/image-27.png)

We **check** the connection to the **Function App** to verify that the **virtual machine** is connected to the same VNet.

![Data Explorer New Container](./screenshots/image-34.png)

Because access to our **Cosmos DB** is restricted to the **private endpoint**, we used the **Azure portal** within the **virtual machine**, located in the same **VNet**, to create a **new database** and **container**.

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
