SWAG_FILE ?= 'https://console.jumpcloud.com/api/api-docs'
LANG ?= 'python'
.PHONY: build
build:
	swagger-codegen generate \
		-i $(SWAG_FILE) \
		-l $(LANG) \
		-c config.json \
		-o .
