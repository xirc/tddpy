TARGETS_SETUP = setup-env setup-run-env setup-test-env
TARGETS_TEST = test unit-test functional-test unit-test-js
TARGETS_DEPLOY = deploy deploy-staging
.PHONY= default ${TARGETS_SETUP} ${TARGETS_TEST} ${TARGETS_DEPLOY}

default:
	exit

# setup
setup-env: setup-run-env setup-test-env
setup-run-env:
	pip install -r requirements.txt
setup-test-env: setup-run-env
	pip install -r test_requirements.txt

# test
test: unit-test functional-test unit-test-js
unit-test: setup-env
	cd source && python manage.py test lists accounts
functional-test: setup-env
	cd source && python manage.py test functional_tests
unit-test-js:
	cd source && phantomjs superlists/static/tests/runner.js accounts/static/tests/tests.html
	cd source && phantomjs superlists/static/tests/runner.js lists/static/tests/tests.html
