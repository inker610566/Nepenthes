'''
	This class is a debugger interface for NepServer to manipulate underlying debugger.
And its design is referred from GDB pythonAPI: https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html#Python-API
'''

class NepDbg:
	'''
		@return created breakpoint no
	'''
	def setBreakPoint(self, source_file, line_no):
		raise NotImplementedError("NepDbg::setBreakPoint NotImplementedError")
	
	'''
		@return result breakpoint no
	'''
	def getBreakPointNo(self, source_file, line_no):
		raise NotImplementedError("NepDbg::getBreakPointNo NotImplementedError")
	
	'''
		@return (source_file, line_no, ...)
	'''
	def getBreakPointInfo(self, bp_no):
		raise NotImplementedError("NepDbg::getBreakPointInfo NotImplementedError")

	def removeBreakPoint(self, bp_no):
		raise NotImplementedError("NepDbg::removeBreakPoint NotImplementedError")

