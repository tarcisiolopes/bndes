import psycopg2 as pg
from psycopg2 import OperationalError
import sys

from log import write_log
from db_data import user_db, password_db

logger = write_log('PG_Connection')
logger.info("Inicio do Script")

# conexão com o banco de dados
# database connection
conn = pg.connect(
    host = 'localhost',
    database = 'bndes',
    user = user_db,
    password = password_db
)

# função para pegar erros de banco de dados
# function to catch database errors
def print_psycopg2_exception(err, file_name):
    err_type, err_obj, traceback = sys.exc_info()
    line_num = traceback.tb_lineno
    logger.error("Psycopg2 ERROR: " + str(err) +
                  " at file: " + str(file_name) +
                  " at line n: " + str(line_num) +
                  " at object: " + str(err_obj))
    logger.error("Psycopg2 traceback:" + str(traceback) +
                  "-- type:" + str(err_type))
    logger.error("Extensions.Diagnostics:" + str(err.diag))
    logger.error("Pgerror:" + str(err.pgerror))
    logger.error("Pgcode:" + str(err.pgcode))
    
# função para conectar ao banco de dados
# function to connect on database
def connectDB(conn=conn):
    logger.info("Conectando ao banco de dados.")
    try:
        conn
    except OperationalError as err:
        logger.error("Erro ao conectar ao banco de dados.")
        print_psycopg2_exception(err)

        conn = None
    else:
        logger.info("Conectado ao banco de dados.")

    if conn != None:
        cur = conn.cursor()

    return cur

# função para fechar o cursor e o conexão do banco de dados
# function to close cursor and connection with database
def close_conection(cur):
    cur.close()
    logger.info('Cursor fechado.')
    conn.close()
    logger.info('Conexao fechada.')