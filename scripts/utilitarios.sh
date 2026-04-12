#!/bin/bash

set -e

JAR_DIR=./jars

echo "Criando diretório de jars..."
mkdir -p $JAR_DIR

echo "Baixando driver mysql..."
wget -O $JAR_DIR/mysql-connector-j-8.0.33.jar \
https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.0.33/mysql-connector-j-8.0.33.jar

echo "Baixando hadoop-aws..."
wget -O $JAR_DIR/hadoop-aws-3.3.4.jar \
https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar

echo "Baixando aws-java-sdk-bundle..."
wget -O $JAR_DIR/aws-java-sdk-bundle-1.12.262.jar \
https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

echo "Download concluído."

echo "Arquivos baixados:"
ls -lh $JAR_DIR