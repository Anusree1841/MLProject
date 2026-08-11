import sys
from src.logger import logging  # Optional: useful if you want to log exceptions automatically

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error information including filename, line number, and error message.
    """
    # exc_info() returns a tuple: (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Format the detailed error message string
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message


class CustomException(Exception):
    """
    Custom Exception class that captures detailed error logs.
    """
    def __init__(self, error_message, error_detail: sys):
        # Pass the basic error message to the parent Exception class
        super().__init__(error_message)
        
        # Format the detailed error message using the function above
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        # Overrides string representation to display our custom detailed message
        return self.error_message

if __name__=="__main__":
    try:
        a=1/10
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)
        
