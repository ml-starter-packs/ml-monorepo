.PHONY: format

install:
	@echo "installing with pants packages to local python env"
	./pants package ::
	pip install dist/*.whl

format:
	./pants fmt ::

pull:
	wget --random-wait -r -np -A.png https://f.mlden.com/test-data/
	mv f.mlden.com/test-data/base ./src/python/base/sample_data
	mv f.mlden.com/test-data/resize ./src/python/resize/sample_data
	mv f.mlden.com/test-data/track ./src/python/track/sample_data
	rm -rf ./f.mlden.com/
