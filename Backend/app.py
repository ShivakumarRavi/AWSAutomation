from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
import boto3

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

"""
Function to authenticate the AccessKey and SecretKey
"""

@app.route('/', methods=['POST'])
@cross_origin()
def authentication():
    req_data = request.get_json()
    accessKeyId = req_data["accessKeyId"]
    secretKeyId = req_data["secretKeyId"]
    status = False
    try:
        client = boto3.client('ec2', aws_access_key_id=accessKeyId, aws_secret_access_key=secretKeyId)
        response = client.list_buckets()
        print(response)
        status = True

    except Exception as e:
        status = False

    return jsonify({'status':status})

"""
Function to create AMI using snapshot ID
"""

@app.route('/createami', methods=['POST'])
@cross_origin()
def createAMI():
    req_data = request.get_json()
    snapshotId = req_data["snapshotId"]
    instanceId = req_data["instanceId"]
    accessKeyId = req_data["accessKeyId"]
    secretKeyId = req_data["secretKeyId"]
    instanceName = req_data["instanceName"]
    status = False
    error = ""
    try:
        client = boto3.client('ec2', region_name='ap-south-1', aws_access_key_id= accessKeyId,
                          aws_secret_access_key= secretKeyId )
        response = client.create_image(
            BlockDeviceMappings=[
                {
                    'DeviceName': 'xvdh',
                    'VirtualName': 'ephemeral0',
                    'Ebs': {
                        'DeleteOnTermination': False,
                        'SnapshotId': snapshotId,
                        'VolumeSize': 123,
                        'VolumeType': 'standard'
                    }
                }
            ],
            Description='Newly created AMI',
            DryRun=False,
            InstanceId= instanceId,
            Name=instanceName,
            NoReboot=False
        )
        status = True

    except Exception as e:
        status = False
        error = str(e)

    return jsonify({'status':status, 'error':error, 'imageId':response["ImageId"]})

"""
Function to run Image (AMI) in AWS
"""
@app.route('/runimage', methods=['POST'])
@cross_origin()
def runImage():
    req_data = request.get_json()
    accessKeyId = req_data["accessKeyId"]
    secretKeyId = req_data["secretKeyId"]
    imageId = req_data["imageid"]
    status = False
    error = ""
    try:
        client = boto3.client('ec2', region_name='ap-south-1', aws_access_key_id= accessKeyId,
                          aws_secret_access_key= secretKeyId )

        instance = client.run_instances(ImageId= imageId,MinCount=1,MaxCount=1, InstanceType='t2.micro')
        status = True

    except Exception as e:
        status = False
        error = str(e)

    return jsonify({'status':status, 'error':error, 'instance':str(instance)})

if __name__ == '__main__':
    app.run()