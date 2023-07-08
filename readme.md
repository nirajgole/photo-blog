create main folder `photo-blog`\
added `readme.md`\
create sub-folder `fastapi-backend`\
create sub-folder `react-backend`\
initiated main folder with git `git init`\
changed master to main branch `git branch --move master main`
created `photo-blog` repo on github.com\
added github repo origin to local folder `git remote add origin https://github.com/nirajgole/photo-blog.git`\
replace local main branch with origin/main `git rebase origin/main`\
push all local changes to origin\
`git . add`\
`git commit -m "created folder structure"`\
`git push`
# FastAPI Backend Setup
switch to folder `fastapi_backend`\
to create virtual environment run ```py -m virtualenv venv```\
activate virtual env ```.\venv\Scripts\activate```\
install fastapi and uvicorn using pip install command: ```pip install fastapi sqlalchemy pymysql pymysql[rsa] uvicorn```\
run app ```uvicorn main:app --reload```\
get dependencies ```pip freeze > dependencies.txt```\
access api docs ```http://localhost:8000/docs```\
generate python linting configuration ```py -m pylint --generate-rcfile > ./pylintrc```