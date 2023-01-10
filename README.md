# This is the content create for Julio Chavez

# Run WSL

# Install python

sudo apt install -y python3-pip

# Create a virtual enviroment

    sudo apt install -y python3-venv
    python3 -m venv env
     source env/bin/activate

# install requirements

pip install -r requirements.txt

# Run sever

uvicorn main:app -reload

# Test API
