test:
	pylint --rcfile=.pylintrc --reports=y --exit-zero amplitude_tracker | tee pylint.out
	flake8 --max-complexity=10 --statistics amplitude_tracker > flake8.out || true
	coverage run --branch --include=amplitude_tracker/\* --omit=*/test* setup.py test

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: test release
