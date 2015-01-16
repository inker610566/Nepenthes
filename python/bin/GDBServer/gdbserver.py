import sys
sys.path.insert("../..")

from lib.nepserver.nepserver import NepServer

class GDBServer(NepServer):
	def __init__(self):
		super(GDBServer, self).__init__()
	
	def _getBreakpoint(self, bp_no):
		# ....




