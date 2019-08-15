# Simple Weather 
Проект создан в рамках тестового задания для компании Improvado

# Setting up a project 
```
function test() {
  console.log("notice the blank line before this function?");
}
```
With Docker
clone first repo
unzip inside src second repo files
create some folders
change settings.py to this.
move requirements.txt to config
install docker:
### Docker dependencies needed using the apt command.
```
sudo apt install -y \
apt-transport-https \
ca-certificates \
curl \
software-properties-common
```
### add the docker key and repository"
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"
```
### update packages
```
sudo apt update
```
### install docker
```
sudo apt install -y docker-ce
```
### After the installation is complete, start the docker service and enable it to launch every time at system boot.
```
sudo systemctl start docker
```
### If not working you will be start docker every time system rebooting
```
sudo systemctl enable docker
```
### check that docker working
```
docker run hello-world
```
### Install Docker-compose
```
sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### check version
```
docker-compose version
```
# Go to folder where you clone Docker project
```
cd ~/SimpleWeatherDocker/
```
### BUild docker project
```
docker-compose build
```    
    
### if you see:  
```
ERROR: yaml.parser.ParserError: while parsing a block mapping
  in "./docker-compose.yml", line 1, column 1
expected <block end>, but found '<block mapping start>'
  in "./docker-compose.yml", line 2, column 3
```
### got to [yaml](yaml-online-parser.appspot.com) and check your docker-compose.yaml

### Deploy poject
```
docker-compose up -d
```
### check that build and start was successful
```
docker-compose ps
docker-compose images
```
###
```
sudo docker inspect --format="{{.Id}}" dg01 <--- Django Image name
```
### Super User creation From above command copy id and
```
sudo docker exec -it dg01_id python manage.py createsuperuser
```
###
Setup Cron Task Manager:


How to control:


# To Develop:
Clone second repo

Install postgress
    https://djbook.ru/examples/77/
    sudo apt-get install postgresql postgresql-server-dev-9.5
    sudo -u postgres psql postgres- call postgress console terminal
    \password postgres - set passwrod I set 123upc098
        create user user_admin with password '123upc098';
        alter role user_admin set client_encoding to 'utf8';
        alter role user_admin set default_transaction_isolation to 'read committed';
        alter role user_admin set timezone to 'UTC';
        create database django_api_db owner user_name;

go to develop branch

set inside settings.py this:
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_api_db',
            'USER': 'user_admin',
            'PASSWORD': '123upc098',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

run commannds:
    pip3 install -r requirements.txt
    python3 manage.py collectstatic --no-input
    python3 manage.py makemigrations : after database changes
    python3 manage.py migrate : after database changes
    python3 manage.py runserver

Server started

# About API
## Api urls 2 apis describe both

site/api/v1/weather
site/api/v1/weather/?city_name={city_name}
site/api/v1/parse/?city_name={city_name}
site/api/v1/parse/?city_name={city_name|city_name|city_name}


# About parsers
How to create each type of parsers
functions to ovveride
psevdo example
