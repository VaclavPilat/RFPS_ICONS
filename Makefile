FILE = *.py

all: run doc

install:
	@pip install -r requirements.txt

doc:
	@doxygen Doxyfile

run:
	@PYTHONPATH=$(CURDIR) find scripts -type f -name $(FILE) -exec python3 {} \;

cloc:
	@cloc src/ --by-file

clean:
	@rm -rf docs/html/ images/
	@find . -type d -name "__pycache__" -exec rm -rf {} +