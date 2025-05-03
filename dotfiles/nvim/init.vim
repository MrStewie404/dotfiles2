call plug#begin()

Plug 'preservim/nerdtree'
Plug 'morhetz/gruvbox'
Plug 'joshdick/onedark.vim'

call plug#end()

nnoremap <C-b> :NERDTreeToggle<CR>

" colo gruvbox
colo onedark

syntax on
set number

highlight Normal guibg=NONE ctermbg=NONE

" Установить количество пробелов вместо табов
set expandtab

" Количество пробелов, которые вставляются при нажатии Tab
set tabstop=4     " Ширина символа табуляции (по умолчанию 8)

" Количество пробелов для автоотступов (>>, <<, autoindent и т. д.)
set shiftwidth=4  " Размер отступа

" Количество пробелов, вставляемых при нажатии Tab в режиме вставки
set softtabstop=4 " Если =0, используется tabstop
