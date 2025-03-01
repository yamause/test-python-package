# Yamause の Python お試し部屋

Python のパッケージングと autodoc を利用したドキュメント作成の個人的な練習ノートだよ

## memo

```python
def main():
    print("hogeohge")
```

```bash
echo "${HOME}"
```

`print("hogehoge")`

`#!php-inline $a = array("foo" => 0, "bar" => 1);`

### コードアノテーション

=== "View"

    ```yaml
    - name: hogehoge
        - hogehoge  # (1)!
    ```

    1. content.code.annotate を利用

=== "Code"

    ````text
    ```yaml
    - name: hogehoge
        - hogehoge  # (1)!
    ```

    1. content.code.annotate を利用
    ````
