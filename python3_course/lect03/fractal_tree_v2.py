"""
    作者：梁斌
    功能：利用递归函数绘制分形树
    版本：2.0
    日期：03/08/2017
    新增功能：叶子颜色；分支粗细
"""
import turtle


def draw_prepare(branch_length):
    """
       设置分形树当前分支颜色/粗细
    """
    if branch_length > 35:
        turtle.color('brown')
    else:
        turtle.color('green')
    turtle.pensize(branch_length / 10)


def draw_branch(branch_length):
    """
        绘制分形树
    """
    if branch_length > 5:
        # 绘制右侧树枝
        draw_prepare(branch_length)
        turtle.forward(branch_length)
        print('向前 ', branch_length)
        turtle.right(20)
        print('右转 20')
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        draw_prepare(branch_length)
        turtle.left(40)
        print('左转 40')
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        draw_prepare(branch_length)
        turtle.right(20)
        print('右转 20')
        turtle.backward(branch_length)
        print('向后 ', branch_length)


def main():
    """
        主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    # turtle.color('brown')
    draw_branch(80)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
