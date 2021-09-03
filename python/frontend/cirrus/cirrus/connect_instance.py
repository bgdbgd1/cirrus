import boto3
import socket

ec2 = boto3.resource('ec2')

# instances = ec2.instances.all()
my_instance = None
for instance in ec2.instances.all():
    if instance.state['Name'] == 'terminated':
        continue
    print(
        "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id,
            instance.state
        )
    )
    my_instance = instance
    break
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.settimeout(handler.PS_CONNECTION_TIMEOUT)
    sock.connect((my_instance.public_ip_address, 22))
except:
    raise

exit()
