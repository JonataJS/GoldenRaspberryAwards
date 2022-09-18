# GoldenRaspberryAwards
API RESTful para possibilitar a leitura da lista de indicados e vencedores da categoria Pior Filme do Golden Raspberry Awards baseado em um arquivo csv.

# Execute H2 
java -cp ./db/h2-2.1.214.jar org.h2.tools.Server -tcp -tcpAllowOthers -tcpPort 5234 -baseDir ./db -ifNotExists


# Set JAVA_HOME
https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html