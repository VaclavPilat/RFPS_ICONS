PYTHON = python3
PIP = pip

all: run doc

install:
	$(PIP) install -r requirements.txt

doc:
	doxygen Doxyfile

run:
	$(PYTHON) src/main.py

cloc:
	cloc . --include-lang=Python --by-file

clean:
	rm -rf docs/html/ images/