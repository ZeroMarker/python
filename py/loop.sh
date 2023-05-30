#!/bin/bash
for a in {1..10}
do
	clear
	python time.py | figlet | cowsay -f tux -n | lolcat
	sleep 1s
done

# bash %

