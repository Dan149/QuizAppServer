import os
import json

__version__ = "0.0.1"


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Main:
    def __init__(self) -> None:
        self.get_json_config()

    def get_json_config(self):
        s = input("Créer nouveau fichier de configuration de quiz ? [O/n]: ")
        if s == "n" or s == "N":
            file_path = input(
                "Entrer le nom d'un fichier de configuration JSON valide (présent dans ce dossier): "
            )
            if os.path.exists(file_path) and file_path.split(".")[-1] == "json":
                self.file_path = file_path
                print("Fichier de configuration: OK")
            else:
                print("Erreur: fichier de configuration invalide ou introuvable.")
                quit()
        else:
            new_file = input("Entrer le nom du nouveau fichier de configuration: ")
            if len(new_file.split(".")) == 1 or new_file.split(".")[-1] != "json":
                new_file += ".json"
            elif new_file.split(".")[-1] == "json":
                pass
            else:
                print("Erreur: nom invalide.")
                quit()
            self.create_new_json_config_file(new_file)

    def create_new_json_config_file(self, file_name):
        content = []
        while True:
            print(
                f"""Nouveau Quiz: configuration
                
              Informations:
                Nombre de questions: {len(content)}
                Nom du fichier: {file_name}
              Commandes:
                N - Nouvelle question
                S - Sauvegarder et utiliser le fichier de configuration"""
            )
            s = input("\nSéléction: ")
            if s == "N" or s == "n":
                question_name = input("Entrer la question: ")
                question_answers = input(
                    "Entrer les réponses à la question, séparés par des ; (max 4 réponses): "
                )
                question_valid_answer = input(
                    "Entrer le numéro de la réponse valide (1, 2, 3 ou 4): "
                )
                if (
                    len(question_answers.split(";")) <= 4
                    and int(question_valid_answer) <= len(question_answers.split(";"))
                    and int(question_valid_answer) > 0
                ):
                    content.append(
                        {
                            "question": question_name,
                            "answers": question_answers.split(";"),
                            "validAnswerIndex": int(question_valid_answer) - 1,
                        }
                    )
                    clear()
                    print("Question ajoutée avec succès !")
                else:
                    clear()
                    print("Erreur: paramètres invalides")
            elif s == "S" or s == "s":
                with open(file_name, "w+") as config_file:
                    json.dump(content, config_file)
                print("Fichier de configuration crée avec succès !")
                break
            else:
                clear()


###

Main()
