'''
	Provide common server interface to vim client.
GDBServer/LLDBServer will extend this interface for communicate with vim client.
An instance of NepServer controls only one debugger process(one NepDbg).
'''

class NepServer:
	def __init__(self, source_file):
		# self.debugger = new NepDbg()
		self._InstallServer()
	
	def CreateBreakpoint(self, ):
		pass
	
	def _InstallServer(self):
		self._InstallRESTful()

	def _InstallRESTful(self):
		pass

	def _InstallHandler(self):
		import 
	
