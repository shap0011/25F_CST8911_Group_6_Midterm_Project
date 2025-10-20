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

![Data Explorer Items](./screenshots/image-32.png)

New items were created in the container to verify accessibility during function testing.

![Postman Download](./screenshots/image-33.png)

We installed **Postman** to test the **Azure Function REST API**.

![Adding Extensions](./screenshots/image-42.png)

We used **Visual Studio Code** to create the function and installed the following extensions:

- **Azure Resources**
- **Azure Functions**

![VSC screenshot](./screenshots/image-37.png)

This is the code for our function, which returns a JSON object containing the items from our Cosmos DB. It uses **DefaultAzureCredential** from the **Azure SDK** to authenticate by verifying the managed identity assigned to the Function App and performing an **OAuth 2.0 token exchange**, which then allows the function to access and read the database contents.

This approach is more secure than using a database connection string, as it avoids storing the primary key within the application.

To deploy this function to the **Function App** in the **Azure portal**, we temporarily allowed public access so that **VS Code** could connect to the Function App for simplicity. However, in real-world scenarios, we can establish a **Point-to-Site (P2S) VPN** from our local computer to the **VNet** instead.

![Environment variable](./screenshots/image-39.png)

We created an **environment variable** to store the **Cosmos DB URI** as an additional security measure. This prevents hardcoding the value within the application.

![Code + Test Azure PowerShell output](./screenshots/image-36.png)

We manually created a **user-assigned managed identity** for the **Function App** through the **Azure portal CLI**, as our subscription does not include the **“Cosmos DB Built-in Data Contributor”** role in the list of available roles. This role is required to allow the Function App to _read data_ from our database.

![Function App Essentials](./screenshots/image-30.png)

The function was deployed to the **Function App** to initialize the **REST API**.

---

### Testing

![Code + Test](./screenshots/image-40.png)

The **function** was tested in the **Azure portal** to verify that it is functioning correctly.

![Postman Get data Test](./screenshots/image-29.png)

We thoroughly tested the function using **Postman** to send an **HTTP GET request** to the Function App’s default domain:
`group6functionapp-e6huapcubacahdcf.canadacentral-01.azurewebsites.net`.

Note that **Postman was run within the virtual machine**, since any requests from IPs outside the virtual network are denied. This serves as one of our key **security measures**.

![Postman Get data Test result](./screenshots/image-31.png)

We successfully sent an **HTTP GET request** and received a **JSON response** with the items from the **Cosmos DB**.

## CONCLUSION
In this project, our team successfully designed and deployed a secure and cost-efficient cloud-based solution using Microsoft Azure. We implemented a fully integrated system comprising a Virtual Machine, Azure Function App, and Cosmos DB, all operating within a private network to ensure security and compliance with Azure best practices.

Through careful configuration, we minimized public exposure by utilizing private endpoints, managed identities, and OAuth 2.0 authentication. The Function App REST API was tested thoroughly using Postman, validating successful interaction with the Cosmos DB.

This project demonstrates our team’s ability to architect, secure, and optimize cloud resources, showcasing practical understanding of Azure’s serverless, networking, and identity management services.Our deployment model aligns with real-world enterprise standards, emphasizing security, scalability, and cost efficiency.