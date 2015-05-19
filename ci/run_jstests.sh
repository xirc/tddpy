#!/usr/bin/env bash
# Script run on 'execute Shell'
# Run at project root

cd source
phantomjs superlists/static/tests/runner.js accounts/static/tests/tests.html
phantomjs superlists/static/tests/runner.js lists/static/tests/tests.html
