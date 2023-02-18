from flask import Blueprint, current_app, abort, request, render_template
import openai

bp = Blueprint('chatgpt', __name__)

@bp.route('', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chatgpt.html')
    
    openai.api_key = current_app.config.get('APIKEY', None)
    if openai.api_key is None:
        abort(500)
    prompt = None
    try:
        prompt = request.get_json()["prompt"]
    except Exception as e:
        abort(500, "invalid input data")
    response = generate_response(prompt)
    return response


def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()