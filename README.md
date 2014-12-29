Nepenthes
===============
	It's a experimental project for control gdb from vim script. For provide IDE-like capability for vim. It's design architecture inspire from https://github.com/Valloric/YouCompleteMe and https://github.com/Valloric/ycmd. Require both vim and gdb compiled with python support.

Architecture
============
	vimscript will act as a client side using popen for start/stop/restart gdb server side. gdb server will be started with "gdb <Target Program> -x GDBServer.py". And GDBServer.py will provide a RESTful interface to access from client for manipulating breakpoints and debug information. Client side will use vim tick trick "http://vim.wikia.com/wiki/Timer_to_execute_commands_periodically" to polling inform from server.


TODO
====

	* Fix PathToPythonInterpreter
