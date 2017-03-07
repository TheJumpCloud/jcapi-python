## JCAPI-Python
### Prerequisites ###
#### Java 1.8 ####
As of swagger-codegen 2.2.2, you must use JDK 1.8 or higher. On Debian/Ubuntu:
```
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt update; sudo apt-get install oracle-java8-installer
```
On OSX, you should just have to add the appropriate `JAVA_HOME` to your path:
```
$ export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
$ export PATH=${JAVA_HOME}/bin:$PATH
```
Then, check your version:
```
$ java -version
java version "1.8.0_121"
Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
```
#### Swagger-codegen ####
```
$ wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.2.2/swagger-codegen-cli-2.2.2.jar -O swagger-codegen-cli.jar
```
The above command will download a jar file to the current directory. This is a pre-built version of swagger-codegen. 
For more information or alternate installation methods, see the github repo: https://github.com/swagger-api/swagger-codegen

To see if it was successfully downloaded:
```
$ java -jar swagger-codegen-cli.jar
Available languages: [android, aspnet5, aspnetcore, async-scala, bash, cwiki, csharp, cpprest, dart, elixir, flash, python-flask, go, groovy, java, jaxrs, jaxrs-cxf-client, jaxrs-cxf, jaxrs-resteasy, jaxrs-resteasy-eap, jaxrs-spec, jaxrs-cxf-cdi, inflector, javascript, javascript-closure-angular, jmeter, nancyfx, nodejs-server, objc, perl, php, python, qt5cpp, ruby, scala, scalatra, finch, silex-PHP, sinatra, rails5, slim, spring, dynamic-html, html, html2, swagger, swagger-yaml, swift, swift3, tizen, typescript-angular2, typescript-angular, typescript-node, typescript-fetch, akka-scala, CsharpDotNet2, clojure, haskell, lumen, go-server, erlang-server, undertow, msf4j, ze-ph]
```

### Generating API Client ###
```
$ make build
$ python setup.py install
```
