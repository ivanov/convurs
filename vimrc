map <leader>s :w! convurs.py<cr>
set makeprg=tmux\ send\ -t\ 2\ 'C-c'\ 'Up'\ 'enter'
autocmd bufwrite *.py silent make
