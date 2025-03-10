# shell

## vim

:!python %
!   external command
%   stand for current file

:%!xxd
text to hex

:!bash %

## Envirment Variable

export PATH=$PATH:~

## Job Switch

./.zshrc
ctrl+z  suspend
fg      foreground
bg      background
kill -9 PID
ps -elf all process
ps -lf  shell about process

### Background Run

nohup python test.py &
nohup python -u sleep.py>test.log 2>&1 &
// stdin & stderr > test.log

**stdio**

- 0 stdin
- 1 stdout
- 2 stderr

## Process

ppid parent process id
cat /proc/pid/maps
ps -o pid,ppid,sz,vsz,rss,cmd
jobs  // view background jobs
// + next job
// - recent nohup job
fg %1 // #1 job
bg %1 // #1 job
pstree -h
