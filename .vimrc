execute pathogen#infect()

syntax on
filetype plugin indent on

set noerrorbells visualbell t_vb=
autocmd GUIEnter * set visualbell t_vb=

" Always display the status line
set laststatus=2

" Enable solarized color scheme
syntax enable
if has('gui_running')
    set background=light
    colorscheme solarized
endif

set spell
set spelllang=en_us
set spellfile=$HOME/.vim/spell/en.utf-8.add
