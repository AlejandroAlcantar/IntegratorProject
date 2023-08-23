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
 
##### Nota: Don´t forget to select the new environment at kernel when using VSCode

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

#### Nota: 
  * Every one has its own hooks to represent specific checks on the code
  * The corresponding libraries are contained inside requirements.txt file. They may be installed but nothing will happen if .yaml file does not exist or is empty, or pre-commit has not been initialized on the project for the first time

### Setup pre-commits

* Open your terminal or command prompt, navigate to the root directory of your project
* Pre-commit needs to be installed, at this time it already was by que requirements file

#### Nota: 

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

* In every one of the folders with a link attached there is code and files extracted from the Water_Quality.py file, and functionalities, with sections identified and linted and formatted with pre-commits hooks.
  * All the code separated in modules and classes can be executed in the terminal
### Nota:

  * Change the directory to "IntegratorProject" folder
  * If not active, activate virtual environment

    * source venv/bin/activate
      
  * Windows cmd:

    * venv\scripts\activate.bat
      
  * Run the following:
    
    * python integratorProject\integratorProject.py
   
  # REST API

  * The implementation of REST API was through the application of fastapi, pydantic and uvicorn libraries and the corresponding code can be found in the _____
  * folder of this project (____).
