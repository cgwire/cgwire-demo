# Demo Script

A python script to create a demonstration production for CGWire.

All pictures come from Caminandes.com, a Blender Foundation production. All are licensed under Creative Commons.

# Purpose

This repository has two purposes:

* Allowing to make demo of the CGWire solution by starting from a non empty production.
* Giving an example of script to feed your production database when using CGWire.

# Using it

This script has two requirements. The first one is an up and runnig instance of CGWire. You can run one with Docker:

```bash
sudo docker pull cgwire/cgwire
sudo docker run -d -ti --rm -p 80:80 --name cgwire-demo cgwire/cgwire
```

The second requirement is Gazu, the Python client for the CGWire API:

```bash
pip install gazu
```

# Running the script

You can run the script by cloning this repository and run it like any Python script:

```bash
git clone git@github.com:cgwire/cgwire-demo.git
cd cgwire-demo
python demo.py
```
