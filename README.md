## About The Project

A repository containing a technical test based on https://www.hackerrank.com/challenges/sparse-arrays/problem .
We will answer this problem using several variation modeling real life usage.
The repository also contains an SQL_queries respository answering another test that won't be detailed.

<!-- GETTING STARTED -->
### Prerequisites

To run the different tests you will need to have installed :
- python:3.7
- Docker

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/pteys/Technical_test.git
   ```

<!-- USAGE EXAMPLES -->
## Repository structure

The repository contains tree different ways of answering the https://www.hackerrank.com/challenges/sparse-arrays/problem problem.

- *Part 1 :* A local version running with Python.
- *Part 2 :* A Docker version.
- *Part 3 :* A Server version emulated by a docker running a Rest API

The repository also contains an SQL_queries respository answering another test that won't be detailed.

## Usage

The repository contains tree different ways of answering the https://www.hackerrank.com/challenges/sparse-arrays/problem problem.
The goal of this problem is to find the number of occurrence of a list of queries in a list of strings.

*Examples :
- input :    
    - strings = "ab,ab,abc"
    - queries = "ab,abc,bc"
- output :
{
  "ab": 2, 
  "abc": 1, 
  "bc": 0
}

The strings list will be read as the environment variable *SPARSE_ARRAY_STRINGS*:
   ```sh
   export SPARSE_ARRAY_STRINGS=ab,ab,abc
   ```
The queries list will be given as a parameter in three different ways: 

1) As a parameter
2) As a parameter inside a docker
3) As a POST request.

### Part 1 : Run the script with python by passing the list of queries as parameters.
   ```sh
   python -m main ab,abc,bc
   ```
### Part 2 : Run the script with docker by passing the list of queries as parameters.
Build the image:  ```sh docker build . -t test_mdm*```

Run the container: ```sh docker run -t test_mdm ab,abc,bc ```

### Part 3 : Run the script as a Flask API documented by a swagger inside a docker.

#### Docker usage
Build the image:  ```sh docker build . -t test_mdm*```

Run the container: ```sh docker run -d -p 5000:5000 test_mdm ```

#### Using the Flask app

The Flask API run at http://0.0.0.0:5000/

Swagger documentation : http://0.0.0.0:5000/swagger

API endpoint : http://0.0.0.0:5000/api/sparsearray

The API endpoint expect a POST request with a json body containing a "queries" parameter:
{
  "queries":"ab,abc,bc"
}

Exemple request:

curl -X POST "http://0.0.0.0:5000/api/sparsearray" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{ \"queries\":\"ab,abc,bc\"}"


<!-- CONTACT -->
## Contact

TEYSSERE Pascal - pateyssere@gmail.com

Project Link: https://github.com/pteys/Technical_test.git
