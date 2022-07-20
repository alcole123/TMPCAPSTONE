#!/bin/bash
read -p "Please input a stackname: " stackname
read -p "Please submit dir of formation file" filename
aws cloudformation create-stack --stack-name ${stackname}  --template-body file://${filename}
