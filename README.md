# TRI Hackathon 2020

This repository contains assets and code for the 2020 TRI hackathon focused on
the development of sequential learning AI for materials science.

## Installation
To set yourself up for the lessons, use the following installation procedure.  We also
recommend using Anaconda python with a fresh environment (e. g. `conda create -n hackathon` 
and `conda activate hackathon` or the like).

1. Clone the repo
    ```bash
    git clone https://github.com/TRI-AMDD/tri-hackathon-2020.git
    ```
    or if you're using ssh:

    ```bash
    git@github.com:TRI-AMDD/tri-hackathon-2020.git
    ```

2. Install requirements.  Install numpy first so dependencies requiring 
    numpy pre-install work.
    ```bash
    cd tri-hackathon-2020
    pip install numpy==1.18.3
    pip install -r requirements.txt
    ```
3. Install package (in development mode so changes in your local repo will be available).
    ```bash
    python setup.py develop
    ``` 
    
4. Start your jupyter server.  Note that you may have to install a clean version of jupyter
in your conda env in order to make sure your codes are using the correct dependencies and
pathing.

    ```angular2
    jupyter notebook
    ```

## Tutorial

The tutorial will walk through an example of using [CAMD](https://github.com/TRI-AMDD/CAMD)
for sequential learning.  Note that using CAMD is not required to participate in the hackathon, but we 
encourage you to compartmentalize your logic into similar bounded objects, i. e. 
the AI into an "Agent" and any postprocessing into something like an "Analyzer".
Also note that CAMD is an open-source code, so please feel free to issue PRs as needed.

## Hackathon rules and objectives

The objective of the hackathon is to develop an effective sequential learning
procedure for your chosen dataset that will progress in its sampling of your dataset
in an efficient manner, i. e. will choose "good" candidates for experimentation.  
Agents will be judged on the following merits:

1. Efficiency - does the SL process make "discoveries" quickly as it progresses?
2. Interpretability - can one understand what the SL is doing from a human perspective?
were the lessons learned in the process of constructing the SL process valuable from a
broader perspective?
3. Code - is the code well-constructed, modular, and able to applied elsewhere?
4. Creativity/X-factor - does the SL process contain elements that are cutting-edge, 
clever, or genuinely new ways to do ML/AI in materials science?  This one will be
highly subjective, of course.


