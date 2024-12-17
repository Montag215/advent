#!/bin/bash
#grep -oE 'do\(\).*?don'"'"'t\(\)' input.txt | \
grep -oE 'mul\([0-9]+,[0-9]+\)' out.txt | \
sed -E 's/mul\(([0-9]+),([0-9]+)\)/\1 \2/' | \
awk '{sum += $1 * $2} END {print sum}'
