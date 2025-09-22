"""MkDocsプラグインをデモンストレーションするモジュール。"""

class Yamause:
    """MkDocsプラグインをデモンストレーションするクラス。

    このクラスには、数値に1を加えるメソッドがあります。
    """

    def __init__(self):
        pass

    def add_one(self, num: int) -> int:
        """指定された数値に1を加えます。

        Examples:
            >>> yamause = Yamause()
            >>> yamause.add_one(1)
            2

        Args:
            num (int): 加える対象の数値。

        Returns:
            int: 数値に1を加えた結果。
        """
        return num + 1

    def say(self) -> str:
        """'Hello, world!'をコンソールに出力します。

        Returns:
            str: 'Hello, world!'という文字列。
        """
        return 'Hello, world!'


def add_one(hogehoge: int) -> int:
    """指定された数値に1を加えます。

    Examples:
        >>> add_one(1)
        2

    Args:
        hogehoge (int): 加える対象の数値。

    Returns:
        int: 数値に1を加えた結果。
    """
    return hogehoge + 1

def say() -> str:
    """'Hello, world!'をコンソールに出力します。

    Returns:
        str: 'Hello, world!'という文字列。
    """
    return 'Hello, world!'

if __name__ == '__main__':
    print(say())
