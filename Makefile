# We need the yaml spec file to be passed to us on the cmdline.
SWAGGER_FILE_PATH ?= ${HOME}/workspace/SI/routes/webui/api
UNAME := $(shell uname)

# If you are on Windows ... really?
ifeq ($(OS), Windows_NT)
UNAME := Windows
endif

# If you are on a Mac you can avoid the whole 'java -jar' dance.
ifeq ($(UNAME), Darwin)
CODEGEN := swagger-codegen
else
CODEGEN := java -jar swagger-codegen-cli.jar
endif

# Hopefully the v1 API gets merged into v2 soon and we don't have to do this
# song and dance.
.PHONY: v1
v1: SWAGGER_FILE := $(SWAGGER_FILE_PATH)/index.yaml
v1:
	$(CODEGEN) generate \
		-i $(SWAGGER_FILE) \
		-l python \
		-c config_v1.json \
		-o jcapi_v1

.PHONY: v2
v2: SWAGGER_FILE := $(SWAGGER_FILE_PATH)/v2/index.yaml
v2:
	$(CODEGEN) generate \
		-i $(SWAGGER_FILE) \
		-l python \
		-c config_v2.json \
		-o jcapi_v2

all: v1 v2

.PHONY: clean
clean:
	rm -rf jcapi jcapi_v1 jcapi_v2
