from urllib.parse import unquote_plus
from flask import Flask, request


app = Flask(__name__)


@app.route("/server_logs", methods=["POST"])
def server_logs():
    get_data = request.get_data(as_text=True)
    data = unquote_plus(get_data)
    print('========================================== LOG ===============================================')
    for data_log in data.split('&'):
        print(data_log)
    return 'Логи получены', 200


if __name__ == "__main__":
    app.run(debug=True)
