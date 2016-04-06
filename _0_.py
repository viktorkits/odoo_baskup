import boto.ec2

conn = boto.ec2.connect_to_region('us-west-1')  # or whatever region you want
reservations = conn.get_all_instances()  # could limit results with filters
instances = []
for r in reservations:
    instances.extend(r.instances)
