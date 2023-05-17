# Vigogne_auto_installer

This repository aims to simplify the installation of the Vigogne AI, provided that you have the prerequisites listed below.

![macOS](https://img.shields.io/badge/-macOS-%23999999?style=flat-square&logo=macos&logoColor=white) 
![Linux](https://img.shields.io/badge/-Linux-%23FCC624?style=flat-square&logo=linux&logoColor=white)
![Windows](https://img.shields.io/badge/-Windows-%230078D6?style=flat-square&logo=windows&logoColor=white)

### Table of contents

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#how-does-it-work-">Introduction</a>
    </li>
    <li>
      <a href="#get-started-">Get started 🚀</a>
      <ul>
        <li><a href="#mac">Mac</a></li>
        <li><a href="#windows">Windows</a></li>
        <li><a href="#linux">Linux</a></li>
      </ul>
    </li>
    <li><a href="#follow-me-">Follow ME ✅</a></li>
    <li><a href="#support">Support</a></li>
    <li><a href="#about-the-repo-">About the repo ⚙️</a></li>
  </ol>
</details>

### Introduction

Using the script corresponding to your operating system, if the prerequisites are met, you just have to run the script. You will answer two questions concerning the weight you wish to use and the version. I invite you to read more by clicking [here](https://github.com/bofenghuang/vigogne/blob/main/vigogne/model/README.md).

## Before you begin !

First of all, you must have Python 3.10 or 3.9 installed. You can check your version by using the following command:

```bash
python3 --version
```

Secondly, you must have GIT installed. You can check your version using the following command:

```bash
git --version
```

Third, you must have WGET installed. You can check your version using the following command:

```bash
wget --version
```

Once you have checked these requirements, make sure you also :

- Have the [llama.cpp](https://github.com/ggerganov/llama.cpp) repository and have compiled it (as we will need ./chat).
- Place the weights you wish to use for Vigogne in the "models" folder of llama.cpp.

```bash
#Here is an example of what the folder containing llama.cpp should look like (showing only the most important files)

llama.cpp
├── convert.py
├── main
├── models
│   ├── 7B
│   │   ├── checklist.chk
│   │   ├── consolidated.00.pth
│   │   └── params.json
│   ├── ggml-vocab.bin
│   ├── tokenizer.model
│   └── tokenizer_checklist.chk
├── quantize

```

Once everything is ready, we can continue.


## Mac

After cloning the repository, you have two options:

### 1. With Python

If you have [Python](https://www.python.org/downloads/release/python-31011/), you can run the python file with this command : 

```bash
#In 🏴󠁧󠁢󠁥󠁮󠁧󠁿
python comparator_sha256.py

#In 🇫🇷
python comparator_sha256_fr.py
```

### 2. With Bash

Or, run this command (once in the folder) to make the bash files executable :

```bash
chmod +x comparator_sha256_mac.sh
chmod +x comparator_sha256_mac_fr.sh
```

And just run : 

```bash
#In 🏴󠁧󠁢󠁥󠁮󠁧󠁿
./comparator_sha256_mac.sh

#In 🇫🇷
./comparator_sha256_mac_fr.sh
```

And let us guide you by answering the questions asked !

## Windows

Once you have python, you just need to run this command :  

```bash
#In 🏴󠁧󠁢󠁥󠁮󠁧󠁿
python comparator_sha256.py

#In 🇫🇷
python comparator_sha256_fr.py
```

And let us guide you by answering the questions asked !

## Linux

After cloning the repository, you have two options:

### 1. With Python

If you have [Python](https://doc.ubuntu-fr.org/python#installation), you can run the python file with this command : 

```bash
#In 🏴󠁧󠁢󠁥󠁮󠁧󠁿
python comparator_sha256.py

#In 🇫🇷
python comparator_sha256_fr.py
```

### 2. With Bash

Or, run this command (once in the folder) to make the bash files executable :

```bash
chmod +x comparator_sha256_linx.sh
chmod +x comparator_sha256_linx_fr.sh
```

And just run : 

```
#In 🏴󠁧󠁢󠁥󠁮󠁧󠁿
./comparator_sha256_linx.sh

#in 🇫🇷
./comparator_sha256_linx_fr.sh
```

And let us guide you by answering the questions asked ! 


## Follow ME ✅

[![youtube](https://img.shields.io/youtube/channel/subscribers/UC5XJLz-Gnv8_T61wMXu-K-A?label=PereConteur&style=social)](https://www.youtube.com/channel/UC5XJLz-Gnv8_T61wMXu-K-A)

[![Rejoignez notre serveur Discord!](https://img.shields.io/badge/Discord-Join%20our%20server-blue?style=for-the-badge&logo=discord)](https://discord.gg/xY63gyVfaR)


[![twitch](https://img.shields.io/twitch/status/pereconteur?label=PereConteur&style=social)](https://www.twitch.tv/pereconteur)

### Resources



### Support

For support, join the [Discord channel](https://discord.gg/xY63gyVfaR)

### About the repo ⚙️

 - ![](https://img.shields.io/github/repo-size/pereconteur/Vigogne_auto_installer)
 - ![](https://img.shields.io/github/last-commit/pereconteur/Vigogne_auto_installer)
