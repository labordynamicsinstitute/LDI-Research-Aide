# TMUX on BioHPC


Cheatsheet: https://gist.github.com/MohamedAlaa/2961058

1. login via SSH
2. launch tmux with a session name that makes sense, e.g. `tmux new -s AEAREP-xxxx`
3. Launch your matlab job
4. Disconnect from tmux: `ctrl-b d`. You don't need to press this both Keyboard shortcut at a time. First press "Ctrl+b" and then press "d" .
5. Log out of SSH

Next time:

1. login via SSH
2. reconnect to your tmux session: `tmux a -t AEAREP-xxxx`
3. If you forgot what session, `tmux ls`


When logged into the compute node, you can call `ps ux` to see all your running jobs.

