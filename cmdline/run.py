import osquery

instance = osquery.SpawnInstance()
instance.open()
query = instance.client.query(".tables")
