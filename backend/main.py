from flask import Flask, request, jsonify, render_template
import requests
from PIL import Image
from io import BytesIO
import base64
import google.generativeai as genai

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure CORS if needed
from flask_cors import CORS
CORS(app)

# Configure the API with your API key
genai.configure(api_key="AIzaSyAr06JCU-JaJHwwkxHdrBiYAALWO1chz7s")

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config)

@app.route('/', methods=['GET'])
def home():
    # Render a simple form for inputting the image URL
    return render_template("index.html")

@app.route('/describe_image', methods=['GET', 'POST'])
def describe_image():
    if request.method == 'POST':
        image_url = request.form['image_url']
    else:
        image_url = request.args.get('image_url')

    prompt = "Describe this image for someone who can't see it. This description will be used to enhance accessibility."

    try:
        if image_url.startswith('data:image'):
            header, encoded = image_url.split(',', 1)
            data = base64.b64decode(encoded)
            img = Image.open(BytesIO(data))
        else:
            response = requests.get(image_url, stream=True)
            img = Image.open(BytesIO(response.content))

        response_model = model.generate_content(contents=[prompt, img], stream=True)
        response_model.resolve()
        description = response_model.text

        return render_template("index.html", image_url=image_url, description=description)

    except Exception as e:
        return render_template("index.html", error=str(e))

@app.route('/describe_image_extension', methods=['GET'])
def describe_image_extension():
    image_url = request.args.get('image_url')
    prompt = request.args.get('prompt', "Describe this image for someone who can't see it. Those description will be used to replace pre-existing alternative text or missing ones related to the images on a web page which this code will be executed. So we need to represent in the best way what the photo are respecting the usage of it in the website.")
    
    try:
        if image_url.startswith('data:image'):
            # Base64 encoded image
            header, encoded = image_url.split(',', 1)
            data = base64.b64decode(encoded)
            img = Image.open(BytesIO(data))
        else:
            # Direct image URL
            response = requests.get(image_url, stream=True)
            if response.headers['Content-Type'] in ['image/jpeg', 'image/jpg', 'image/png']:
                img = Image.open(BytesIO(response.content))
            # elif response.headers['Content-Type'] == 'image/svg+xml' and cairosvg is not None:
            #     # Convert SVG to PNG using CairoSVG
            #     png_data = cairosvg.svg2png(bytestring=response.content)
            #     img = Image.open(BytesIO(png_data))
            else:
                return jsonify(error="Unsupported image format"), 400

        # Generate content using the model, prompt, and image data
        response_model = model.generate_content(contents=[prompt, img], stream=True)
        response_model.resolve()

        # Return the AI-generated description
        return jsonify(description=response_model.text)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
