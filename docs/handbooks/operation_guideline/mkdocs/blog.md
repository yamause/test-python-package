# Blogの始め方

## 新規記事の投稿

`mkdocs.yml` を編集し、 `nav` セクションに新しい投稿のファイルパスを追加します。

```yaml title="mkdocs.yml"
nav:
  - Blog:
      - blog/index.md
      - blog/posts/new-post.yml  # 新規記事
```

`docs/blog/posts/` 配下に記事を書くためのYAMLファイルを作成します。
ファイルの先頭に記事のメタ情報を記述し、その下に本文を記述します。


```yaml title="docs/blog/posts/new-post.yml"
---
draft: false # (1)
date: # (2)
  created: 2023-12-31
  updated: 2024-01-02
authors: # (3)
  - yamause
categories: # (4)
  - tech
links: # (5)
  - reference/yamause.md
tags: # (6)
  - blog
---

# Hello world!

以下、本文

```

1. __draft__: `true` の場合はブラウザに表示されません。
2. __date__: 記事の投稿日と更新日
3. __authors__: 記事の著者
4. __categories__: 記事をカテゴリーごとに分類できます。カテゴリーはナビゲーションバーに表示されます。利用可能なカテゴリーは `mkdocs.yml` に記述します。

    ```yaml title="mkdocs.yml"
    plugins:
      - blog:
          categories_allowed:
            - tech
            - news
            - poem
        # これはサンプルです。
        # 最新の設定は直接ファイルを確認してください。
    ```
5. __links__: 記事の関連リンク

## プロフィールの作成

`.authors.yml` に authors のプロフィールを作成します。

```yaml title="docs/blog/.authors.yml"
authors:
  yamause:
    name: Yamause
    description: Creator
    avatar: https://github.com/yamause.png
```
