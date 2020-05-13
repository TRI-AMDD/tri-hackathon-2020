echo "installing camd"
sudo -u ec2-user -i <<'EOF'
unset SUDO_UID
source activate /home/ec2-user/SageMaker/custom-miniconda/envs/AMDD
cd /home/ec2-user/SageMaker/tri-hackathon-2020
pip install -r requirements.txt
pip install -e .
EOF