from log import write_log
from pg_connection import *

file_name = 'Main'

logger = write_log(file_name)
logger.info('Inicio do Script.')
logger.info('Start of Script.')


cur = connectDB()
    
close_conection(cur)
    
logger.info('Fim do Script.')
logger.info('End of script.')