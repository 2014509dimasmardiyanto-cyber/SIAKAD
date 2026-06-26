import json
import os

FILE_NAME = 'database.json'

def muat_data():
    """Membaca data dari file JSON dengan Try-Catch"""
    try:
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error membaca file: {e}")
        return []

def simpan_data(data):
    """Menyimpan data (List/Array) ke JSON"""
    try:
        with open(FILE_NAME, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error menyimpan file: {e}")