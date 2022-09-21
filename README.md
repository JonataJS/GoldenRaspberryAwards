# Description

RESTful API to read the list of Golden Raspberry Awards Worst Film nominees and winners based on a csv file.

---
# Requirements


## System requirements
- [Python 3](https://www.python.org/downloads/)
- [Java SE](https://www.oracle.com/java/technologies/downloads/)
- [H2 database](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)

## Project dependencies
Use pip to install project dependencies from requirements.tx file

Ex: `pip install -r config/requirements.txt`

---
# Run Project


## Execute Database 
`java -cp ./db/h2-2.1.214.jar org.h2.tools.Server -tcp -tcpAllowOthers -tcpPort 5234 -baseDir ./db -ifNotExists`


## Execute project 
`flask run`