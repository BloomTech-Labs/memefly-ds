# InceptionV3 Embedding Extraction Endpoint

<<<<<<< HEAD
2019-12-18 - Init.

### Endpoints Usage

```
curl -X POST "http://localhost:8080/invocations" -d '{"instances": [big, bad, image, array]|'
```
=======
2019-12-18 - Init. Created Dockerfile and nginx.conf. Tensorflow Serving REST API uses port 8501. Sagemaker is expected to use port 8080. Thus using NGINX to tunnel external port 8080 traffic to internal 8501 traffic. Sagemaker uses /invocations and /ping endpoints. 

### Endpoints Usage

You can cURL but it will take forever to create a (1, 299, 299, 3) image array of floats. Please see `test_docker_local.py` on how to request using Python.
```
curl -X POST "http://localhost:8080/invocations" -d '{"instances": [big, bad, image, array]|'
```

Return: Python List of length 2048. PLEASE REMEMBER TO CONVERT INTO NUMPY ARRAY.
 
# Subdirectory Structure:
```
├── build_docker.sh        <- Convenience script to build docker image
├── run_docker.sh          <- Convenience script to run Docker image locally
├── push_docker_ecr.sh     <- Convenience script to push Docker image to AWS ECR
├── test_docker_local.py   <- Docker image system testing       
├── dockerfile 
├── nginx.conf             <- NGINX configuration
├── inceptionv3_embeddings <- Tensorflow servable model
│    └── 1                 <- Version
│        ├── saved_model.pb
│        ├── assets
│        └── variables
│
└── README.md
```

# Debugging

- Log into Docker container `docker exec -it <container id> /bin/bash`
- Restart NGINX inside Docker `nginx -s reload`
- Restart Docker container `docker restart <container id>`
>>>>>>> c3a097b... 'rc'
