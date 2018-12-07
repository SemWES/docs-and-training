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
import clfpy

interface_url = 'https://api.hetcomp.org/servicectl-1/'
```

TODO: Continue here!


## Monitoring a service's status and logs

## Deleting a service
