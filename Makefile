test:
	pylint --rcfile=.pylintrc --reports=y --exit-zero amplitude | tee pylint.out
	flake8 --max-complexity=10 --statistics amplitude > flake8.out || true
	coverage run --branch --include=amplitude/\* --omit=*/test* setup.py test

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: test release
