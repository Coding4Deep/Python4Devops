services=[
    ("web-app",5),
    ("db-app",3),
    ("cache-app",1),
    ("api-app",2)
]


# without lambda function
def get_replica_count(svc_tuple):
    return svc_tuple[1]

services_sorted=sorted(services, key=get_replica_count)
print(services_sorted)


#using lambda function
print(sorted(services,key=lambda svc:svc[1]))



