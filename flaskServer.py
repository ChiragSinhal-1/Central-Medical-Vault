from flask import Flask, render_template, request
import requests
import json



app = Flask(__name__)


users = {}

@app.route('/')
def home():
    return render_template('user_login.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    uid = request.form.get('uid')
    login_pwd = request.form.get('password')
    print(uid)
    print(login_pwd)

    if uid in users and str(uid).startswith("p"):
        if users[uid]["password"] == login_pwd:
            return render_template('patient_home.html')
        else:
            return "Invalid Credentials"
    elif uid in users and str(uid).startswith("d"):
        if users[uid]["password"] == login_pwd:
            return render_template('doctors_home.html')
        else:
            return "Invalid Credentials"
    
    elif uid in users and str(uid).startswith("i"):
        if users[uid]["password"] == login_pwd:
            return render_template('patient_home.html')
        else:
            return "Invalid Credentials"
    else:
        return "Unique ID does not exists!"
    

@app.route('/register',methods = ['GET','POST'])
def register():
    
    return render_template('user_register.html')

@app.route('/register/user',methods = ['GET','POST'])
def registeruser():
    email = request.form.get('email')
    name = request.form.get('name')
    uid = request.form.get('UniqueID')
    password = request.form.get('password')

    users[uid] = {"name": name, "email":email, "password":password}

    print(users)
    
    return render_template('user_login.html')

@app.route('/patient/login')
def patientLogin():
    return render_template('patient_home.html')

@app.route('/patient/request')
def patientInfoForm():
    return render_template('patient_info_form.html')



@app.route('/getAccessToken',methods = ['GET','POST'])

def getAccessToken():
#     response = requests.get("https://20.193.232.239:5000/getAccessToken", verify = False, headers={'Content-Type': 'application/json'})
#     res = response.json()
#     print(response)

        address_req = request.args.get('address')
        global accessToken
        accessToken = str(address_req)
        print(accessToken)
        return {}, 200
    
@app.route('/patient/new/request',methods = ['GET','POST'])
def patientNewRequest():
    familyName = request.form.get('lname')
    givenName = request.form.get('fname')
    uid = request.form.get('UniqueMedicalID')
    ctScore = request.form.get('CTScore')
    rtpcrScore = request.form.get('RTPCRScore')
    hospitalName = request.form.get('hospitalName')
    doctorName = request.form.get('preferedDoctor')
    
    
    data = {
    "resourceType": "Patient",
    "active": True,
    "name": [
        {
            "use": "official",
            "family": familyName,
            "given": [
                
                givenName
            ]
        },
        {
            "use": "usual",
            "given": [
                f"UID: {uid}",
                f"CT Score: {ctScore}",
                f"RTPCR Score: {rtpcrScore}",
                f"Hospital Name: {hospitalName}",
                f"Doctor Name: {doctorName}",
                "Diagnosis = To be done"
            ]
        }
    ],
    "gender": "male",
    "birthDate": "1960-12-25"
    
}   

    data = json.dumps(data)


    print(f"data is {data}")
    print(type(data))
    bearerValue = f'Bearer {accessToken}'
    print(f"Hello {accessToken}")
    
    header = {'Authorization': bearerValue, 'Content-Type': 'application/json; charset=UTF-8'}

    accessTokenName = "Shubham Garg"
    response = requests.post("https://cmv.azurehealthcareapis.com/Patient",headers=header,data=data)
    
    print(response.json())
    print(uid)
    print(ctScore)
    return "Success"

@app.route('/patient/claim')
def patientInsuranceClaim():
    return "Work in progress"
@app.route('/patient/medicalstatistics')
def medicalStatistics():
    return render_template('resources_hospital.html')

@app.route('/patient/updatepersonalinfo')
def updatePersonalInfo():
    return render_template('update_personal_info.html')

@app.route('/patient/diagnosedreports')
def diagnosedReports():
    return render_template('new.html')

@app.route('/doctor/login')
def  doctorLogin():
    return render_template('doctors_home.html')

@app.route('/doctor/updateprofessionalinfo')
def updateProfessionalInfo():
    return render_template('doctor_professional_info.html')

@app.route('/doctor/request')
def viewRequest():
    return "Work in Progress"

@app.route('/doctor/uploadreport')
def uploadReport():
    return "Work in Progress"

@app.route('/doctor/medicalstatistics')
def indMedicalStats():
    return render_template('individual_hospital_resources.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 5000, debug= True, ssl_context= 'adhoc')
    