# AWSAutomation
Problematically create ec2 instance using snapshot ID of previously created ec2 instance. 

I have created Frontend using Basic HTML, CSS, Javascript and backend using Python (Flask)

To run this application, host the frontend application in any webserver and
run backend server by using python, before running python, install all necessary dependencies mentioned in requirements.txt file.

Once the applicatio is hosted in the web server and the backend services in hosted using python flask server (http://127.0.0.1:5000/)

Application ask for the AWS Access Key Id and Secret Key Id for the Authtication purpose.

On Successfull authtication, Application will ask for the Snapshot Id, Instance Id and Instance Name to be creted in AMI.

On this, application will create the AMI in ap-south-1 region.

Once the AMI is created, it will launch the newly created AMI instance.
