### Swagger Code Generation

This repository relies on the following Dockerfile in order to run
Swagger Codegen inside a Docker container:
https://hub.docker.com/r/jimschubert/swagger-codegen-cli/.

We're currently using version 2.3.1 of Swagger Codegen.

### Generating the API Client

Copy the Swagger specification YAML files to the local `./input` directory.

The API v1 and v2 files can be found using the OAS export link on our
documentation pages: https://docs.jumpcloud.com/1.0 and
https://docs.jumpcloud.com/2.0.

Update the version number for each package in `config_v1.json` or
`config_v2.json`.

To generate the API v1 or v2 client, run the commands below (assuming your
API v1 and v2 specification files are `./input/index1.yaml` and
`./input/index2.yaml`):

```
docker-compose run --rm swagger-codegen generate -i /swagger-api/yaml/index1.yaml -l python -c /config/config_v1.json -o /swagger-api/out/jcapiv1
docker-compose run --rm swagger-codegen generate -i /swagger-api/yaml/index2.yaml -l python -c /config/config_v2.json -o /swagger-api/out/jcapiv2
```

This will generate the API v1 and v2 client files under the local
`./output/jcapiv1` and `./output/jcapiv2` directories.

Once you are satisfied with the generated API client, you can replace the
existing files under the `jcapiv1` or `jcapiv2` directory with your generated
files:

```
rm -rf jcapiv1
mv output/jcapiv1 .

rm -rf jcapiv2
mv output/jcapiv2 .
```
