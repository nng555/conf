#
# Executes commands at the start of an interactive session.
#
# Authors:
#   Sorin Ionescu <sorin.ionescu@gmail.com>
#

# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi


# Customize to your needs...

# export paths
#export PATH=/pkgs/cuda-9.2/bin:/pkgs/nccl_2.3.5-2+cuda9.2_x86_64/lib:/h/nng/programs/julia-1.3.1:/h/nng/programs/julia-1.3.1/bin:/scratch/ssd001/home/nng/.local/lib/python3.6/site-packages:/h/nng/programs/bin:$PATH
export EDITOR=vim
export VISUAL=vim
export KEYTIMEOUT=1
#export LD_LIBRARY_PATH=/pkgs/nccl_2.3.5-2+cuda9.2_x86_64/lib:$LD_LIBRARY_PATH

#export NVM_DIR="$HOME/.nvm"
#[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm

#export PATH="/Applications/Julia-1.3.app/Contents/Resources/julia/bin:/Applications/Skim.app/Contents/SharedSupport:$PATH"

# The next line updates PATH for the Google Cloud SDK.
#if [ -f '/Users/nathanng/Downloads/google-cloud-sdk/path.zsh.inc' ]; then source '/Users/nathanng/Downloads/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
#if [ -f '/Users/nathanng/Downloads/google-cloud-sdk/completion.zsh.inc' ]; then source '/Users/nathanng/Downloads/google-cloud-sdk/completion.zsh.inc'; fi

setopt nosharehistory

# don't put duplicate lines or lines starting with space in the history.
setopt HIST_IGNORE_ALL_DUPS

# append to the history file, don't overwrite it
setopt APPEND_HISTORY

# some more ls commands
alias ll='ls -alF'
alias la='ls -A'
alias lh='ls -lah'
alias l='ls -CF'

# slurm commands
alias sqw='squeue -u nng --sort=+i --format=\"%.8F %.6P %.70j %.2t %.10M %.6D %.8N %.6b %.15E\"'
alias squ='squeue -u nng --format="%.8F %.6P %.100j %.2t %.10M %.6D %.8N %.6b %.13q" --sort=+i'
alias sql='squeue -u nng --format="%.8F %.6P %.100j %.2t %.10M %.6D %.8N %.6b %.13q" --sort=+i | less'
alias sq='squeue --format="%.8F %.6P %.10u %.50j %.2t %.10M %.6D %.8N %.6b %.15E"'
alias sqr='squ | grep " R " | wc -l'
alias sqp='squ | grep " PD " | wc -l'
scseq () { for i in $(seq $1 $2); do scancel $i; done }

vview () { for d in launch*$1*$2*$3*; do for f in `ls -d $d/log/*.out | sort -rV`; do line=`grep "| valid" $f | tail -n 1`; if [[ "$line" == *"| accuracy"* ]]; then echo $f; echo $line; break; fi; done; done}
lview () { for d in launch*$1*$2*$3*; do for f in `ls -d $d/log/*.out | sort -rV`; do line=`grep valid $f | tail -n 1`; if [[ "$line" == *"| loss"* ]]; then echo $f; echo $line; break; fi; done; done}
bview () { for d in launch*$1*$2*$3*; do for f in `ls -d $d/log/*.out | sort -rV`; do line=`grep "| bleu" $f | tail -n 1`; if [[ "$line" == *"| bleu"* ]]; then echo $f; echo $line; break; fi; done; done}

cpbest () { for d in launch*$1*$2*; do if [ ! -e $d/checkpoint_best.pt ]; then for f in `ls -d $d/* | sort -rV`; do if [ -e $f/checkpoint_best.pt ]; then cp $f/checkpoint_best.pt $d/checkpoint_best.pt; echo $f; break; fi; done; fi; done }
cplast () { for d in launch*$1*$2*; do for f in `ls -d $d/* | sort -rV`; do if [ -e $f/checkpoint_last.pt ]; then cp $f/checkpoint_last.pt $d/checkpoint_last.pt; echo $f; break; fi; done; done }

venv () {
. /scratch/ssd001/home/nng/venv/$1/bin/activate    # commented out by conda initialize
}

# vector directory aliases
hdd=/scratch/hdd001/home/nng

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

alias leaderboard='sshare -a | head -n 2 && sshare -a | sort -rnk5 | head -n 20'

alias cleandir='rm -rf bin; rm train.raw.input0; rm train.raw.label; rm train.soft.label; rm train.label; rm train.input0'

alias watch-5='watch -n 5 '
unalias rm

setopt nomenucomplete
setopt GLOB_ASSIGN

bindkey -v
bindkey '^R' history-incremental-search-backward
#autoload -U edit-command-line
#zle -N edit-command-line
#bindkey '\033' edit-command-line
