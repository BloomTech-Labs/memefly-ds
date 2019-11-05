# Memefly Machine Learning Engineering Deployment

## Version Schema

VERSION Schema {api_version.model_version.data_version}


## AWS Elastic Beanstalk

Zip the whole directory, including Dockerfile. Upload. Ez Pz. Will break under load if being too cheap.


# Package Directory Structure:
```
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
