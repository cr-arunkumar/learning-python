from flask import Flask, jsonify,request
from flask_socketio import SocketIO, emit
import json
import peewee
app = Flask(__name__)
socketio = SocketIO(app,debug=True,cors_allowed_origins='*')

# Load the initial data from the JSON file
json_file_path = 'rest_api/data.json'

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def read_json_file_id(file_path, post_id):
    json_data = read_json_file(file_path)
    post=None
    for post in json_data:
        if post['id'] == post_id:
            post=post
            break    
    return post


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_post_json(new_post):
    data = read_json_file(json_file_path)
    data.append(new_post)
    write_json_file(json_file_path, data)

def update_post_json(post_id, updated_post):
    data = read_json_file(json_file_path)
    for post in data:
        if post['id'] == post_id:
            post.update(updated_post)
            break
    write_json_file(json_file_path, data)

def delete_post_id_json(post_id):
    data = read_json_file(json_file_path)
    data = [post for post in data if post['id']!= post_id]
    write_json_file(json_file_path, data)


@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(read_json_file(file_path=json_file_path))

@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    print(new_post,"-----")
    add_post_json(new_post)
    return jsonify(new_post), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    posts = read_json_file(file_path=json_file_path)
    post = next((post for post in posts if post["id"] == post_id), None)
    if post is not None:
        updated_post = request.get_json()
        update_post_json(post_id, updated_post)
        return jsonify(updated_post)
    else:
        return jsonify({"error": "Post not found"}), 404

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        delete_post_id_json(post_id)
        return jsonify({"message": "Post deleted successfully"}), 204
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500
    
@app.route('/server-metrics', methods=['POST'])
def handle_server_metrics():
    metrics = request.get_json()
    print(f"Received server metrics: {metrics}")
    try:
        print(f"Received server metrics: {json.dumps(metrics,indent=4, sort_keys=True)}")
        return jsonify({"message": "server metrices process successfully"}), 204
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    try:
        posts = read_json_file(file_path=json_file_path)
        post = next((post for post in posts if post["id"] == post_id), None)
        if post is not None:
            post_data = read_json_file_id(file_path=json_file_path, post_id=post_id)
            if post_data:
                return jsonify(post_data)
            else:
                return jsonify({"error": "Post data not found in file"}), 404
        else:
            return jsonify({"error": "Post not found"}), 404
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route("/",methods=['GET','POST'])
def hello():
    return "Hello, World!"

# listening for websocket events on /api/v1/server-metrics endpoint
@socketio.on('connect', namespace="/")
def hello_connect():
    try:
        print("Client connected to /")
    except Exception as e:
        print(f"An error occurred during connection: {e}")

@socketio.on('message', namespace='/api/v1/server-metrics')
def handle_server_metrics_event(metrics):
    try:
        print(f"Received server metrics via WebSocket: {metrics}")
        # Process the metrics as needed
        emit('metrics_response', {'message': 'Metrics processed successfully'})
    except Exception as e:
        print(f"An error occurred while processing metrics: {e}")
        emit('metrics_response', {'error': 'An error occurred while processing metrics'})

@socketio.on('message', namespace='/')
def hello_world_socket(msg):
    try:
        print(f"hello world socket: {msg}")
        # Process the message as needed
        emit('metrics_response', {'message': 'Metrics processed successfully'})
    except Exception as e:
        print(f"An error occurred while processing message: {e}")
        emit('metrics_response', {'error': 'An error occurred while processing message'})

@socketio.on('disconnect', namespace='/api/v1/server-metrics')
def handle_disconnect():
    try:
        print("Client disconnected from /api/v1/server-metrics")
    except Exception as e:
        print(f"An error occurred during disconnection: {e}")

# Run the Flask application
if __name__ == '__main__':
    # app.run(debug=True)
    socketio = SocketIO(app)
    socket_server=socketio.run(app, host='0.0.0.0', port=5001, debug=True,log_output=True)
    # logging web socker server
    # print(f"Web socket server started on {socket_server}")    