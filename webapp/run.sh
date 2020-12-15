#!/bin/bash

cd tests/
pytest

cd ../main/
python app.py
