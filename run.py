import unittest
import HTMLTestReportCN
import time
import os
from cases.login import Login
from cases.case_orderlist import OrderList


suite=unittest.TestSuite()
# suite.addTest(Login("test_login"))
# suite.addTest(OrderList("test_query"))
suite=unittest.defaultTestLoader.discover(start_dir=os.path.dirname(__file__)+"/cases",pattern="case_*.py")

file_name=time.strftime("%y_%m_%d %H_%M_%S",time.localtime(round(time.time())))
file=open(os.path.dirname(__file__)+"/report/{file_name}.html".format(file_name=file_name),"wb")

HTMLTestReportCN.HTMLTestRunner(stream=file,title="保险系统",tester="田哥").run(suite)

# unittest.TextTestRunner().run(suite)
