from flask import Flask, jsonify,request
import json
app = Flask(__name__)

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

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)