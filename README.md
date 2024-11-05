# NEON - N-Body Simulation of Near Earth Objects

## Setup
1. Clone this repository to your workspace
```bash
mkdir -p workspace
git clone TODO
cd neon
```
2. Create a python virtual environment
```bash
python -m venv .venv
```
3. Activate the virtual environment
```bash
source .venv/bin/activate
```
4. Install requirements
```bash
pip install -r requirements.txt
```
5. Run the example script
```bash
python neon.py example
```
6. A *.result* file should be generated in the *results* directory. Please investigate this file

Refer to the JPL Horizons documents on how to author the request file and the response structures.

## Horizons Documentation
For neon, we implement the file api due to its robustness. Other access methods, like a query based api, cli, telnet, and simply the public web app are available

[File API](https://ssd-api.jpl.nasa.gov/doc/horizons_file.html)

[Manual](https://ssd.jpl.nasa.gov/horizons/manual.html)

[Other Access Methods](https://ssd.jpl.nasa.gov/horizons/)

**TODO** We refer to the JPL Horizons manual to build upon the requests towards a data-provider we integrate to the simulation



