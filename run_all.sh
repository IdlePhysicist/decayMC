#!/bin/bash

echo This script will execute the Decay simulation
echo
echo RUNNING DECAYMC
python decayMC.py
echo RUNNING FIT
python fit.py

echo END SCRIPT 
