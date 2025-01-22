import logging

logging.basicConfig(
    filename="error.log", 
    level=logging.ERROR, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(message):
    """message d'erreur"""
    logging.error(message)

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        log_error("Le fichier n'a pas été trouvé.")
        print("Erreur : Le fichier est introuvable.")


read_file("fichier_inexistant.txt")
