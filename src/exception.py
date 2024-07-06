import sys
import logging 

def errorMessage(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    lineNumber=exc_tb.tb_lineno
    error_message = "There is an error in the file [{0}] at line [{1}] and the error message is [{2}]".format(
        filename, lineNumber, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,errorDetail:sys):
        super().__init__(error_message)
        self.error_message=errorMessage(error_message,error_detail=errorDetail)
    
    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide By Zero Error")
        raise CustomException(e,sys)


        

