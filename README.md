# ML_Project

### Software requirements:
1. [github account](https://github.com/)
2. [Heroku account](https://dashboard.heroku.com/login)
3. [Pycharm IDE]
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT tutorial](https://git-scm.com/docs/gittutorial)

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
DEPLOYEMENT - To setup CI/CD pipleine in Heroku we need 3 thins:
1. HEROKU_API_KEY: to_add
2. HEROKU_EMAIL: rivillasm@gmail.com
3. HEROKU_APP_NAME : ml-project-app0
"""
Create and populate the Dockerfile and the .dockerignore file
"""
BUILD DOCKER IMAGE
"""
docker build -t <image_name>:<tagname> .
"""
Note - image name is all lower case and the dot means the location where the dockerfile is located
tagname can be any
"""
To list docker image
"""
docker images
"""
run docker image
"""
docker run -p 5000:5000 -e PORT=5000 5b78ed2614c0
"""
To check running containers in docker
"""
docker ps
"""
to stop the container
docker stop container_id
"""

"""
python setup.py install
"""