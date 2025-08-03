# socket_reader.py
import socket
import threading

latest_data = {}

def read_socket_data():
    global latest_data
    host = '127.0.0.1'  # Or IP of the data source
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Listening on {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    latest_data = eval(data.decode())  # Use `json.loads` if data is JSON
                except:
                    pass

def start_socket_thread():
    thread = threading.Thread(target=read_socket_data)
    thread.daemon = True
    thread.start()
