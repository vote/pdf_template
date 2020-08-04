lint:
	autoflake \
		--remove-unused-variables \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		--in-place \
		--recursive \
		*.py && \
		isort --recursive *.py && \
		black *.py


test:
	docker build . -t pdf-template-dev
	docker run --rm -it -v ${PWD}:/app pdf-template-dev

test_inner:
	mypy *.py
	python -m pytest .
