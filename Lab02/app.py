from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# -------------------------------------------------
# Khởi tạo (singleton) cho các thuật toán
# -------------------------------------------------
caesar = CaesarCipher()
vigenere = VigenereCipher()
transposition = TranspositionCipher()

# -----------------------------
# Trang chủ
# -----------------------------
@app.route("/")
def home():
    """Hiển thị landing page hoặc redirect."""
    return render_template("index.html")

# -----------------------------
# Trang giao diện Caesar, Vigenère & Transposition
# -----------------------------
@app.route("/caesar")
def caesar_page():
    return render_template("caesar.html")

@app.route("/vigenere")
def vigenere_page():
    return render_template("vigenere.html")

@app.route("/transposition")
def transposition_page():
    return render_template("transposition.html")

# -------------------------------------------------
#  Caesar API
# -------------------------------------------------
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    if request.is_json:  # JSON (fetch)
        data = request.get_json(force=True)
        text = data.get("plain_text", "")
        key = int(data.get("key", 0))
        result = caesar.encrypt_text(text, key)
        return jsonify({"encrypted_text": result})

    text = request.form.get("inputPlainText", "")
    key = int(request.form.get("inputKeyPlain", 0))
    result = caesar.encrypt_text(text, key)
    return (
        f"text: {text}<br/>key: {key}<br/>encrypted text: {result}",
        200,
        {"Content-Type": "text/html"},
    )

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    if request.is_json:
        data = request.get_json(force=True)
        text = data.get("cipher_text", "")
        key = int(data.get("key", 0))
        result = caesar.decrypt_text(text, key)
        return jsonify({"decrypted_text": result})

    text = request.form.get("inputCipherText", "")
    key = int(request.form.get("inputKeyCipher", 0))
    result = caesar.decrypt_text(text, key)
    return (
        f"text: {text}<br/>key: {key}<br/>decrypted text: {result}",
        200,
        {"Content-Type": "text/html"},
    )

# -------------------------------------------------
#  Vigenère API
# -------------------------------------------------
@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    if request.is_json:
        data = request.get_json(force=True)
        text = data.get("plain_text", "")
        key = data.get("key", "")
        result = vigenere.vigenere_encrypt(text, key)
        return jsonify({"encrypted_text": result})

    text = request.form.get("inputPlainText", "")
    key = request.form.get("inputKeyPlain", "")
    result = vigenere.vigenere_encrypt(text, key)
    return (
        f"text: {text}<br/>key: {key}<br/>encrypted text: {result}",
        200,
        {"Content-Type": "text/html"},
    )

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    if request.is_json:
        data = request.get_json(force=True)
        text = data.get("cipher_text", "")
        key = data.get("key", "")
        result = vigenere.vigenere_decrypt(text, key)
        return jsonify({"decrypted_text": result})

    text = request.form.get("inputCipherText", "")
    key = request.form.get("inputKeyCipher", "")
    result = vigenere.vigenere_decrypt(text, key)
    return (
        f"text: {text}<br/>key: {key}<br/>decrypted text: {result}",
        200,
        {"Content-Type": "text/html"},
    )

# -------------------------------------------------
#  Transposition API
# -------------------------------------------------
@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    if request.is_json:
        data = request.get_json(force=True)
        text = data.get("plain_text", "")
        key = int(data.get("key", 0))
        result = transposition.encrypt(text, key)
        return jsonify({"encrypted_text": result})

    text = request.form.get("inputPlainText", "")
    key = int(request.form.get("inputKeyPlain", 0))
    result = transposition.encrypt(text, key)
    return (
        f"text: {text}<br/>key: {key}<br/>encrypted text: {result}",
        200,
        {"Content-Type": "text/html"},
    )

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    if request.is_json:
        data = request.get_json(force=True)
        text = data.get("cipher_text", "")
        key = int(data.get("key", 0))
        result = transposition.decrypt(text, key)
        return jsonify({"decrypted_text": result})

    text = request.form.get("inputCipherText", "")
    key = int(request.form.get("inputKeyCipher", 0))
    result = transposition.decrypt(text, key)
    return (
        f"text: {text}<br/>key: {key}<br/>decrypted text: {result}",
        200,
        {"Content-Type": "text/html"},
    )

# -----------------------------
# Chạy server
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
