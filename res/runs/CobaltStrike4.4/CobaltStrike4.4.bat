cd /d %~dp0
start /b ../../env/jdk11/bin/javaw.exe -XX:ParallelGCThreads=4 -XX:+AggressiveHeap -XX:+UseParallelGC -javaagent:CSAgent.jar=5e98194a01c6b48fa582a6a9fcbb92d6 -Duser.language=en -jar cobaltstrike.jar
