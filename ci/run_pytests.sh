#!/usr/bin/env bash
# Script run on virutalenv builder @python3
# Run at project root

cd source
pip install -r requirements.txt
pip install -r test_requirements.txt
python manage.py test lists accounts
python manage.py test functional_tests
