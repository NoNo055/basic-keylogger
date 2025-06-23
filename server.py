from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.data.decode('utf-8')  
    print(f" {data}")
    with open("received_logs.txt", "a") as f:
        f.write(data + "\n")
    return "Log ", 200

if __name__ == '__main__':
    app.run(port=5000)
