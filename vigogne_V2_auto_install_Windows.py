import os
import subprocess

def echo_green(message):
    print(message)

def echo_yellow(message):
    print(message)

def echo_red(message):
    print(message)

def check_python_version():
    version_requise = "3.10"
    python_version = subprocess.check_output(["python", "--version"]).decode("utf-8").strip()

    if f"Python {version_requise}" in python_version:
        return True
    else:
        echo_red(f"Python {version_requise} n'est pas installé")
        return False

def check_wget_version():
    try:
        wget_version = subprocess.check_output(["wget", "--version"]).decode("utf-8")
        if "GNU Wget" in wget_version:
            return True
        else:
            echo_red("Wget n'est pas installé")
            return False
    except FileNotFoundError:
        echo_red("Wget n'est pas installé")
        return False

def check_git_version():
    try:
        git_version = subprocess.check_output(["git", "--version"]).decode("utf-8")
        if "git version" in git_version:
            return True
        else:
            echo_red("Git n'est pas installé")
            return False
    except FileNotFoundError:
        echo_red("Git n'est pas installé")
        return False

def chooseYourLlamaModel():
    poids_llama = ""
    while True:
        choix = input("\nAvant de commencer, voulez-vous utiliser les modèles basés sur les anciens poids de LLama ou les derniers sortis le 18/07/2023 (pas besoin d'avoir les poids de Llama !) :\n1 = Ancien Poids (env. 420K Data)\n2 = Les derniers sortis le 18/07/2023\n")
        if choix == "1":
            poids_llama = "llama-ancien"
            break
        elif choix == "2":
            poids_llama = "llama-2"
            break
        else:
            echo_red("Choix invalide. Veuillez réessayer.")
    return poids_llama

def chooseYourVigogneType():
    while True:
        choix = input("\nChoisissez quel modèle voulez-vous utiliser pour Vigogne :\n1 = Chat (env. 420K Data)\n2 = Instruct (env. 420K Instruction data)\n")
        if choix == "1":
            type_vig = "chat"
            break
        elif choix == "2":
            type_vig = "instruct"
            break
        else:
            echo_red("Choix invalide. Veuillez réessayer.")
    return type_vig

def chooseYourVigogneModel(poids_llama_choice, type_vig_choice):
    model_vig = ""
    poids_B = ""
    if poids_llama_choice == "llama-ancien":
        if type_vig_choice == "chat":
            while True:
                choix = input("\nChoisissez votre modèle (en fonction de celui que vous avez téléchargé):\n1 = 7b\n2 = 13b\n")
                if choix == "1":
                    model_vig = "vigogne-7b-chat"
                    poids_B = "7B"
                    break
                elif choix == "2":
                    model_vig = "vigogne-13b-chat"
                    poids_B = "13B"
                    break
                else:
                    echo_red("Choix invalide. Veuillez réessayer.")
        else:
            while True:
                choix = input("\nChoisissez votre modèle (en fonction de celui que vous avez téléchargé):\n1 = 7b\n2 = 13b\n3 = 33b\n")
                if choix == "1":
                    model_vig = "vigogne-7b-instruct"
                    poids_B = "7B"
                    break
                elif choix == "2":
                    model_vig = "vigogne-13b-instruct"
                    poids_B = "13B"
                    break
                elif choix == "3":
                    model_vig = "vigogne-33b-instruct"
                    poids_B = "33B"
                    break
                else:
                    echo_red("Choix invalide. Veuillez réessayer.")
    else:
        if type_vig_choice == "chat":
            while True:
                choix = input("\nChoisissez votre modèle (en fonction de celui que vous avez téléchargé):\n1 = 7b\n")
                if choix == "1":
                    model_vig = "vigogne-2-7b-chat"
                    poids_B = "7B"
                    break
                else:
                    echo_red("Choix invalide. Veuillez réessayer.")
        else:
            while True:
                choix = input("\nChoisissez votre modèle (en fonction de celui que vous avez téléchargé):\n1 = 7b\n2 = 13b\n")
                if choix == "1":
                    model_vig = "vigogne-2-7b-instruct"
                    poids_B = "7B"
                    break
                elif choix == "2":
                    model_vig = "vigogne-2-13b-instruct"
                    poids_B = "13B"
                    break
                else:
                    echo_red("Choix invalide. Veuillez réessayer.")
    return model_vig, poids_B

def goForVigogneInstallation(modele_choice, poids_choice, chat_or_instruct):
    echo_yellow(f"La version choisie est : {modele_choice} {poids_choice}")
    os.chdir("..")

    while True:
        choix = input("\nAvez-vous déjà installé le repo de Vigogne sur GitHub "
                      "ou voulez-vous que je m'en charge ? :\n1 = Oui\n2 = Non\n")
        if choix == "1":
            echo_yellow("Clonage du dépôt GitHub de Vigogne")
            subprocess.run(["git", "clone", "https://github.com/bofenghuang/vigogne.git"])
            break
        elif choix == "2":
            break
        else:
            echo_red("Choix invalide. Veuillez réessayer.")

    os.chdir("vigogne")
    echo_yellow("Installation des dépendances")

    while True:
        choix = input("\nAvez-vous déjà installé les dépendances "
                      "ou voulez-vous que je m'en charge ? :\n1 = Oui\n2 = Non\n")
        if choix == "1":
            subprocess.run(["pip", "install", "deepspeed"])
            subprocess.run(["pip", "install", "."])
            break
        elif choix == "2":
            break
        else:
            echo_red("Choix invalide. Veuillez réessayer.")

    os.chdir("scripts")
    echo_yellow("Conversion des poids au format HF")
    echo_yellow("Lancement de la commande python : export_state_dict_checkpoint.py")
    path = f"{modele_choice}_path"
    commandExportState = [
        "python",
        "export_state_dict_checkpoint.py",
        "--base_model_name_or_path", f"bofenghuang/{modele_choice}",
        "--output_dir", f"./models/{path}",
        "--base_model_size", f"{poids_choice}"
    ]
    subprocess.run(commandExportState, check=True)

    echo_yellow("Téléchargement du tokenizer")
    commandDownloadTokenizer = [
        "wget", "-P",
        "./models",
        f"https://huggingface.co/bofenghuang/{modele_choice}/resolve/main/tokenizer.model"
    ]
    subprocess.run(commandDownloadTokenizer, check=True)

    echo_yellow("Conversion...")
    commandConvert = [
        "python",
        "../../llama.cpp/convert.py",
        f"models/{path}"
    ]
    subprocess.run(commandConvert, check=True)

    echo_yellow("Quantization...")
    commandQuantize = [
        "../../llama.cpp/quantize",
        f"models/{path}/ggml-model-f16.gguf",
        f"models/{path}/ggml-model-q4_0.bin",
        "q4_0"
    ]
    subprocess.run(commandQuantize, check=True)

    echo_yellow("Lancement de l'IA")
    if chat_or_instruct == "instruct":
        subprocess.run([
            "../../llama.cpp/main.exe", "-m", f"./models/{path}/ggml-model-q4_0.bin", "--color", "-f",
            f"../prompts/instruct.txt", "-ins", "-c", "2048", "-n", "256", "--temp", "0.1",
            "--repeat_penalty", "1.1"
        ])
    else:
        subprocess.run([
            "../../llama.cpp/main.exe", "-m", f"./models/{path}/ggml-model-q4_0.bin", "--color", "-f",
            f"../prompts/chat.txt", "--reverse-prompt", '"<|user|>:"',
            "--in-prefix", '" "', "--in-suffix", '"<|assistant|>:"',
            "--interactive-first", "-c", "2048", "-n", "-1", "--temp", "0.1"
        ])

def check_requirements():
    result_python = check_python_version()
    result_wget = check_wget_version()
    result_git = check_git_version()

    if result_python and result_wget and result_git:
        llama_model = chooseYourLlamaModel()
        type_vig = chooseYourVigogneType()
        choice = chooseYourVigogneModel(llama_model, type_vig)
        model_vig, poids_B = choice
        goForVigogneInstallation(model_vig, poids_B, type_vig)
    else:
        print(result_python)
        print(result_wget)
        print(result_git)

check_requirements()
