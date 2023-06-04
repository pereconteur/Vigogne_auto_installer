#!/bin/bash

# Function to print a message in green
function echo_green {
  echo -e "\033[32m$1\033[0m"
}

function echo_yellow {
  echo -e "\033[33m$1\033[0m"
}


# Function to print a message in red
function echo_red {
  echo -e "\033[31m$1\033[0m"
}

function check_python_version {
    version_requise="3.10"

    python_version=$(python3 --version 2>&1)

    if [[ $python_version == *"Python $version_requise"* ]]; then
        echo "true"
    else
        echo_red "Python $version_requise n'est pas installé"
    fi
}

function check_wget_version {
    wget_version=$(wget --version 2>&1)

    if [[ $wget_version == *"GNU Wget"* ]]; then
        echo "true"
    else
        echo_red "Wget n'est pas installé"
    fi
}

function check_git_version {
    git_version=$(git --version 2>&1)

    if [[ $git_version == *"git version"* ]]; then
        echo "true"
    else
        echo_red "Git n'est pas installé"
    fi
}

function check_requirements {
    result_python=$(check_python_version)
    result_wget=$(check_wget_version)
    result_git=$(check_git_version)

    if [[ $result_git == "true" && $result_wget == "true" && $result_python == "true" ]]; then
        
        while true; do
                    echo -e "\nChoisissez quel poids voulez-vous utiliser pour Vigogne : \n1.7B \n2.13B"
            read choix

            if [[ $choix == "1" ]]; then
                poids_B="7B"
                poids_b="7b"
                break  # Sortir de la boucle while
            elif [[ $choix == "2" ]]; then
                poids_B="13B"
                poids_b="13b"
                break  # Sortir de la boucle while
            else
                echo_red "Choix invalide. Veuillez réessayer."
            fi
        done

        while true; do
            echo -e "\nVous voulez la version : \n1.chat \n2.instruct"
            read choix

            if [[ $choix == "1" ]]; then
                version_vig="chat"
                break  # Sortir de la boucle while
            elif [[ $choix == "2" ]]; then
                version_vig="instruct"
                break  # Sortir de la boucle while
            else
                echo_red "Choix invalide. Veuillez réessayer."
            fi
        done

        echo_yellow "La version choisie est : $version_vig $poids_B"
        cd ..
        echo_yellow "Clonage du dépôt GitHub de Vigogne"
        git clone https://github.com/bofenghuang/vigogne.git
        cd vigogne
        echo_yellow "Installation des dépendances"
        pip3.10 install deepspeed
        pip3.10 install .
        cd scripts
        echo_yellow "Conversion des poids au format HF"
        python3.10 convert_llama_weights_to_hf.py \
            --input_dir ../../llama.cpp/models \
            --model_size $poids_B \
            --output_dir ../../llama-$poids_B-hf

        path="$poids_B"_"$version_vig"

        echo_yellow "Lancement de la commande python : export_state_dict_checkpoint.py"
        python3.10 export_state_dict_checkpoint.py \
            --base_model_name_or_path ../../llama-$poids_B-hf \
            --lora_model_name_or_path bofenghuang/vigogne-$version_vig-$poids_b \
            --output_dir ./models/$path \
            --base_model_size $poids_B

        
        echo_yellow "Téléchargement du tokenizer"
        wget -P ./models https://huggingface.co/bofenghuang/vigogne-instruct-7b/resolve/main/tokenizer.model
        python3.10 ../../llama.cpp/convert.py models/$path
        ./../../llama.cpp/quantize models/$path/ggml-model-f16.bin models/$path/ggml-model-q4_0.bin q4_0
        ./../../llama.cpp/main -m ./models/$path/ggml-model-q4_0.bin --color -f ../prompts/$version_vig.txt -ins -c 2048 -n 256 --temp 0.1 --repeat_penalty 1.1
    else
        echo $result_python
        echo $result_wget
        echo $result_git
    fi
}

check_requirements
