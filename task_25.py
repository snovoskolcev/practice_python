#!/usr/bin/python3

from pyrob.api import *

@task
def task_2_2():
    move_down(2)
    n=1
    while n < 6:
        n+=1
        fill_cell()
        move_down()
        move_right()
        fill_cell()
        move_up()
        fill_cell()
        move_up()
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        if n < 6:
            move_right(2)
    else:
        move_up()
        move_left(2)


if __name__ == '__main__':
    run_tasks()
