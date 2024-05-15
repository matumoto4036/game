from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 既存のオセロのロジック関数（initialize_board, print_board, make_move など）はここに含めます。

@app.route('/')
def index():
    return render_template('index.html')  # オセロのボードを表示するHTMLページを返す

@app.route('/move', methods=['POST'])
def move():
    # フロントエンドから送信された手のデータを取得
    data = request.json
    board = data['board']
    player = data['player']
    move = data['move']  # moveは(row, col)の形式であることを想定

    # 手を実行
    if make_move(board, player, move[0], move[1]):
        return jsonify(success=True, board=board)
    else:
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)