#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    move_right(6)
    while(wall_is_beneath() == True):
        move_right()
        


if __name__ == '__main__':
    run_tasks()
