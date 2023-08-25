# Machine Learning Operation
Project inegrator  for the subject Problems resolution with technology application.

# Module 1 - Key concepts of ML systems

## Base-line definition and project scope

Base-line: This the baseline of the project.
* A linear regression model is implemented, which loads a data set (Water Potibility) and applies the StandardScaler transformation to all numeric fields, also applies an 80-20 partition for the training and test sets respectively, achieving a final precision of about 80%.

Scope: 
* The scope of this project is implementation of techniques and good practices to achieve deployment of the full functionality of this code through REST API.

Situation:
* Having access to safe drinking water is crucial for maintaining good health and is considered a fundamental human right. It is an integral aspect of effective health        protection policies at various levels, including national, regional, and local. Investments in water supply and sanitation have proven to be economically advantageous in    certain regions, as the positive impact on health outcomes and reduced healthcare costs outweigh the expenses associated with implementing such interventions.
Drinking an adequate amount of water and staying hydrated has been linked to a decreased risk of urinary tract infections (UTIs), lower blood pressure, and a healthier      heart. Hence, water consumption plays a vital role in maintaining cardiovascular well-being.
Water is the most essential nutrient for our bodies, providing numerous health benefits and safeguarding against illnesses and diseases. Additionally, water is a            fundamental component of a healthy lifestyle.

To know more about the data sets, you can look directly at the Kaggle links: 

* https://www.kaggle.com/code/wadors/proyecto2/notebook
* https://www.kaggle.com/code/monicacinthya/water-potability-eda

## Notebook 
Base-line code may be found at https:
* //github.com/AlejandroAlcantar/IntegratorProject/blob/main/Water_Quality.py.

It was extracted from two notebooks developed by other users on the Kaggle platform.

# Module 2 - Basic concepts and tools for software development

## Virtual environments

* Change the directory to "IntegratorProject" folder.
* Create a virtual environment with Python 3+:
  
  * python3 -m venv venv

  * Windows cmd
  
    * py -3.10 -m venv venv

* Activate the virtual environment

  * source venv/bin/activate
    
  * Windows cmd
  
    * venv\scripts\activate.bat

* Install the other libraries. Run the following command to install the libraries/packages
  * pip install -r requirements.txt

* Requirements file may be consulted
  
  * https://github.com/AlejandroAlcantar/IntegratorProject/blob/main/Requirements.txt
 
##### Note: Don´t forget to select the new environment at kernel when using VSCode

# Continuous use of GitHub

* GitHub was used continuously throughout the development of this project, gradually increasing the content of the repository with each change made
  
  * https://github.com/AlejandroAlcantar/IntegratorProject/commits/main

# Unit tests

* Trabajando en ellas

# Pre-Commits

* Pre-commits were implemented on the project from Water_Quality.py file onward, since this was the first element pre-commits are able to evaluate

   * https://github.com/AlejandroAlcantar/IntegratorProject/blob/main/Water_Quality.py
   
* This are the repos implemented for linting and formatting:
  
  * autopep8
  * flake8
  * isort
  * autoflake

* Configuration file can be found at: https://github.com/AlejandroAlcantar/IntegratorProject/blob/main/.pre-commit-config.yaml

#### Note: 
  * Every one has its own hooks to represent specific checks on the code
  * The corresponding libraries are contained inside requirements.txt file. They may be installed but nothing will happen if .yaml file does not exist or is empty, or pre-commit has not been initialized on the project for the first time

### Setup pre-commits

* Open your terminal or command prompt, navigate to the root directory of your project
* Pre-commit needs to be installed, at this time it already was by que requirements file

#### Note: 

  * If you are installing it for the firs time use:
    
      * pip install pre-commit

  * After creating the .pre-commit-config.yaml file, initialize pre-commit for the project:

    * pre-commit install

  * With the pre-commit hooks installed, you can now make changes to your Python code. When you're ready to commit your changes, run the following command to trigger the pre-commit checks:

    * git commit -m "add pre-commit file"

  * If every check "passed", then you are ready to upload your changes to the repository at GitHub
    
    * git push

# Module 3 - Development of ML models

## Refactorization

* Folders with refactorized code is found in the following directory structure of this project (https://github.com/AlejandroAlcantar/IntegratorProject)
  * api
  * BaseCode
  * DataSet
  * integratorproject
    * docs
    * integratorproject
      * Data
      * Load
      * Models
      * Predictor
      * Preprocess
      * tests
      * train

* All the code separated in modules and classes can be executed in the terminal
    
### Note:

  * Change the directory to "IntegratorProject" folder
  * If not active, activate virtual environment

    * source venv/bin/activate
      
    * Windows cmd:
  
      * venv\scripts\activate.bat
      
  * Run the following:
    
    * python integratorProject\integratorProject.py
   
  # REST API

  * The implementation of REST API was through the application of fastapi, pydantic and uvicorn libraries and the corresponding code can be found in the https://github.com/AlejandroAlcantar/IntegratorProject/tree/main/api
    
  * folder of this project (https://github.com/AlejandroAlcantar/IntegratorProject)
    
    * All libraries are included in requirements file, and are already installed by this point
   
  * The endpoints generated to run the project as an API are
    
    * healthcheck
    * train_new_model
    * predictor
   
  * Run the following command to start House-pricing API locally

    * uvicorn api.main:app --reload
      
  * You can check the endpoints as follows:

    * Access http://127.0.0.1:8000/, you will see a message like this "WaterPotability Regressor is ready to go!"
   
    * ![image](https://github.com/AlejandroAlcantar/IntegratorProject/assets/140922747/2169ba86-7701-4829-aa4d-2545e5d88ae9)

    * Access http://127.0.0.1:8000/docs, the browser will display something like this:
   
  * Try running the following predictions with the endpoint by writing the following values:
    
    * Prediction 1
      * Request body
        * {
  "ph": 0,
  "Hardness": 0,
  "Solids": 0,
  "Chloramines": 0,
  "Sulfate": 0,
  "Conductivity": 0,
  "Organic_carbon": 0,
  "Trihalomethanes": 0,
  "Turbidity": 0
}

        * Response body The output will be:

        * "Resultado predicción: [0]"

    * Prediction 2
      * Request body
        * {
  "ph": 1,
  "Hardness": 0,
  "Solids": 1,
  "Chloramines": 0,
  "Sulfate": 1,
  "Conductivity": 1,
  "Organic_carbon": 1,
  "Trihalomethanes": 0,
  "Turbidity": 1
}

        * Response body The output will be:

        * "Resultado predicción: [1]"

## Complete deployment of all containers with Docker Compose and usage

### Create the network

  * First, create the network AIService by running this command:
    
      * docker network create AIservice
   
### Run Docker Compose

  * Ensure you are in the directory where the docker-compose.yml file is located
  * Run the next command to start the App and Frontend APIs

    * docker-compose -f docker-compose.yml up --build
   
  * You will see something like this:
    *  ✔ Container integratorproject-server-1  Created                                                                                   0.0s
 ✔ Container integratorproject-api-1     Recreated                                                                                 0.1s
Attaching to integratorproject-api-1, integratorproject-server-1
integratorproject-server-1  | INFO:     Will watch for changes in these directories: ['/']
integratorproject-server-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
integratorproject-server-1  | INFO:     Started reloader process [1] using StatReload
integratorproject-api-1     | INFO:     Will watch for changes in these directories: ['/']
integratorproject-api-1     | INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
integratorproject-api-1     | INFO:     Started reloader process [1] using StatReload
integratorproject-server-1  | INFO:     Started server process [8]
integratorproject-server-1  | INFO:     Waiting for application startup.
integratorproject-server-1  | INFO:     Application startup complete.
integratorproject-api-1     | INFO:     Started server process [8]
integratorproject-api-1     | INFO:     Waiting for application startup.
integratorproject-api-1     | INFO:     Application startup complete.

### Checking endpoints in Frontend

* 1 Access http://localhost:3000/ , and you will see a message like this "Water-Potability Model Front-end is ready to go!"
* ![image](https://github.com/AlejandroAlcantar/IntegratorProject/assets/140922747/051a5a7a-ca8c-4c39-baef-4f0cfe17436e)
* 2 Access http://localhost:3000/docs#/
* ![image](https://github.com/AlejandroAlcantar/IntegratorProject/assets/140922747/b228ea66-e845-4d0f-a791-f31cd8bf56c2)

### Contact information

  #### Alejandro Alcantar alcantar.medel@gmail.com

### Gratitude

  * Thank you very much teachers Carlos Mejia, I struggled, but I learned and had fun.

