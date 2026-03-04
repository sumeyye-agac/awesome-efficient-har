.PHONY: validate generate check

validate:
	python3 scripts/validate_entries.py

generate:
	python3 scripts/generate_readme.py

check:
	python3 scripts/validate_entries.py
	python3 scripts/check_generated_readme.py
