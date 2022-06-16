# ML_Project

### Software requirements:
1. [github account](https://github.com/)
2. [Heroku account](https://dashboard.heroku.com/login)
3. [Pycharm IDE]
4. [GIT cli](https://git-scm.com/downloads)

Creating conda environment
"""
conda create -p venv python==3.7 -y
or
use File|Settings|Project|Python Interpreter and create a new conda environment in the 'venv' folder within the project
"""
conda activate venv/
"""
conda env list
"""
pip install -r requirements.txt
To add files to git
"""
git add .   or the file name instead of .
"""
Note: To ignore file or folder from git we can write the name of the file/folder in the .gitignore file
"""
To check all versions maintained by git
"""
git log
"""
To create a version/commit all changes by git
"""
git commit -m "message"
"""
To send version/changes to github
"""
git push origin main
"""
To check remote url
"""
git remote -v
"""