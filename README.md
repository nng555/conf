# Installation Instructions

This is a set of environment configuration files for my favorite development environment. You can pick and choose which parts you would like to install or keep. Instllation for each individual component is listed below.

## `vim`
The vim packages are the heaviest and may slow down vim loadtimes considerably. To install, run the following command.

`cp .vimrc ~ && cp -r .vim_runtime ~`

## `tmux`
the `tmux` configuration is a single file and can be installed with the following command.

`cp .tmux.conf ~`

The prefix for this configuration is `C-z`, and switching between windows has been mapped to shift arrow keys. Moving between panes within a window has been mapped to meta arrow keys, which for macs is the option key.

## iterm2 colors
