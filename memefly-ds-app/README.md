# Memefly Machine Learning Engineering Deployment

## Version Schema

VERSION Schema {api_version.model_version.data_version}

<<<<<<< HEAD
=======
## Endpoints Usage

1. ROUTE: `/get-meme-names`
 
METHOD: `GET`
OUTPUT: 
```
[
    "Original-Stoner-Dog",
    "Musically-Oblivious-8th-Grader",
    "Hedonism-Bot",
    "Joe-Biden",
    "Gangnam-Style",
    "Scumbag-Boss",
    "Archer",
    "Lame-Pun-Coon",
    "Scumbag-Steve",
    "Maury-Lie-Detector",
    "Slowpoke",
    ...
]
```

2. ROUTE: `/generate-meme-text` 

METHOD: `POST`

INPUT: 
```
{
    "meme_name": "y-u-no"
}
```

OUTPUT: 
```
{
    "meme_text": "meme generator y u no let me delete mistakes"
}
```
# Deploying Model Endpoints

## Local REST API

Go into the `package` directory, and run 

```python run.py```

Or, in the same directory,

```./run.sh```

## Docker REST API

Container needs to be binded to `0.0.0.0` to be accessible from outside.

To build Docker image, run:

```./scripts/build_api_docker.sh```

The built Docker image can be run locally with: 

```./scripts/run_api_docker.sh```

or

```docker run -p 8000:8000 --name memefly_api -it --rm memefly_api```

To test the API endpoint locally, try:

```curl -X POST -H "Content-Type: application/json" -d '{"meme_url": "1st-World-Canadian-Problems"}' http://0.0.0.0:5000/```

```curl -X POST -H "Content-Type: application/json" -d '{"meme_url": "Y-U-No"}' http://0.0.0.0:5000/```

```curl -X POST -H "Content-Type: application/json" -d '{"meme_url": "Y-U-No"}' http://0.0.0.0:5000/```

```curl -X POST -H "Content-Type: application/json" -d '{"meme_url": "confession-kid"}' http://0.0.0.0:5000/```
>>>>>>> c3a097b... 'rc'

## AWS Elastic Beanstalk

Zip the whole directory, including Dockerfile. Upload. Ez Pz. Will break under load if being too cheap.

<<<<<<< HEAD

# Package Directory Structure:
```
=======
## AWS Sagemaker

Run Bash scripts inside img_emb_endpoint. Good luck getting around Sagemaker JSON payload limit.

# Package Directory Structure:
```
├── run.sh                
├── build_api_docker.sh   
├── run_api_docker.sh     
├── run.py                
>>>>>>> c3a097b... 'rc'
├── api                   
│    ├── app.py
│    ├── endpoints.py     
│    ├── config.py        
│    ├── validation.py    
│    └── pipeline         
│          ├── ingesting.py
│          ├── preprocessing.py
│          └── inferencing.py
├── img_emb_endpoint      <- Tensorflow Serving Deployment
├── tests                 
├── cors-test
├── logs                   
├── VERSION
├── Dockerfile           
├── requirements.txt
└── README.md
```

# Change log

2019-12-17 - Separating models serving from machine learning endpoints. Models now served using TF Serving.

2019-12-03 - 3.3.2 API, release 3, refactored added Beam Search, updated beam width to 1

2019-11-23 - 2.2.2 API, refactored env to config. Added test cases.

2019-11-20 - 2.2.2 API release 2, now with url and bounding box, model v2, data v2

2019-11-13 - 0.2 Release, Refactored.

2019-11-08 - 0.1 Release                                                  
