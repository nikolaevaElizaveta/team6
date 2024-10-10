# Twitter-like System

## Description

This is a simple Twitter-like system that allows users to register, post short messages, view them, and like them. The system consists of three services:

1. **User Service** - Manages user registration and authentication.
2. **Message Service** - Manages posting and retrieving messages.
3. **Like Service** - Manages liking messages.

## Installation

Before you begin, make sure you have Python and pip installed.

### Install Dependencies

Make sure you have the necessary libraries installed:

```bash
pip install Flask Flask-RESTful requests
```

## Running the Services

You can run all services simultaneously using the run_services.py script. This script will start all three services in separate processes.

### Start All Services

Open a terminal and navigate to the project directory:

```bash
cd path\to\your\project
```

Run the services using the script:

```bash
python run_services.py
```
## Example Requests

Once all services are running, you can send requests to the services. Here are some example requests:

### 1. Register a User
```bash
Invoke-WebRequest -Uri http://localhost:5000/register -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"username": "your_username"}'
```

### 2. Post a Message
```bash
Invoke-WebRequest -Uri http://localhost:5001/messages -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"username": "your_username", "message": "Hello, world!"}'
```

### 3. Get Feeds
```bash
Invoke-WebRequest -Uri "http://localhost:5002/feed" -Method Get
```

### 4. Like a Message
```bash
Invoke-WebRequest -Uri http://localhost:5002/like -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"message_id": 1, "username": "your_username"}'
```

### 5. Get a Number of Likes
```bash
Invoke-WebRequest -Uri "http://localhost:5003/likes?message_id=1" -Method Get
```

## Conclusion

You now have a working system that allows users to register, post messages, view them, and like them. If you have any questions, feel free to reach out for help!
Make sure to replace `path\to\your\project` with the actual path to your project. 
If you encounter any issues while running the services, you can use three separate terminals. Open a terminal and navigate to each service directory, then run the service. 
Additionally, you can send requests using a fourth terminal with the command examples provided above.


