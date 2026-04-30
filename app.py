#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

SCORES_FILE = os.path.join(os.path.dirname(__file__), 'scores.json')


def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_scores(scores):
    with open(SCORES_FILE, 'w', encoding='utf-8') as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/scores', methods=['GET'])
def get_scores():
    scores = load_scores()
    scores.sort(key=lambda x: x['score'], reverse=True)
    return jsonify(scores[:10])


@app.route('/api/scores', methods=['POST'])
def post_score():
    data = request.get_json()
    name = str(data.get('name', 'Player'))[:20].strip() or 'Player'
    score = int(data.get('score', 0))
    level = int(data.get('level', 1))
    lines = int(data.get('lines', 0))

    scores = load_scores()
    entry = {
        'name': name,
        'score': score,
        'level': level,
        'lines': lines,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
    }
    scores.append(entry)
    scores.sort(key=lambda x: x['score'], reverse=True)
    save_scores(scores[:100])

    top10 = scores[:10]
    rank = next((i + 1 for i, s in enumerate(top10)
                 if s['score'] == score and s['name'] == name), None)
    return jsonify({'ok': True, 'rank': rank})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
