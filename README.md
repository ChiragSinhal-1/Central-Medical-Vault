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

### References to deploy Azure Api for FHIR
1. https://docs.microsoft.com/en-us/azure/healthcare-apis/fhir/overview#:~:text=%20What%20is%20Azure%20API%20for%20FHIR%C2%AE%3F%20,Interoperability%20Resources%20%28FHIR%C2%AE%29%205%20%20is...%20More%20
2. https://docs.microsoft.com/en-us/azure/healthcare-apis/fhir/fhir-paas-portal-quickstart

### References to deploy Azure Virtual Machine
1. https://azure.microsoft.com/en-in/overview/what-is-a-virtual-machine/
2. https://azure.microsoft.com/en-in/services/virtual-machines

### References to deploy Azure Health bots
1. https://docs.microsoft.com/en-us/azure/health-bot/#:~:text=Azure%20Health%20Bot%20is%20a%20cloud%20platform%20that,AI-powered%20virtual%20health%20assistants.%20About%20Azure%20Health%20Bot
2. https://azure.microsoft.com/en-in/blog/introducing-azure-health-bot-an-evolution-of-microsoft-healthcare-bot-with-new-functionality/
### Azure API for FHIR Configuration:
1. 


### Install PIP for python3

Pip3 can be installed on Ubuntu using the APT package manager. To start off, update the package lists as shown.
```bash 
$ sudo apt update
```

To install pip3 run the command:
```bash 
$ sudo apt install python3-pip
```
### Install all python libraries on Virtual Machine:
Install python flask

```bash 
  pip install python3 flask
  cd my-project
```
### Install Git
Use the following steps to install Git on Ubuntu Linux system. 

Install the software-properties-common package on your system, which contains add-apt-repository command
```bash 
  sudo apt install software-properties-common -y
```
Add the PPA to your system using the following command.
```bash 
  sudo add-apt-repository ppa:git-core/ppa
```
Next, install git debian package on your system
 
```bash 
  sudo apt install git -y
```
 That’s it, Git has been installed on your Ubuntu system.

### Setup Git
Setup the Git user details on your machine, which is used as your identity by the Github or other repository providers.

To setup username and email address system wide, execute the following command. Make sure to change your name and email address with yours
```bash 
 git config --gloabl user.name "Abc Pqr"
git config --gloabl user.email "abc@pqr.com"
```

### Initialise the Git

Navigate to the directory in which you need to initialise the git.

```bash 
 cd my_project
```

Run Initialise Git Command
```bash 
 git init
```
and git repository is initialised.


### Clone the existing project

```bash 
 git clone "project_url"
```

### Run the python server and open VM-ipaddress:5000 in your browser.

Command to open port 5000 of your virtual machine is as follows:

First, you should disable selinux, edit file /etc/sysconfig/selinux so it looks like this: SELINUX=disabled SELINUXTYPE=targeted

Then you can add the new rule to iptables:

```
bash iptables -A INPUT -m state --state NEW -p tcp --dport 5000 -j ACCEPT
```



Save changes
```
sudo service iptables save
```

Command to run the python server is as follows - 
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

  
