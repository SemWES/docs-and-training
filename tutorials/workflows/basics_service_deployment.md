# Tutorial: Service creation and deployment
This tutorial shows you how to create a simple service using one of our service templates. Additionally, you will learn how to deploy you service on the SemWES machines using our automated deployment tools.

## Step 1 - Adapt service template

1. Open a remote shell to your VM.
2. Navigate to the location of the demo services (`<path/to/doc>/docs-and-training/code_examples/Python/app_simple/`).
3. Edit the file "env", adapt the CONTEXT_ROOT, e.g, to `/my-demo`.

```
# CONTEXT_ROOT defines the deployment location relative to the host.
CONTEXT_ROOT=/my-demo
```

## Step 2 - Deploy service using `clfpy_cli`

1. Now, start `clfpy_cli` in your remote shell, and enter your user credentials and project.
2. To select the services client, enter

 ```
 client services
 ```

3. Create a new service by choosing a short name (only lower-case letters, numbers and hyphens, e.g `my-test-service1`), and enter

```
create_new my-test-service1
```

4. Answer with `N` to the question on a custom health check.
5. To check the list of available services, enter `ls`. You should see your service along with its deployment URL in the list.
6. Build the docker image and push it to the SemWES repository using the following command, where the path to the docker source folder is something like `<path/to/doc>/docs-and-training/code_examples/Python/app_simple`. This process may take a short while.

```
push_docker_image my-test-service1 <path_to_docker_source_folder>
```

7. One final step to deploy your service is to run the following command to update the service definition and to start the service. For the basic services you can stick to the default values for `memory reservation`, `memory limit` and `container port`. Your `environment-definition file` should be available at `<path/to/doc>/docs-and-training/code_examples/Python/app_simple/env` (the file you edited in Step 1.3).

```
update my-test-service1
```
After the script has executed it might take a short moment until your service is available.

## Step 3 - Inspect your service's deployment

1. You can check the status of you service by running: 

```
status my-test-service1
```

2. Also, you can have a look at the service's logs using:

```
logs my-test-service1
```

3. Finally, your service should be available under the following url:

```
https://srv.hetcomp.org/<project>-<service_name><CONTEXT_ROOT>
```

Using the values from this example this should be:
	
```
https://srv.hetcomp.org/demo-my-test-service1/my-demo
```

4. You can have a look at the service's wsdl (using a browser) at:

```
https://srv.hetcomp.org/<project>-<service_name><CONTEXT_ROOT>?wsdl
```

	Using the values from this example this should be:
	
```
https://srv.hetcomp.org/demo-my-test-service1/my-demo?wsdl
```

## Conclusion
After finishing this tutorial you should have a basic understanding of how to adapt our service templates to your needs, and how to deploy this service using our automated deployment tool integrated with`clfpy_cli`.

For an in-depth documentation of the deployment process head over to https://github.com/SemWES/docs-and-training/blob/master/service_implementation/deployment_automated.md .

To learn more about the different templates and how to further adapt them to your needs, check their documentation on github, e.g. https://github.com/SemWES/docs-and-training/tree/master/code_examples/Python/app_simple .