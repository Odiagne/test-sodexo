# test-sodexo

## Summary

This repo is an answer to the sodebo test.
The test was about performing clustering with data about CityBike‘s stations in Brisbane.
The input is a json file located at: Odiagne/test-sodexo/data/Brisbane_CityBike.json.
The scripts import the input file, make some cleanings to the data, perform K-means and export data at Odiagne/test-sodexo/output/result.json. 

## Installation

```bash
pip install -r /requirements.txt
```

## Running

To run the code you must create a .env file in the root of the project. 
To make it easier to test, the .env file is removed from the .gitignore so you just have to pull it, no need to create it.
The .env file indicate the name of the input json file and the name of the output file to write at the end.

The command to run the program: 

```bash
cd test-sodexo/scripts/
python3 clustering.py
```

## Unit tests

Unit tests are performed for the script and can be run with:

```bash
python3 -m unittest test_functions
```

## Alternative

If you don't have python installed, you can run the script using Docker.
A Dockerfile is ready t build.
You have to build it with:
```bash
docker build -t test \test-sodexo
```
And run the image with
```bash
docker run test
```
In this case, you will need to need to modify the export_result function in clustering.py in order to write the result weather in a database or in a blob file outside the docker environment. 
