from ycmd import utils
class GDBServer:
	def __init__(self):
		self._SetupServer()
	
	def _SetupServer(self):
		args = [ "/usr/bin/python",
				 _PathToServerScript()]
		self._server_open = utils.SafePopen(args)

def _PathToServerScript():
	return "./gdbServer.py"
