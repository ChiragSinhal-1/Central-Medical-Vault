# Central Medical Vault
Azure FHIR services based medical record maintaining system for the efficient use of medical resources across the country. 

## Idea
The proposed engineered solution aims to build a secure, tamper proof, automated Azure services based centralised medical platform providing a user with an intuitive and hassle free experience while navigating through the medical resources.

## Objective
The objective of the solution is to act as a one stop platform for availing all the medical resources like diagnosis, hospitalisation and lab reports to mention the few. The tamper proof solution will aim to provide a seamless exchange of medical records with the third parties like insurance companies, educational institutions etc. as well. All the features together will create a system and a channel which could bring a difference and protect the health of each individual in the nation. 

## Application
As stated in the objective, the web application will act as a central Medical Vault for storing all the medical records of an individual. The application comes with the features that aims in changing the future of the healthcare industy. The applications are:

1. The User/Medical Authority/Third Pary will have an unique medical ID(like Aadhar Number) which will be key in accessing the solution. 
2. The Users will be able to request for diagnosis and post diagnosis the doctor will be able to upload the reports on the FHIR server. All the changes made will get dynamically reflected on the portals of each individuals.
3. The User will not have the write access to the document through which the integrity and the authenticity of the reports will be maintained at all times. 
4. The user will be able to levergae the automated bed booking feature in case of emergency and criticality. Since, the bed booking is automated, the user should have the bed booking check approved from the doctor in the diagnosis step itself. In case, the resources are less than the requests, the tool based on ML algorithms will be able to assign the beds based on severity.  
5. The solution comes integrated with the AI based Azure Bots to help the user with covid assesment, findind resources and booking the lab tests directly. 
6. The third party integration like the insurance company, educatioon institutions can be made seamlessly with the FHIR server to access the medical records of an individual for perusal. 

The solution aims in reducing the manual effort by leveraging the AI/ML based Azure services while availing the medical help. 

## Steps to run the application:

### References to deploy Azure Services for the solution:
1. https://docs.microsoft.com/en-us/azure/healthcare-apis/fhir/fhir-paas-portal-quickstart (To deploy the FHIR Service)
2. https://docs.microsoft.com/en-us/azure/healthcare-apis/fhir/tutorial-web-app-write-web-app (FHIR Integration with the Web Application using APIs)
3. https://azure.microsoft.com/en-in/services/virtual-machines (To deploy Azure VMs)
4. https://docs.microsoft.com/en-us/azure/health-bot/quickstart-createyourhealthcarebot (To deploy Azure Health Bots)
5. https://docs.microsoft.com/en-us/azure/app-service/overview (To deploy Azure Web App)
6. https://docs.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial (Azure Log Analytics)

### Azure API for FHIR Configuration:
1. The FHIR server needs to be deployed as per the guided steps in the document above. 
2. Navigate on to the CORS setting on the left pane and enter * for origin and headers. Select all the 6 CRUD operations on the FHIR. 
3. Define the throughput in the database tab on the left pane.
4. Register the application in the Azure Active Directory and provide the permission to the solutions URL (Azure-VM-IP:5000) 
5. Pick the client ID and the tenant ID of the application and add it into the file (Central-Medical-Vault/templates/new.html) for access to FHIR
6. Navigate on to the FHIR service on Azure portal, under the diagnostic tab link the log analytics Azure services deployed from the link above. This will inspect and monitor all the actions performed on FHIR database. 
7. IoT connector can also be linked in case the dat needs to be sensed and entered from the external device. 

### Environement Setup (Azure virtual machine)

1. pip3 can be installed on Ubuntu using the APT package manager. To start off, update the package lists as shown.
```bash 
$ sudo apt update
```

2. To install pip3 run the command:
```bash 
$ sudo apt install python3-pip
```
3. Install all python libraries on Virtual Machine:
```bash 
  pip install python3 flask
  cd my-project
```
4. Configure GIT and clone the project code in a directory. 
5. Run the python server (python3 flaskServer.py) and open VM-ipaddress:5000 in your browser.
6. If the page is not responsive, execute the command to open port 5000 of your virtual machine is as follows:
    First, you should disable selinux, edit file /etc/sysconfig/selinux so it looks like this: SELINUX=disabled SELINUXTYPE=targeted

    Then you can add the new rule to iptables:

    ```
    bash iptables -A INPUT -m state --state NEW -p tcp --dport 5000 -j ACCEPT
    ```
7. Save changes
```
sudo service iptables save
```

8. Re-run the command to start the python server is as follows - 
```bash 
  python3 flaskServer.py
```
### Roles deployed in the Azure API for FHIR:
1. Patient
2. Hospital
3. Insurance Company

### Actions supported by each Role:
##### Note: 
Patient has a Unique Medical ID which always starts with 'p',
similarly, Doctor's which 'd' and Insurance Company with 'i'.
#### Patient
1. The Patient portal will have a homepage through which the patient can navigate between different functionalities.
2. The Patient has an option to make a request for diagnosis and send the request to FHIR Database, also the patient can view what all request has been made by him/her and prescription provided by the doctor.
3. There is an option to view hospital's medical resources which are near to the patient's locality.
4. Once the Doctor approves the patient to make a bed booking request, the Patient can go ahead and raise a request to book a bed in his/her preferred hospital along with an option to check the booking status.
5. There are three bots to help the patient.
6. Patient portal also comes with an option to claim insurance by volunteerly share his/her details with the insurance company and proceed with the protocol.

#### Hospital
1. A Doctor can login into the hospital's portal and can view all the diagnosis request which has been made by the patients.
2. After examining the diagnosis report a Doctor can upload the diagnosed report to FHIR database, From there the patint can view the his diagnosed report.
3. Doctor can also see the stock of hospital's medical resources.

#### Insurance Company
1. In the future, if the patient  claims for insurance and raise a request, that request will go to FHIR Database and after signin into FHIR portal the Insurer can view all the requests and analyse them.
2. After analysing the request the Insurer can further proceed either he/she wants to approve/reject the claim based on the protocols.

## Additional Features:
1. The contract initiated by the customer can be terminated by the customer/Bank if the breach is sensed by any of the parties.
2. The Dashboard can be accessed only by the authorized personas through the email ID which will keep the ledger secured at all times.
3. All the activities done by any of the users will be transparent to all the users in the blockchain so that every party is aware of all the transactions.
4. The ledger is secured through the hashing technology which comes with the Blockchain. 
5. The services can be extended beyond financial institutions depending upon the request and permissions.

## Architectural Flow Chart of the Central Medical Vault:

![Flow Chart](https://github.com/ChiragSinhal-1/Central-Medical-Vault/blob/master/Azure%20Deployment(images)/Architechture_flow_diagram.png)


## Growth Strategy
1. Security Enhancement 
2. Fixed time validity for the KYC
3. Adding other credible information


  
## Demo

Insert gif or link to demo

  
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

  
