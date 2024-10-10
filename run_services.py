import subprocess 
import os 
 
user_service_path = os.path.join(os.getcwd(), 'user_service') 
message_service_path = os.path.join(os.getcwd(), 'message_service') 
like_service_path = os.path.join(os.getcwd(), 'like_service') 
 
user_service = subprocess.Popen(['python', 'app.py'], cwd=user_service_path) 
message_service = subprocess.Popen(['python', 'app.py'], cwd=message_service_path) 
like_service = subprocess.Popen(['python', 'app.py'], cwd=like_service_path) 
 
print("press Ctrl+C to exit") 
 
try: 
    user_service.wait() 
    message_service.wait() 
    like_service.wait() 
except KeyboardInterrupt: 
    print("Exitting...") 
    user_service.terminate() 
    message_service.terminate() 
    like_service.terminate()
