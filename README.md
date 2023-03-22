# Predicting-Insurance-Premium

### Introduction

```
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an insurance policy rather han the ineffective part.

The insurance.csv dataset contains 1338 observations (rows) and 7 features (columns). The dataset contains 4 numerical features (age, bmi, children and expenses) and 3 nominal features (sex, smoker and region) that were converted into factors with numerical value desginated for each level.
```

### Model

```
Adaboost regression model is used for this problem.
```

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Step 3 - git

```bash
git --version
```

### Git commands

If you are starting a project and you want to use git in your project

```
git init
```
Note: This is going to initalize git in your source code.

OR

You can clone exiting github repo
```bash
git clone <github_url>
```
Note: Clone/ Downlaod github repo in your system

Add your changes made in file to git stagging are
```bash
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to staging are

### Create commits
```bash
git commit -m "message"
git push origin main
```
Note: origin--> contains url to your github repo main--> is your branch name

To push your changes forcefully.
```bash
git push origin main -f
```
To pull changes from github repo

```bash
git pull origin main
```
Note: origin--> contains url to your github repo main--> is your branch name

.env file has


```bash
MONGO_DB_URL="mongodb://localhost:27017"
AWS_ACCESS_KEY_ID="aagswdiquyawvdiu"
AWS_SECRET_ACCESS_KEY="sadoiuabnswodihabosdbn"
```

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

```
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_REGION =
AWS_ECR_LOGIN_URI =
ECR_REPOSITORY_NAME =
BUCKET_NAME =
MONGO_DB_URL =
```
