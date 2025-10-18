# 25F_CST8911 Group 6: Midterm Project

## Students:

- Durham Olga - 040687883 - shap0011@algonqionlive.com
- Heallis Dom - heal0076@algonquinlive.com
- Mendoza Jediael - 041208322 - mend0214@algonquinlive.com
- Parsons Matthew - pars0230@algonquinlive.com
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
Select image size of **"Standard_B2als"** which has _2vcpus_ and _4Gib_ memory. We're using this image and size because it is the cheapest option that allows us to install Postman to test our **Function App** later and to login to Azure portal to manage our _database_. We tested cheaper image sizes but the virtual machines crashes from opening a browser. We created an _administrator account_ to login through **Bastion** later.

![Virtual network created](./screenshots/image-10.png)
We created a _virtual network_ named `Group6-VM1-vnet`, and leave the other options default.

![alt text](./screenshots/image-11.png)
Create and deploy the virtual machine.

---

### Cosmos DB Setup

![alt text](./screenshots/image.png)
We created a Cosmos DB for NoSQL database, we used Learning workload type because we are only going to handle small amount of data for testing, put the database in the same resource group as before, named it "group6cosmodb", and select Canada Central region. We use serverless to minimize cost because we're only going to be using the datase when the function application is running and will be paused for most of the time.

![alt text](./screenshots/image-2.png)
Leave these default.

![alt text](./screenshots/image-3.png)

![alt text](./screenshots/image-4.png)
![alt text](./screenshots/image-41.png)

---

### Function App

![alt text](./screenshots/image-6.png)
![alt text](./screenshots/image-12.png)
![alt text](./screenshots/image-43.png)
![alt text](./screenshots/image-44.png)
![alt text](./screenshots/image-45.png)
![alt text](./screenshots/image-16.png)
![alt text](./screenshots/image-46.png)

---

### Networking

![alt text](./screenshots/image-17.png)
![alt text](./screenshots/image-18.png)
![alt text](./screenshots/image-19.png)
![alt text](./screenshots/image-20.png)
![alt text](./screenshots/image-21.png)
![alt text](./screenshots/image-22.png)
![alt text](./screenshots/image-24.png)

---

### Environment Setup

![alt text](./screenshots/image-26.png)
![alt text](./screenshots/image-27.png)
![alt text](./screenshots/image-34.png)
![alt text](./screenshots/image-32.png)
![alt text](./screenshots/image-33.png)
![alt text](./screenshots/image-42.png)
![alt text](./screenshots/image-37.png)
![alt text](./screenshots/image-39.png)
![alt text](./screenshots/image-38.png)
![alt text](./screenshots/image-36.png)
![alt text](./screenshots/image-40.png)

---

### Testing

![alt text](./screenshots/image-30.png)
![alt text](./screenshots/image-29.png)
![alt text](./screenshots/image-31.png)
