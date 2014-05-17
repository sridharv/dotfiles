" Enable pathogen
source ~/.vim/custom/pathogen.vim

" Source a few sensible defaults outside of vim-sensible. 
source ~/.vim/custom/defaults.vim

" Load local machine overrides.
if !empty(glob("~/.vim/custom/local.vim"))
	source ~/.vim/custom/local.vim
endif

" Per module customization
source ~/.vim/custom/vim-airline.vim
source ~/.vim/custom/vim-solarized.vim
source ~/.vim/custom/supertab.vim
source ~/.vim/custom/overrides.vim

