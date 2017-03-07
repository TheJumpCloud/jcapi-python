SWAG_FILE ?= 'https://console.jumpcloud.com/api/api-docs'
TARGET_LANG ?= 'python'
.PHONY: build
build:
	swagger-codegen generate \
		-i $(SWAG_FILE) \
		-l $(TARGET_LANG) \
		-c config.json \
		-o .
