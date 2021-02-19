include .env

YEAR=2019
DAYS=$(shell seq -w 1 25)

TMPL=template.py

$(DAYS):
	@test -d $@ && [ "$(shell ls -A $@ 2>/dev/null)" ] \
		&& echo "the directory is not empty" && exit 1 \
		|| true
	mkdir -p $@
	curl -f -b "session=$(SESSION)" -o "$@/data.in" \
		"https://adventofcode.com/$(YEAR)/day/$(@:0%=%)/input"
	cp $(TMPL) $@/solve.py

test:
	@echo $(DAYS)

.PHONY: $(DAYS)

