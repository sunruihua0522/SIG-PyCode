# encoding: utf-8
#!/usr/bin/env python
'''
@author: rabbit

@contact: 739462304@qq.com

@time: 2017/11/27 14:15

@desc:

'''

from flask_script import Manager, Shell

from main import app

manager=Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command("shell",Shell(make_context=make_shell_context))

@manager.command
def deploy():
    '''run deployment tasks'''
    pass


if __name__=='__main__':
    manager.run()