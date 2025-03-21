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
Command running:
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=mydocker133 -d mysql:latest

$ docker run -it --network some-network --rm mysql mysql -hsome-mysql -uexample-user -p
Build Docker Image:
	#The -t flag tags your image with a name. (welcome-to-docker in this case). And the . lets Docker know where it can find the Dockerfile.
	Docker Build command : docker build -t welcome-to-docker . 
	Run Container:
		Once the build is complete, an image will appear in the Images tab. Select the image name to see its details. Select Run to run it as a container. In the Optional settings remember to specify a port number (something like 8089).
	View Docker Frontend on port:
		You now have a running container. If you don't have a name for your container, Docker provides one. View your container live by selecting the link below the container's name.
	
Run Docker Hub images:
	You can search images by selecting the bar at the top, or by using the Ctrl + K shortcut. Search for welcome-to-docker to find the image used in this guide.
	Run the Image:
		Select Run. When the Optional settings appear, specify the Host port number 8090 and then select Run. You can also select View on Hub to learn more about an image.
	Explore the Container:
		Go to the Containers tab in Docker Desktop to view the container.