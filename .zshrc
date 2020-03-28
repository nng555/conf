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

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm

export PATH="/Applications/Julia-1.3.app/Contents/Resources/julia/bin:/Applications/Skim.app/Contents/SharedSupport:$PATH"

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/nathanng/Downloads/google-cloud-sdk/path.zsh.inc' ]; then source '/Users/nathanng/Downloads/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/nathanng/Downloads/google-cloud-sdk/completion.zsh.inc' ]; then source '/Users/nathanng/Downloads/google-cloud-sdk/completion.zsh.inc'; fi

setopt nosharehistory
