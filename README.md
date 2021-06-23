# Central Medical Vault
Azure FHIR (Fast Healthcare Interoperability Resources) services based medical record maintaining system for the efficient use of medical resources across the country. 

## Idea
The proposed engineered solution aims to build a secure, tamper proof, automated Azure services based centralised medical platform providing a user with an intuitive and hassle free experience while navigating through the medical resources.

## Objective
The objective of the solution is to act as a one stop platform for availing all the medical resources like diagnosis, hospitalisation and lab reports to mention the few. The tamper proof solution will aim to provide a seamless exchange of medical records with the third parties like insurance companies, educational institutions etc. as well. All the features together will create a system and a channel which could bring a difference and protect the health of each individual in the nation. 

## Application
As stated in the objective, the web application will act as a central Medical Vault for storing all the medical records of an individual. The application comes with the features that aims in changing the future of the healthcare industy. The applications are:

1. The User/Medical Authority/Third Pary will have an unique medical ID(like Aadhar Number) which will be key in accessing the solution. 
2. The Users will be able to request for diagnosis and post diagnosis the doctor will be able to upload the reports on the FHIR server. All the changes made will get dynamically reflected on the portals of each individuals.
3. The User will not have the write access to the document through which the integrity and the authenticity of the reports will be maintained at all times. 
4. The user will be able to leverage the automated bed booking feature in case of emergency and criticality. Since, the bed booking is automated, the user should have the bed booking check approved from the doctor in the diagnosis step itself. In case, the resources are less than the requests, the tool based on ML algorithms will be able to assign the beds based on severity.  
5. The solution comes integrated with the AI based Azure Bots to help the user with covid assesment, finding medical resources and booking the lab tests directly. 
6. The third party integration like the insurance company, education institutions can be made seamlessly with the FHIR server to access the medical records of an individual for perusal. 

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

### Azure AI Health Bots Configuration:
1. Deploy the health bots from the documents shared in the reference above. 
2. Navigate on to the health bot management portal. Take the scenario JSONs from the location in this repo (Central-Medical-Vault/Health Bots/) and create all the three scenarios. 
3. The web Application should be deployed using the Azure App service and link the scenario using the {scenaioID} with the application. 
4. The link to the web app then needs to be added in the following location in this repository (Central-Medical-Vault/templates/patient_home.html)

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
9. The link will now land on to the SignIn/SignUp page of the application. This page is common for logging into all three kind of dashboards supported which are: Patients, Hospitals and the Insurance company. The guided steps to navigate can also be referred from the demo link provided below. 

### Roles supported in the solution proposed:
1. Patient
2. Hospital
3. Insurance Company

### Actions supported by each Role:
##### Note: 
1. Patients will have to signup with the medical ID starting with the initial 'p', Doctor's with the initial 'd' and Insurance Company with the initial 'i'.
2. Refer to the demo link below for the navigation guide through the solution developed. 
#### Patient's Dashboard
1. The Patient portal will have a dashboard through which the patient can navigate between different functionalities.
2. The Patient will be able to make a diagnosis request by clicking on the "New Request" and entering the details in the pop up form. The patient will have a choice to select the preferred hospital name and the doctor as well as to enter the symptoms for initial triage. Once the request is submitted, the patient will be able to see the request status in the "Diagnosed Reports" tab. The data will get written to FHIR database.
3. Once, diagnosed from the doctor's end the patient will be able to see the reports in the "Diagnosed Repots" tab itself. The patient will only have read access to all it's medical records to maintain authenticity. 
4. The patient will be able to find the medical resources/ take covid assesment/ book lab test using the AI based Aure health bots. 
5. The patient wll be able to book the bed using the automated tool which will require a check for the hospitalization from the doctor during the diagnosis request itself. No manual process or human efforts will be involved in the bed booking process. 
6. Patient portal also comes with an option to claim insurance by volunteerly share his/her details with the insurance company and proceed with the protocol.
7. Additional tabs can be added in future develpements with respect to the third party integrations. 

#### Hospital
1. A Doctor will land on to the  hospital's dashboard and can view all the diagnosis request made by the patients.
2. After examining the patient, the diagnosis comments can be written on the "Diagnosis Submission" Tab. This is the place from where the data can be written on the FHIR server and will be reflected immediately on the Patient's portal as well. All the details are transitioned seamlessly between the parties. 
3. Doctor can also see the stock of hospital's medical resources.

#### Insurance Company
1. This is where the third party integration comes into highlight, the insurance company dashboard will have a tab to see the pending requests and the approval request.
2. After analysing the request the Insurer can further proceed for the claim reimbursement.
3. With FHIR, the data is tamper proof which will exempt the third party from re-validating the medical records reducing the delay in claims. 
4. The same can be extended for ther third parties like education institutions etc. in future versions of solution. 

## Additional Features:
1. The automated bed booking facility is an Azure ML based solution which will learn the severity of the request and assign the bed incase the request are more than the resources available. 
2. The medical IDs are unique for an inidividual and can't be assigned again in a lifetime. 
3. All the medical records will be stored in the FHIR database in the format defined by them. For more details visit (https://hl7.org/FHIR/)
4. FHIR meets HIPPA regulatory and is ISO 27001 certified along with 90 other compliance certifications. 
5. FHIR comes with an IoT connector through which the data can be sent using smart devices. 
6. The medical records are secured and protected at all times. 

## Architectural Flow Chart of the Central Medical Vault:

![Flow Chart](https://github.com/ChiragSinhal-1/Central-Medical-Vault/blob/master/Azure%20Deployment(images)/Architechture_flow_diagram.png)

## Growth Strategy
1. Enhanced Integrations 
2. Machine Based Diagnosis
3. Enhanced Scalabilty & Security
4. Cross Platfrom Support
5. IoT Integrations

## Demo Recording
Link: https://drive.google.com/file/d/1xS8ehFfj8BFEvDXAe7RYnQJfUzaUchuX/view?usp=sharing
