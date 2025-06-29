from flask import Flask, request, jsonify
import sys
import os

# Add the directory of jarvis_ai.py to sys.path
# This assumes jarvis_ai.py is in the same directory as app.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import jarvis_ai
except ImportError:
    # Fallback if running in a slightly different environment where jarvis_ai is discoverable
    # This can happen in some testing/deployment scenarios.
    # If this still fails, an error will be raised.
    from . import jarvis_ai


app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    """
    API endpoint to interact with the Jarvis AI.
    Expects a JSON payload with a 'message' key.
    Returns a JSON response with the AI's 'reply'.
    """
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({'error': 'Missing "message" in request JSON'}), 400

    user_message = data['message']

    if not isinstance(user_message, str):
        return jsonify({'error': '"message" must be a string'}), 400

    if not user_message.strip():
        return jsonify({'error': '"message" cannot be empty'}), 400

    ai_reply = jarvis_ai.get_response(user_message)

    return jsonify({'reply': ai_reply})

@app.route('/', methods=['GET'])
def home():
    """
    A simple GET endpoint to confirm the API is running.
    """
    return "Jarvis AI API is running. Use the /chat endpoint with POST to interact."

if __name__ == '__main__':
    # Note: For development only. For production, use a WSGI server like Gunicorn.
    app.run(host='0.0.0.0', port=5000, debug=True)
