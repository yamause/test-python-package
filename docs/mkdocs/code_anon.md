# コードに注釈を追加する

`mkdocs.yml` につぎの値を追記します。

```yaml
  features:
    - content.code.annotate
```

サンプルとして Markdown はつぎのように記載します。

=== "View"

    ```python
    import yamause

    yamause.say()  # (1)!
    ```

    1. ここに注釈を表示します

=== "Code"

    ````text
    ```python
    import yamause

    yamause.say()  # (1)!
    ```

    1. ここに注釈を表示します
    ````


---

参考： [Material for MkDocs. "Code bloks. Code annotations", (2025-03-02).](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/?h=code#code-annotations)
