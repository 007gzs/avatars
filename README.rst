#############################
Avatars
#############################

多种风格SVG头像生成工具

.. image:: https://github.com/007gzs/avatars/raw/master/resource/bottts_1.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/bottts_2.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/female_1.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/female_2.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/identicon_1.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/identicon_2.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/initials_1.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/initials_2.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/male_1.svg
.. image:: https://github.com/007gzs/avatars/raw/master/resource/male_2.svg

********
安装
********

目前 Avatars 支持的 Python 环境有 2.7, 3.4, 3.5, 3.6, 3.7 和 pypy。

为了简化安装过程，推荐使用 pip 进行安装

.. code-block:: bash

    pip install avatars

升级 Avatars 到新版本::

    pip install -U avatars

如果需要安装 GitHub 上的最新代码::

    pip install https://github.com/007gzs/avatars/archive/master.zip


********
使用
********

代码样例::

    from avatars.sprite import *
    print(MaleSprite().create("张三"))
    print(FemaleSprite().create("张三"))
    print(IdenticonSprite().create("张三"))
    print(BotttsSprite().create("张三"))
    print(InitialsSprite().create("张三"))

