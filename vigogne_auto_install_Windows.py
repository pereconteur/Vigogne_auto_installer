import os
import subprocess
import platform

def echo_green(message):
    print("\033[32m" + message + "\033[0m")

def echo_yellow(message):
    print("\033[33m" + message + "\033[0m")

def echo_red(message):
    print("\033[31m" + message + "\033[0m")

def check_python_version():
    version_requise = "3.10"
    python_version = platform.python_version()

    if python_version.startswith(version_requise):
        return True
    else:
        echo_red("Python {} n'est pas installé".format(version_requise))
        return False

def check_wget_version():
    try:
        subprocess.check_output(["wget", "--version"])
        return True
    except subprocess.CalledProcessError:
        echo_red("Wget n'est pas installé")
        return False

def check_git_version():
    try:
        subprocess.check_output(["git", "--version"])
        return True
    except subprocess.CalledProcessError:
        echo_red("Git n'est pas installé")
        return False

def check_requirements():
    if check_git_version() and check_wget_version() and check_python_version():
        while True:
            choix = input("\nChoisissez quel poids voulez-vous utiliser pour Vigogne : \n1.7B \n2.13B\n")
            if choix == "1":
                poids_B = "7B"
                poids_b = "7b"
                break
            elif choix == "2":
                poids_B = "13B"
                poids_b = "13b"
                break
            else:
                echo_red("Choix invalide. Veuillez réessayer.")

        while True:
            choix = input("\nVous voulez la version : \n1.instruct \n2.chat\n")
            if choix == "1":
                version_vig = "chat"
                break
            elif choix == "2":
                version_vig = "instruct"
                break
            else:
                echo_red("Choix invalide. Veuillez réessayer.")

        echo_yellow("La version choisie est : {} {}".format(version_vig, poids_B))
        os.chdir("..")
        echo_yellow("Clonage du dépôt GitHub de Vigogne")
        subprocess.call(["git", "clone", "https://github.com/bofenghuang/vigogne.git"])
        os.chdir("vigogne")
        echo_yellow("Installation des dépendances")
        subprocess.call(["pip", "install", "deepspeed"])
        subprocess.call(["pip", "install", "."])
        os.chdir("scripts")
        echo_yellow("Conversion des poids au format HF")
        subprocess.call([
            "python",
            "convert_llama_weights_to_hf.py",
            "--input_dir", "../../llama.cpp/models",
            "--model_size", poids_B,
            "--output_dir", "../../llama-{}-hf".format(poids_B)
        ])

        path = "{}_{}".format(poids_B, version_vig)

        echo_yellow("Lancement de la commande python : export_state_dict_checkpoint.py")
        subprocess.call([
            "python",
            "export_state_dict_checkpoint.py",
            "--base_model_name_or_path", "../../llama-{}-hf".format(poids_B),
            "--lora_model_name_or_path", "bofenghuang/vigogne-{}-{}".format(version_vig, poids_b),
            "--output_dir", "./models/{}".format(path),
            "--base_model_size", poids_B
        ])

        echo_yellow("Téléchargement du tokenizer")
        subprocess.call([
            "wget",
            "-P", "./models",
            "https://huggingface.co/bofenghuang/vigogne-instruct-7b/resolve/main/tokenizer.model"
        ])

        subprocess.call([
            "python", "../../llama.cpp/convert.py", "models/{}".format(path)
        ])

        subprocess.call([
            "../../llama.cpp/quantize",
            "models/{}/ggml-model-f16.bin".format(path),
            "models/{}/ggml-model-q4_0.bin".format(path),
            "q4_0"
        ])

        subprocess.call([
            "../../llama.cpp/main",
            "-m", "models/{}/ggml-model-q4_0.bin".format(path),
            "--color", "-f", "../prompts/{}.txt".format(version_vig),
            "-ins", "-c", "2048", "-n", "256",
            "--temp", "0.1", "--repeat_penalty", "1.1"
        ])

    else:
        echo_red("Les exigences ne sont pas satisfaites.")


check_requirements()
