#!/bin/bash
#generates sample input and output

rm samples/explanations.txt
for i in {0..2}
do
#   echo $i | python3 ./mkin.py > samples/input/input$i.txt
  python3 solutions/run_sequence.py < samples_for_sequence/input/input$i.txt >> samples/explanations.txt
done
