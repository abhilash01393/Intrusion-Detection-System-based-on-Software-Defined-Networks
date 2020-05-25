from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('blue', 'hello111')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('Prey')
cb.upsert('u:king_arthur', {'name': 'Arthur', 'email': 'kingarthur@couchbase.com', 'interests': ['Holy Grail', 'African Swallows']})
# OperationResult<RC=0x0, Key=u'u:king_arthur', CAS=0xb1da029b0000>

print(cb.get('u:king_arthur').value)
# {u'interests': [u'Holy Grail', u'African Swallows'], u'name': u'Arthur', u'email': u'kingarthur@couchbase.com'}
