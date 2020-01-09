## memefly _- An AI powered Meme generator_ - Data Engineer

---

## ETL - version 1

<<insert ETL Architect image>>

## :ballot_box_with_check: TO-DO

### Usage

To create `pipenv` or `conda` virtual environment

1. `Pipenv` method:

- To install: `pipenv install`
- To activate: `pipenv shell`

2. `conda` method:

- To install: `conda env create -f environment.yml`
- To activate: `conda activate memefly-etl`
- To list envs: `conda info --envs`
- To remove env: `conda remove --name memefly-etl --all`

### Phase 1. ETL v0

:point_right: [X] Part 1: Cleaned `Captions.txt` file from `memegenerator.net` dataset

:point_right: [X] Part 2. Scrapped base meme images and combined them to


### Phase 2. ETL v1

:point_right: [X] Part 1. Web Scrapping done in different repo.

:point_right: [X] Part 2. Cleaning using notebooks

:point_right: [X] Part 3. Loading to database with MongoDB wrapper

### Phase 3. ETL v1.1

:point_right: [X] Part 1. Adding new data from WebArchive `memegenerator.net` dataset

:point_right: [X] Part 2. Re-factoring ETL cleaning scripts to automatically dump it to S3 bucket and MongoDB
                  -- [X] Needs MongoDB wrapper
                  -- [ ] Needs S3 wrapper
 

## CHANGELOG

2019-10-26 - repo created, barebone template created, initial scrapping file added to master

2019-10-28 - added S3 functions to upload download images

2019-11-12 and 2019-11-13 - cleaned raw meme text and combined to singular JSON file

2019-11-19 - added S3 links instead of imgflip

2019-11-20 - dumping singular JSON to AWS RDS scrapped instead MongoDB is preferred

2019-11-26 - added MongoDB wrapper file to easily dump and fetch content from MongoDB

2019-11-26 - added WebArchive `memengenerator.net` dataset and updated TODO list
