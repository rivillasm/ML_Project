
import sys
import os

class HousingException(Exception):    # getting exceptio from the father class

    def __init__(self, error_message:Exception, error_detail:sys):   # gets error message and details
        super().__init__(error_message)                                     # passes the mesage to the exception class
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error message: Exception object
        error detail : object of sys module
        """
        _,_,exec_tb = error_detail.exc_info()     # exc_info() requires parameters: type,value,traceback
                                                  # we are only interested in the traceback parameter
        line_number = exec_tb.tb_frame.f_lineno            # gets the line number
        file_name = exec_tb.tb_frame.f_code.co_filename    # gets the file name
        error_message = f"Error occured in script:[{file_name} at line number [{line_number}] error message [{error_message}]]"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self)-> str:
        return HousingException.__name__.str()