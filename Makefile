SWAGGER_FILE ?= 'https://console.jumpcloud.com/api/api-docs'
.PHONY: build
build:
	swagger-codegen generate \
		-i $(SWAG_FILE) \
		-l python \
		-c config.json \
		-o .
