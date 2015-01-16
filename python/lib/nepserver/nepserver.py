import os
import signal
from ..third_party.bottle import bottle
from ..third_party.bottle.bottle import Bottle
from ..third_party.bottle.bottle import request
'''
	Provide common server interface to vim client.
GDBServer/LLDBServer will extend this interface for communicate with vim client.
An instance of NepServer controls only one debugger process(one NepDbg).
'''

bottle.Request.MEMFILE_MAX = 1000 * 1024

class NepServer(object):
	def __init__(self):
		# self.debugger = new NepDbg()
		self._InstallServer()
	
	def CreateBreakpoint(self, source_file, line):
		'''
			post to /breakpoint
		'''
		pass
	
	def Shutdown(self):
		'''
			close server process
		'''
		pass
	
	def _InstallServer(self):
		app = Bottle()
		self._InstallRouting(app)
		app.run(host='140.115.53.50', port=5566)
	
	def _InstallRouting(self, app):
		app.route('/breakpoint', 'GET', lambda *args, **kargs: self._getBreakpoint(*args, **kargs))
		app.route('/breakpoint', 'POST', lambda *args, **kargs: self._postBreakpoint(*args, **kargs))
		app.route('/kill', 'GET', lambda *args, **kargs: self._shutdownServer(*args, **kargs))

	'''
		RESTful handler
	'''
	def _getBreakpoint(self):
		return "Hello"
	
	def _postBreakpoint(self):
		# request.json
		return "Hello"
	
	def _shutdownServer(self):
		return "ready to shutdown"
	


