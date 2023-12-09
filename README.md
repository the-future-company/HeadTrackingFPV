# Head Tracking FPV Raspberry Pi Repo
This repo is installed on the Raspberry Pi. Responsible for
1. Establishing Wi-Fi Direct with a mobile phone.

# Development Setup
This project uses `pipenv` for managing package dependencies and Python environments. Here's how you can set up your 
development environment to start contributing to the project.

## Prerequisites
Before you begin, ensure you have the following installed:
- [Python 3.9](https://www.python.org/downloads/)
- [pip3](https://pip.pypa.io/en/stable/installation/)

### You can follow this to install Python 3.9 in your Raspberry Pi

#### 1. Update and Install Dependencies:
First, update your package list and install necessary dependencies for building Python.
```bash
sudo apt update
sudo apt install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```

#### 2. Download Python 3.9 Source:
Go to the /tmp directory and download the Python 3.9 source code.
```bash
cd /tmp
wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tar.xz
```

#### 3. Extract and Compile:
Extract the tarball and compile Python. Replace 3.9.x with the exact version number in both commands.
```bash
tar xf Python-3.9.13.tar.xz
cd Python-3.9.13
./configure --prefix=$HOME/.local
make -j 4
make altinstall
```

#### 4. Verify Installation:
Check if Python 3.9 is installed:
```bash
~/.local/bin/python3.9 --version
```

## Installing Pipenv
`pipenv` is a packaging tool for Python that simplifies dependency management. If you don't have `pipenv` installed, 
you can install it using `pip`:
```bash
python3 -m pip install --user pipenv
```

Once pipenv is installed create a virtual environment point to Python 3.9:
```bash
pipenv --python ~/.local/bin/python3.9
```

## Setting Up the Development Environment
Once you have `pipenv` installed, follow these steps to set up your development environment:

1. Clone the repository:
2. Install dependencies using the following command: `python3 -m pipenv install --dev`. This command will install all 
the dependencies required for the project, including the ones needed for development.

## Adding New Dependencies
1. To add a new package: `python3 -m pipenv install packagename`. And for development dependencies: `python3 -m pipenv 
install packagename --dev`. These commands will update the `Pipfile` and `Pipfile.lock` accordingly.
2. Don't forget to update the `requirements.txt` by running `python3 -m pipenv requirements > requirements.txt` 

Happy coding!
