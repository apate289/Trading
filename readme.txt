1. Create project folder and open it in VS Code.
2. Create Virtual Environment.
    # Windows
    # You can also use `py -3 -m venv .venv`
    python -m venv .venv
    Activate : .\venv\Scripts\activate
    add Interpretor : ./venv/Scripts/python.exe
3. Create app.py

Frontend:
    1. npm install -g @angular/cli
    2. Create a new Angular project by running: ng new angular-python-app --standalone
    3. Change to the project directory: cd angular-python-app
    4. ng build --output-hashing=none
    
	
Docker Hub:
ankitdock133 -> AnkitDoc133
Authenticate using : "docker login" command on cmd

$ docker run --name testmysql -e MYSQL_ROOT_PASSWORD=mySQLdbPSW -d mysql:tag
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

$ docker run -it --network some-network --rm mysql mysql -hsome-mysql -uexample-user -p

