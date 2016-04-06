import boto3


def inst_ids():

    """
    Get list of instances in zone
    profile name set in ~/.aws
    :return:
    """

    s = boto3.Session(profile_name='test')
    ec2 = s.resource('ec2')
    for i in ec2.instances.all(): print(i)
    #for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    #    print status
        #print status['InstanceId']


    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.id, instance.instance_type)




def s3_storage():
    """
    Get list of files en S3 bucked
    :return:
    """
    s = boto3.Session(profile_name='default')
    s3 = s.resource('s3')
    bucked = s3.Bucket('odoo-pro-db-backups')
    for i in bucked.objects.all():
        print i.key


s = boto3.Session(profile_name="default")
ec2 = s.resource('ec2')
instance_odoo = ec2.Instance(id='i-558f61d9')
print instance_odoo.state['Name']




