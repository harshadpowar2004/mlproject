import sys
import logging

# Configure logging (you can later move this to logging.py)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = f"""
    Error occurred in script: [{file_name}] 
    Line number: [{line_number}] 
    Error message: [{str(error)}]
    """

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

        # ✅ Log the error here (best practice)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message


