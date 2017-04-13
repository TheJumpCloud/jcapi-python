## JCAPI-Python
### Prerequisites ###
#### Java 1.8 ####
As of swagger-codegen 2.2.2, you must use JDK 1.8 or higher. On Debian/Ubuntu:
```
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt update; sudo apt-get install oracle-java8-installer
```
The easiest way to get java/swagger-codegen on MacOSX is below.  It
will also setup your `JAVA_HOME` and `PATH` for you.
```
brew cask install java
brew install swagger-codegen
```
If you had to install Java the hard way on your Mac, you should just have to add the appropriate `JAVA_HOME` to your path:
```
$ export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
$ export PATH=${JAVA_HOME}/bin:$PATH
```
Check your version:
```
$ java -version
java version "1.8.0_121"
Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
```
#### Swagger-codegen ####
A pre-built version of swagger-codegen is included in this repo.
For more information, updates, or alternate installation methods, please see the github repo: https://github.com/swagger-api/swagger-codegen

Check swagger-codegen:
```
$ java -jar swagger-codegen-cli.jar

```
OR
```
$ swagger-codegen
```
Will get your the following output:
```
Available languages: [android, aspnet5, aspnetcore, async-scala, .... ]
```

### Generating API Client ###

You can generate either the v1 or v2 APIs by specifying the
appropriate yaml file on the cmdline - assuming that you have SI
cloned somewhere.

```
$ make v2 SWAGGER_FILE=$HOME/workspace/SI/routes/webui/api/v2/index.yaml
$ make v1 SWAGGER_FILE=$HOME/workspace/SI/routes/webui/api/index.yaml
```

If you are developing the APIs, you can clean up by running `make clean`

### Installing the Python Client

Change to the appropriate version directory (jcapi_v1 or jcapi_v2) and
then run the following command.  This will install the Python Client
API locally after building.

```
$ python setup.py install
```

### Examples ###

```
import jcapi
...
api_instance = jcapi.DefaultApi()
api_instance.systemusers_get(x_api_key=<API Key>, limit=5)
```
