test:
	pylint --rcfile=.pylintrc --reports=y --exit-zero amplipy | tee pylint.out
	flake8 --max-complexity=10 --statistics amplipy > flake8.out || true
	coverage run --branch --include=amplipy/\* --omit=*/test* setup.py test

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: test release
