import  os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_DIR=os.path.join(BASE_DIR,"conf")
DATA_DIR=os.path.join(BASE_DIR,"datas")
CASE_DIR=os.path.join(BASE_DIR,"testcases")
REPORT_DIR=os.path.join(BASE_DIR,"reports")
LOG_DIR=os.path.join(BASE_DIR,"logs")
