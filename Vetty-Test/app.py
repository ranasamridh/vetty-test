import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the file viewer!"

@app.route('/view_file')
def view_file():
    try:
        # Get filename from URL parameter or default to file1.txt
        filename = request.args.get('filename', default='file1.txt')
        
        # Get start and end line numbers from query parameters
        start_line = request.args.get('start', type=int)
        end_line = request.args.get('end', type=int)

        # Read file content
        file_path = os.path.join('files', filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Slice lines based on start and end line numbers if provided
        if start_line is not None and end_line is not None:
            lines = lines[start_line - 1:end_line]
        
        # Render file content in HTML
        content = ''.join(lines)
        return render_template('file_viewer.html', content=content)
    
    except Exception as e:
        # Handle exceptions gracefully
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
