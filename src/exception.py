import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,ex_tb=error_detail.exc_info()
    file_name=ex_tb.tb_frame.f_code.co_filename
    error_message="Error in occured in python script [{0}] in the line number [{1}] and the error message is [{2}]".format(file_name,ex_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    
    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
    