[markdown basic syntax](https://www.markdownguide.org/basic-syntax/)

create main folder `photo-blog`\
added `readme.md`\
create sub-folder `fastapi-backend`\
create sub-folder `react-backend`

# Github
initiated main folder with git `git init`\
changed master to main branch `git branch --move master main`
created `photo-blog` repo on github.com\
added github repo origin to local folder `git remote add origin https://github.com/nirajgole/photo-blog.git`\
replace local main branch with origin/main `git rebase origin/main`\
push all local changes to origin\
`git . add`\
`git commit -m "created folder structure"`\
`git push`

# MySql Container with Docker
need to install docker desktop on local machine
start mysql container with docker `docker run --name mysqldb -e MYSQL_DATABASE=test -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3306 mysql:latest`

# FastAPI Backend Setup
switch to folder `fastapi_backend`\
to create virtual environment run `py -m virtualenv venv`\
activate virtual env `.\venv\Scripts\activate`\
install fastapi and uvicorn using pip install command: `pip install fastapi sqlalchemy pymysql pymysql[rsa] uvicorn`\
run app `uvicorn main:app --reload`\
get dependencies `pip freeze > requirements.txt`\
access api docs `http://localhost:8000/docs` | `http://localhost:8000/redoc`\
generate python linting configuration `py -m pylint --generate-rcfile > ./pylintrc`
if there is existing requirements file is there, user can install requirement from same `pip install -r .\requirements.txt`

# Authentication and Authorization
install python modules ``\
get secret key `openssl rand -hex 32` -> run this command on `git-bash` terminal

# Generic database migration
install alembic `py -m pip install alembic`\
create ini file at root where main.py resides `alembic init alembic`\
change alembic.ini -> sqlalchemy.url = `your_database_URL`\
to create migration revision files `alembic revision --autogenerate -m "your commit message"`

# React Frontend setup
switch to folder `react_frontend`\
initialize npm project by running `npm create vite .`
- select framework `React`
- select a variant `TypeScript + SWC`
- install dependencies from package.json `npm i`
>[vite](https://vitejs.dev) | [react](https://react.dev) | [typescript](https://www.typescriptlang.org/) | [swc](https://swc.rs/)


# Note:
- To make login work successfully on frontend set allow-access-origins to wildcards and withCredentials=False at both end
- But to set-cookie header work on frontend you need to make credentials true at both end and allow-origins true in frontend and add frontend url to allow-origins of backend