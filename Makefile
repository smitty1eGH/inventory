.phony: help test clean
help:
	@echo ""
	@echo "Handy project commands:"
	@echo ""
	@echo "target  | description"
	@echo "--------+------------"
	@echo "test      Run test.py unit tests"
	@echo "clean     Empty __pycache__/"
	@echo ""
test:
	@../bin/activate && python -m pytest --capture=no tests
clean:
	@rm -vf tests/__pycache__/*
