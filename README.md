# Vigogne_auto_installer

This repository aims to simplify the installation of the [Vigogne AI](https://github.com/bofenghuang/vigogne), provided that you have the prerequisites listed below.

![macOS](https://img.shields.io/badge/-macOS-%23999999?style=flat-square&logo=macos&logoColor=white) 
![Linux](https://img.shields.io/badge/-Linux-%23FCC624?style=flat-square&logo=linux&logoColor=white)
![Windows](https://img.shields.io/badge/-Windows-%230078D6?style=flat-square&logo=windows&logoColor=white)

### Table of contents

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#before-you-begin-">Before you begin</a>
      <ul>
        <li><a href="#mac-&-linux">Mac & Linux</a></li>
        <li><a href="#windows">Windows</a></li>
      </ul>
    </li>
    <li><a href="#follow-me-">Follow ME ✅</a></li>
    <li><a href="#resources">Resources</a></li>
    <li><a href="#support">Support</a></li>
    <li><a href="#about-the-repo-">About the repo ⚙️</a></li>
  </ol>
</details>

### Introduction

Using the script corresponding to your operating system, if the prerequisites are met, you just have to run the script. You will answer two questions concerning the weight you wish to use and the version. 
I invite you to read more by clicking [here](https://github.com/bofenghuang/vigogne/blob/main/docs/model.md).

## Before you begin !

First of all, you must have **Python [3.10](https://www.python.org/downloads/release/python-3100/) or [3.9](https://www.python.org/downloads/release/python-390/) installed**. You can check your version by using the following command:

```bash
python3 --version
```

Secondly, you must have **[GIT](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git) installed**. You can check your version using the following command:

```bash
git --version
```

Third, you must have **WGET installed**. You can check your version using the following command:

```bash
wget --version
```

Once you have checked these requirements, make sure you also :

- Have the [llama.cpp](https://github.com/ggerganov/llama.cpp) repository and have compiled it (as we will need ./main, ./quantize and convert.py).

**Apparently this time you don't need to download the LLama weights beforehand, so it's even easier!**

```bash 
# (showing only the most important files)

llama.cpp
├── convert.py
├── main
├── quantize
```

Once everything is ready, we can continue.


## Mac & Linux

After cloning the repository, you must place it in the same folder as llama.cpp, as shown in the example below :

```bash
Desktop
├── Vigogne_auto_installer
└── llama.cpp
```

Once this is done, go to the repository :

```bash
cd path/to/Vigogne_auto_installer
```

Make the file executable :

```bash
chmod +x vigogne_auto_install_Mac.sh
```

Then run the command :

```bash
./vigogne_auto_install_Mac.sh
```

## Windows

After cloning the repository, you must place it in the same folder as llama.cpp, as shown in the example below :

```bash
Desktop
├── Vigogne_auto_installer
└── llama.cpp
```

Once this is done, go to the repository :

```bash
cd path/to/Vigogne_auto_installer
```

Then run the command :

```bash
python3.10 vigogne_auto_install_Windows.py
```

## Linux


## Follow ME ✅

[![youtube](https://img.shields.io/youtube/channel/subscribers/UC5XJLz-Gnv8_T61wMXu-K-A?label=PereConteur&style=social)](https://www.youtube.com/channel/UC5XJLz-Gnv8_T61wMXu-K-A)

[![Rejoignez notre serveur Discord!](https://img.shields.io/badge/Discord-Join%20our%20server-blue?style=for-the-badge&logo=discord)](https://discord.gg/xY63gyVfaR)

[![twitch](https://img.shields.io/twitch/status/pereconteur?label=PereConteur&style=social)](https://www.twitch.tv/pereconteur)

### Resources

- [Bofenghuang](https://github.com/bofenghuang) (creator of Vigogne IA)
- [Vigogne](https://github.com/bofenghuang/vigogne)
- [Vigogne models](https://github.com/bofenghuang/vigogne/blob/main/vigogne/model/README.md)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)

### Support

For support, join the [Discord channel](https://discord.gg/xY63gyVfaR)

### About the repo ⚙️

 - ![](https://img.shields.io/github/repo-size/pereconteur/Vigogne_auto_installer)
 - ![](https://img.shields.io/github/last-commit/pereconteur/Vigogne_auto_installer)
