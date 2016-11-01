.PHONY: build
build:
	java -jar swagger-codegen-cli.jar generate \
		-i index.yaml \
		-l python \
		-c config.json \
		-o .
