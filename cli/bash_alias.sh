### common ###
alias lla='ll -a'
alias sls='sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g" | less -R'
alias hls='history | less'


### git ###
alias gck='git checkout'
alias gst='git status'
alias gsh='git stash'
alias gsha='git stash apply'
alias gshd='git stash drop'

alias gl='git log --graph --decorate'
alias gld='git log --graph --decorate --date-order'
alias glo='git log --graph --decorate --oneline'
alias gldo='git log --graph --decorate --date-order --oneline'

alias gla='git log --graph --decorate --all'
alias glad='git log --graph --decorate --all --date-order'
alias glao='git log --graph --decorate --all --oneline'
alias glado='git log --graph --decorate --all --date-order --oneline'
