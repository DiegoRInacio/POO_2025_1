from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# ✅ Caminho absoluto do banco
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'banco.db')

def conectar_banco():
    conn = sqlite3.connect(DB_PATH)
    return conn

def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.json
    nome = dados.get('nome')
    idade = dados.get('idade')
    email = dados.get('email')

    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)', 
                   (nome, idade, email))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'})

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, idade, email FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()

    lista = [{'id': u[0], 'nome': u[1], 'idade': u[2], 'email': u[3]} for u in usuarios]
    return jsonify(lista)

@app.route('/excluir/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': f'Usuário {id} excluído com sucesso!'})

@app.route('/limpar', methods=['DELETE'])
def limpar_usuarios():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios')
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Todos os usuários foram removidos com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
