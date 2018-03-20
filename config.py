import logging
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Config():
    logger=logging.getLogger("staticNew")
    logger.setLevel(logging.INFO)
    fh=logging.FileHandler("D:/JsonSch/a.log")
    fh.setLevel(logging.INFO)
    ch=logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fomater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(fomater)
    ch.setFormatter(fomater)
    logger.addHandler(fh)
    logger.addHandler(ch)
    def getlog(self):
        return self.logger
