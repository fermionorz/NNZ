cd /d %~dp0
start /B "BurpSuite" "javaw.exe" "-Xmx8G" "-Dfile.encoding=utf-8" "-noverify" "-javaagent:BurpSuiteLoader.jar" "-jar" "BurpSuite.jar" 