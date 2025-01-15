PYTHON = python3
PIP = pip

all: run doc

install:
	$(PIP) install -r requirements.txt

doc:
	doxygen Doxyfile

run:
	$(PYTHON) main.py

cloc:
	cloc . --include-lang=Python

clean:
	rm -rf html/ images/