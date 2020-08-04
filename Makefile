lint:
	autoflake \
		--remove-unused-variables \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		--in-place \
		--recursive \
		*.py pdf_template/ && \
		isort --recursive *.py pdf_template/  && \
		black *.py pdf_template/


test:
	docker build . -t pdf-template-dev
	docker run --rm -it -v ${PWD}:/app pdf-template-dev

test_inner:
	mypy pdf_template
	python -m pytest .
