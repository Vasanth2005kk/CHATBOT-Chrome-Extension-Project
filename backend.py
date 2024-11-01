from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

client = Groq(api_key='<api-key>')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/chatbot', methods=['POST'])
def chatbot():
    conversation = request.json.get('conversation')
    response = chat_with_chatbot(conversation)
    if "*" in response:
        response = chatbot_format(response)
    return jsonify({'response': response})

def chatbot_format(string):
    output = ""
    star = 0
    ans = ""
    for i in string:
        if i == "*":
            star +=1
            if star == 2 :
                ans +='<br><h4 style="text-transform: uppercase ;">'
            elif star == 4:
                ans += '</h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                output += ans
                star = 0
                ans = ""
        elif i == "-":
            continue
        else:
            ans +=i
    return output



def chat_with_chatbot(message):
    completion = client.chat.completions.create(
        model="gemma-7b-it",
        messages=[
            {"role": "system", "content": "chat friendly"},
            {"role": "user", "content": message}
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    # Print the entire response to understand its structure
    # print(completion)

    # Extract the response from the model - modify this based on the actual structure
    response_text = completion.choices[0].message.content  # Access the 'content' attribute

    return response_text.strip()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
