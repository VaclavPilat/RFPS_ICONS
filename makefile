PYTHON = python3
PIP = pip
FILE = src/*.py

all: run doc

install:
	$(PIP) install -r requirements.txt

doc:
	@doxygen Doxyfile

run:
	@for file in $(FILE); do \
		$(PYTHON) "$$file"; \
	done

cloc:
	@cloc . --include-lang=Python --by-file

clean:
	@rm -rf docs/html/ images/