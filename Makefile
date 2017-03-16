SWAGGER_FILE ?= 'https://console.jumpcloud.com/api/api-docs'
.PHONY: build
build:
	java -jar swagger-codegen-cli.jar generate \
		-i $(SWAGGER_FILE) \
		-l python \
		-c config.json \
		-o .
