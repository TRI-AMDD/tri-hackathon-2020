echo "installing camd"
sudo -u ec2-user -i <<'EOF'
unset SUDO_UID
source activate AMDD
cd
pip install tensorflow==1.15.2
pip install -r requirements.txt
pip install -e .

# Install ipywidgets and widgets extensions
pip install ipywidgets
source activate JupyterSystemEnv  # not sure if this is necessary
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter nbextension enable --py widgetsnbextension
EOF

restart jupyter-server