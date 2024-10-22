from flask import Flask, render_template_string, redirect, url_for
import os

app = Flask(__name__)

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


@app.route('/')
def score_server():
    try:
        # Check if the scores file exists
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                # Assuming the score file contains a single number (accumulated score)
                score = file.read().strip()
                if score.isdigit():
                    score_text = f"Current Score: {score} Points"
                else:
                    score_text = "Score file is invalid or corrupted."
        else:
            score_text = "No scores available."

        # HTML for displaying the score
        html = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The current score is:</h1>
            <pre id="score">{score_text}</pre>
            <form action="/wipe" method="post">
                <button type="submit">Reset Score</button>
            </form>
        </body>
        </html>
        """
    except Exception as e:
        # Handle any exceptions and show an error message
        html = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>ERROR:</h1>
            <div id="score" style="color:red">{str(e)}</div>
        </body>
        </html>
        """
    return render_template_string(html)


@app.route('/wipe', methods=['POST'])
def wipe_score_route():
    # Wipe the score by overwriting the score file with 0
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write('0')
        return redirect(url_for('score_server'))
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
