cd /d %~dp0
start /b ../../env/jdk11/bin/javaw.exe -javaagent:patch.jar -jar dogcs.jar