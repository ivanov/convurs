map <leader>s :w! snarq.py<cr>
set makeprg=tmux\ send\ -t\ 2\ 'C-c'\ 'Up'\ 'enter'
autocmd bufwrite *.py silent make
