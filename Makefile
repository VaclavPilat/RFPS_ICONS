PYTHON = python3
PIP = pip
FILE = *.py

all: run doc

install:
	$(PIP) install -r requirements.txt

doc:
	@doxygen Doxyfile

run:
	@PYTHONPATH=$(CURDIR) find scripts -type f -name $(FILE) -exec $(PYTHON) {} \;

cloc:
	@cloc icons/ --by-file

clean:
	@rm -rf docs/html/ images/