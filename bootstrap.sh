#!/bin/bash
for i in 2015 2016 2017
do
  cd '/path/to/advent-of-code/'$i
  for j in {1..25}
  do
    mkdir $j
    cd '/path/to/advent-of-code/'$i'/'$j
    touch README.md
    echo "Insert Question Here" >> README.md
  done
done
