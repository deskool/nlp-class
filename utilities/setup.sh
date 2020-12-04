#!/bin/bash

echo "INSTALLING VIRTUALENV PACKAGE"
pip3 install virtualenv

echo "CREATING SUBMISSION DIRECTORIES..."
mkdir Homework
for i in {0..15}
do
   mkdir Homework/HW$i
   touch Homework/HW$i/requirements.txt 
   mkdir Homework/HW$i/materials
   
done

mkdir Project
for i in {1..4}
do
  mkdir Project/Part$i
  mkdir Project/Part$i/materials
done

mkdir FinalReport


