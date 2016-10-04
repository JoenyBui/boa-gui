# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines
* Minion Pull Request

        git checkout v1
        git remote add protectionconsultants/pec_gui ssh://git@bitbucket.org/protectionconsultants/pec_gui.git
        git fetch protectionconsultants/pec_gui
        git merge remotes/protectionconsultants/pec_gui/v1

* Requirements
    There are two sets of requirements to output (pip and conda)

        pip list > requirements.txt

        conda env export > environment.yml

    The user needs to have Anaconda installed and then first run the yaml file:

        conda env create -f environment.yml

    and then install the pip file

        pip install -r requirements.txt

    afterwards install local projects and wheels:

        python setup.py develop

        pip install <project>.whl

### Who do I talk to? ###

* Repo owner or admin
Joeny Bui
Eyenunwana Nwoko
 
* Other community or team contact