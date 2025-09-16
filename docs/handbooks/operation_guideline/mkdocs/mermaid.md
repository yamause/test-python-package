# Mermaid を表示する

`mkdocs.yml` につぎの値を追記します。

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
```

サンプルとして Markdown はつぎのように記載します。

=== "View"

    ```mermaid
    flowchart LR
        Start --> Stop
    ```

=== "Code"

    ````markdown
    ```mermaid
    flowchart LR
        Start --> Stop
    ```
    ````


Mermaid の記法については公式のドキュメントを参照してください。[https://mermaid.js.org/intro/](https://mermaid.js.org/intro/)

---

参考： [Material for MkDocs. "Diagrams", (2025-03-02).](https://squidfunk.github.io/mkdocs-material/reference/diagrams/)
