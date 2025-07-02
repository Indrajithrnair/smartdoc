import os, uuid
from flask import Flask, request, render_template, send_from_directory
from dotenv import load_dotenv
from formatter import apply_instruction

# Load config
load_dotenv()
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/format', methods=['POST'])
def format_route():
    docx_file = request.files['file']
    instr = request.form['instruction']

    uid = uuid.uuid4().hex
    in_path = os.path.join(UPLOAD_FOLDER, f"{uid}.docx")
    out_path = os.path.join(OUTPUT_FOLDER, f"{uid}_out.docx")
    docx_file.save(in_path)

    # Apply formatting
    apply_instruction(in_path, instr, out_path)

    return render_template('upload.html', download_url=f"/download/{os.path.basename(out_path)}")

@app.route('/download/<fname>')
def download(fname):
    return send_from_directory(OUTPUT_FOLDER, fname, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)