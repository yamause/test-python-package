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

````markdown
```mermaid
flowchart LR
    Start --> Stop
```
````

表示

```mermaid
flowchart LR
    Start --> Stop
```

---

参考： [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/diagrams/)
