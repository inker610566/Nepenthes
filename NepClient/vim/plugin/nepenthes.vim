command! GDB call s:StartServer()

function! s:StartServer()
	py import os
	py import sys
	py print os.path.abspath(".")
	py print sys.path.insert(0, os.path.abspath("."))
	py from Nepenthes.GDBServer import GDBServer
	py nepServer = GDBServer()
endfun
