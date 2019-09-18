import configparser

# 修改配置文件绝对路径
filepath_config = '/home/yanan/Documents/python/config.ini'

class Config_parser:
    '''获取和修改参数文件基类'''
    def __init__(self, filepath):
        config = configparser.ConfigParser()
        config.read(filepath)
        self.config = config
        self.filepath = filepath
        self.sections = config.sections()
        
    def get_config(self, sections, options):
        '''获取参数方法'''
        return self.config.get(sections, options)

    def change_config(self, sections, options):
        pass


class Sqoop(Config_parser):
    '''sqoop任务'''
    def __init__(self, task_name, filepath):
        Config_parser.__init__(self, filepath)
        self.task_name = task_name

    def create_script(self):
        script = "run script %s" % self.task_name
        return script

    def run_task(self):
        return self.create_script()

class Beeline(Config_parser):
    '''beeline任务'''
    pass

class Schedual():
    '''调度任务'''
    pass

class Logger():
    '''任务日志'''
    pass

## 20190918 test
## 123