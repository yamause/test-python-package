# Yamause の Python お試し部屋

Python のパッケージングと mkdocs を利用したドキュメント作成の個人的な練習ノートだよ

## はじめに

<div class="grid cards" markdown>

-   :material-fountain-pen-tip:{ .lg .middle } __Blogを始める__

    ---

    Blog は自由に記述することができノウハウを共有します。

    [:octicons-arrow-right-24: Getting started](blog/posts/hello-world.md)

-   :fontawesome-brands-markdown:{ .lg .middle } __Pythonコードリファレンスをかく__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __ドキュメントをかく__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>

## メモ

### ハンドブック - 運用ガイドラインとベストプラクティスどっちに書く？書き分けについて

**運用ガイドライン** は目的に対して、どのようにその目的を達成するのか道筋を示します。技術的な詳細は記載してはいけません。例えばPythonのパッケージングのガイドラインでは `pyproject.toml` の内容について一切触れるべきではありません。パッケージングするうえで必要なコマンドとなぜその手順を実行すべきかのみを説明します。

※手順内でファイルを更新する場合などは更新個所について説明をすべきです。

**ベストプラクティス** は推奨される構成について記載します。例えばPythonのパッケージングのベストプラクティスでは `pyproject.toml` の設定内容について、なぜその設定値が推奨されるのか技術的な観点から説明を記載します。

### 忘れちゃいけないこと

人は見出しに書いてある以上の情報を求めていない。目的の情報を簡潔に提供することを重視する。話が広がりそうなときは別の記事に書いてリンクする。
