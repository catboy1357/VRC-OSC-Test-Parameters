@echo off
echo "Installing requirements (be sure to have python installed and in PATH)"
pip install -r Requirements.txt
python Test_VRC_OSC.py
pause