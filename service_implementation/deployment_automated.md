# Service-deployment manual
In CloudFlow, services are deployed in a highly automated fashion. As a
developer, you will not have to manually start and stop Docker containers. You
also won't have to (in fact, you cannot) log into the VM where your services
will be running. This manual describes all necessary steps for deploying and
monitoring your services.

## Prerequisites
### Where are services deployed?
While you won't have to manually deploy your services, you have to know _where_
they are deployed, such that you can register them in the workflow editor.
Once deployed, all services are available under the following deployment path:
```
https://srv.hetcomp.org/<project>-<service_name>
```
Here, `<project>` is the project name you log in with into the CloudFlow
portal. For experiment partners, this is most likely `"experiment_#"`.
`<service_name>` is a name that you choose when creating a new service.

### Do I have to configure my service for being deployed?
Yes, you do. You have to tell your service the `/<project>-<service_name>` bit
of the previous section, such that the service knows under which path it needs
to listen for incoming requests.

In all code examples in this repository, this sub-path is called the
`CONTEXT_ROOT`, and is configurable via an environment variable.

As an example, if you log in with the project name `experiment_2`, and you
create a service with the name `hpc-preprocessor`, your service would have to
listen under the path `/experiment_2-hpc-preprocessor`.

### Are there restrictions for the service names?
Yes. Service names have to
* begin with a lower-case letter,
* contain only lower-case letters (`a-z`), numbers (`0-9`), and hyphens,
* end with a lower-case letter or number (but not with a hyphen),
* have at most 32 characters, including the `<project>-` prefix.

### What is the interface for service deployment?
In CloudFlow, the platform service `servicectl` takes care of the automatic
service deployment. It is a RESTful web service deployed under:
```
https://api.hetcomp.org/servicectl-1/
```
Additionally, the CloudFlow Python library clfpy
(https://github.com/CloudiFacturing/clfpy) comes with a client for servicectl.
In the examples given here, we will be using this client.

## Creating and starting a new service
The creation of a new service contains the following steps:
1. Create a new, empty, and non-active service. This will set up all the
   necessary "wiring" behind the scenes and also create a Docker repository for
   the service.
2. Obtain Docker login credentials for the service's repository
3. Push a Docker image to the service's repository
4. Update the service with a service definition. This will trigger the Docker
   image to be pulled and started.

Afterwards, the service's status and log files can be monitored, see the next
sections for details.

In the following sub-sections, the four steps above will be explained in
detail, with code stubs using the clfpy library for every step. For all API
calls, a valid CloudFlow session token is required which can also be acquired
using the clfpy library. Here, it is assumed that such a token is stored in the
environment variable `CFG_TOKEN`.

### 1 Create a new, empty service
To create a new, empty service, one only needs to choose a name and call the
`create_new_service()` method of clfpy's services client:
```python
import os

import clfpy

interface_url = 'https://api.hetcomp.org/servicectl-1/'
token = os.environ['CFG_TOKEN']
name = 'test-service'

srv = clfpy.ServicesClient(interface_url)
r = srv.create_new_service(token, name)
```
The response object, `r`, is a Python `dict`:
```python
>>> pprint(r)
{'links': [{'href': '/services/test-service', 'rel': 'self'},
           {'href': 'https://srv.hetcomp.org/cloudifacturing-test-service',
            'rel': 'deployment'}],
 'name': 'test-service'}
```
The response object contains links to the service itself (as a relative link
within the services-client API) as well as to the deployment URL where the
service will be reachable once it's deployed.

### 2 Obtain Docker login credentials
The following snippet assumes that it is run after the snippet in the previous
section.
```python
creds = srv.get_docker_credentials(token, name)
```
This returns a Python `dict` in `creds`, where Docker credentials are stored for the repository created
together with the new service. `creds` contains the following elements:
* `repo_uri`
* `proxy_endpoint`
* `user`
* `password`

### 3 Push a Docker image to the service repository
With the elements in the `creds` object mentioned above, you can perform the
following sequence of Docker commands to build, tag, and push a Docker image
to the service repository:
```
docker login -u <user> -p <password> <proxy_endpoint>
docker build -t somename:sometag .
docker tag somename:sometag <repo_uri>:sometag
docker push <repo_uri>:<sometag>
docker logout <proxy_endpoint>
```
We recommend, however, to use the convenience methods offered by the services
client, which will automatically perform the above steps for you:
```python
docker_source_folder = '/path/to/a/folder/containing/a/Dockerfile'
srv.build_and_push_docker_image(token, name, docker_source_folder, creds)
```
In case you want to assign a different Docker tag name than `latest` to your
image, add the tag as an optional keyword argument:
```python
docker_source_folder = '/path/to/a/folder/containing/a/Dockerfile'
srv.build_and_push_docker_image(token, name, docker_source_folder, creds, tag='1.1.0')
```

### 4 Update the service with a service definition
The following snippet updates a service, which triggers currently running
instances of the service to be stopped and replaced by a new instance. This
new instance can have a new Docker image, or simply new configuration
parameters.
section.
```python
project = 'cloudifacturing'
service_definition = {
    "container-tag": "latest",
    "memory-reservation": 100,
    "memory-limit": 150,
    "container-port": 80,
    "environment": [
        {"name": "CONTEXT_ROOT", "value": "/{}-{}".format(project, name)}
    ]
}
pprint(srv.update_service(token, name, service_definition))
```
The service-definition object requires the following fields:
* `container-tag` (string): Which Docker image tag to use for the service. If
  no tag was given when pushing Docker images to the service repository, use
  `'latest'` here.
* `memory-reservation` (int): The amount of memory reserved for the service on
  the hosting VM. Make sure to set this to the lowest realistic number, as it
  affects how many services can be started on a single VM, and thus how many
  VMs need to be available for hosting CloudFlow services. (You as a user won't
  see anything of these VMs.) Use the `docker stats` command locally to
  determine how much your service needs. Note that this is not a hard limit, so
  the service will be allowed to allocate more memory.
* `memory-limit` (int): Hard memory limit. If the service tries to allocate
  more than this limit, it will be forcefully killed. Use this number to
  accomodate for memory-usage spikes your service might have.
* `container-port` (int): HTTP port the container listens to for incoming
  connections. For Python-based services using the spyne library (holds for all
  Python code examples), this is usually port 80. For the Java-based code
  examples, this is usually port 8080.
* `environment` (list of dicts): List of dicts with `name`-`value` pairs which
  define the environment variables set to configure the service. Corresponds to
  the `--env-file` argument to the `docker run` command.

TODO: Document convenience function for reading env files

Note: In the example above, the environment variable `CONTEXT_ROOT` is set to
`/<project>-<service-name>`. This corresponds directly to the deployment URL
returned when creating the service (section 1 above). It is important to tell
the Docker container to listen for connections on the same route as where the
service is deployed. Otherwise, no connections will ever reach the service.

## Monitoring a service's status and logs

## Deleting a service
