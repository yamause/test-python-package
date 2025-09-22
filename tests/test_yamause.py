
"""yamauseモジュールのテストケースを定義するモジュール。"""

def test_add_one():
    """Yamauseクラスのadd_oneメソッドとモジュールレベルのadd_one関数が同じ動作をすることを確認するテストケース。"""
    from yamause.example import Yamause
    from yamause.example import add_one as add_one_func
    yamause = Yamause()
    assert add_one_func(1) == yamause.add_one(1)
    assert add_one_func(2) == yamause.add_one(2)
    assert add_one_func(3) == yamause.add_one(3)
    assert add_one_func(4) == yamause.add_one(4)
