import sys

class HolidayPlannerException(Exception):
	"""Custom exception for Holiday Planner application."""
	def __init__(self, message: str):
		super().__init__(message)
		# Capture the last frame from the traceback
		tb = sys.exc_info()[2]
		if tb:
			frame = tb.tb_frame
			self.filename = frame.f_code.co_filename
			self.lineno = tb.tb_lineno
		else:
			# fallback to caller
			import inspect
			frame = inspect.currentframe().f_back
			self.filename = frame.f_code.co_filename
			self.lineno = frame.f_lineno
		self.message = message

	def __str__(self):
		return f"File \"{self.filename}\", line {self.lineno}: {self.message}"
