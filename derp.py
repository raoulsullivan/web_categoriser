#!/usr/bin/env python
import boto
import k2
import pdb

aws_access_key_id = k2.aws_access_key_id
aws_secret_access_key = k2.aws_secret_access_key

pdb.set_trace()

kwargs = {'aws_access_key_id': aws_access_key_id, 'aws_secret_access_key': aws_secret_access_key}

boto.connect_dynamodb(aws_access_key_id, aws_secret_access_key)
dbinstance = boto.dynamodb.connect_to_region("us-west-2", **kwargs)

tableinstance = dbinstance.get_table('testing')

result = tableinstance.query(hash_key='test')

print "Content-Type: text/html"
print
print '<html>'
print '<body>'
for item in result:
    print item
print 'done</body></html>'
