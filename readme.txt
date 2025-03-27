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
	5. ng serve
    6. ng generate component 'component-name' // to create new componenet    
	
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

RabbitMQ (Message Queue):
	Docker Setup FOr RabbitMQ:
		Create a docker-compose.yaml file
			version: '3.8'

			services:
			rabbitmq:
				image: rabbitmq:3-management
				container_name: rabbitmq
				ports:
				- '5672:5672'
				- '15672:15672'
				environment:
				RABBITMQ_DEFAULT_USER: guest
				RABBITMQ_DEFAULT_PASS: guest
		Start the RabbitMQ container:
			docker-compose up -d
	
	Add user to RabbitMQ:(not Tested with CLI)
		RUN rabbitmqctl add_user {username} {password}
		RUN rabbitmqctl add_user "Ankit" "Ankit@134"
		RUN rabbitmqctl set_user_tags {username} administrator
		RUN rabbitmqctl set_permissions
	Application Development:
		Implement the RabbitMQ class (rabbitmq.py):
			Create a file named main.py in the root of your project directory. Add the following content to the file.
			This script connects to RabbitMQ and starts consuming messages from a queue named test_queue.
		Create the publisher.py script:
			Create a file named publisher.py in the root of your project directory. Add the following content to the file.
			This script publishes a test message to the test_queue.With these scripts in place, you are ready to run and test your application.
	Running the Application:
		Start the RabbitMQ server
			Run the main.py script to start the RabbitMQ server and begin consuming messages from the test_queue:
				python main.py -> You should see a message indicating that the connection to RabbitMQ was established successfully. 
				The script will continue running and wait for messages to consume from the test_queue.
		Publish a test message:
			Open a new terminal window or tab, and run the publisher.py script to publish a test message to the test_queue:
				python publisher.py -> You should see a message indicating that the test message was published successfully. 
				The main.py script should also display the received message, indicating that the message was successfully consumed from the test_queue.	
	Example Output:
		When you run main.py, you should see something like this:
			Connection to RabbitMQ established successfully.
			Received message: b'Test message'
		When you run publisher.py, you should see something like this:
			Sent message to queue test_queue: Test message
			Test message published successfully.
	
