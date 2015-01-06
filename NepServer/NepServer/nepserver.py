import ..third_party.bottle.bottle
from ..third_party.bottle.bottle import Bottle
from ..third_party.bottle.bottle import request
'''
	Provide common server interface to vim client.
GDBServer/LLDBServer will extend this interface for communicate with vim client.
An instance of NepServer controls only one debugger process(one NepDbg).
'''

bottle.Request.MEMFILE_MAX = 1000 * 1024

class NepServer:
	def __init__(self):
		# self.debugger = new NepDbg()
		self._InstallServer()
	
	def CreateBreakpoint(self, source_file, line):
		pass
	
	def _InstallServer(self):
		app = Bottle()
		self._InstallRouting(app)
		app.run(host='localhost', port=5566)

	def _InstallRouting(self, app):
		app.route('/breakpoint', 'GET', lambda *args, **kargs: self._getBreakpoint(*args, **kargs))
		app.route('/breakpoint', 'POST', lambda *args, **kargs: self._postBreakpoint(*args, **kargs))

	'''
		RESTful handler
	'''
	def _getBreakpoint(self):
		return "Hello"
	
	def _postBreakpoint(self):
		# request.json
		return "Hello"


