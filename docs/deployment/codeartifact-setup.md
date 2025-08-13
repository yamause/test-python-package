# AWS CodeArtifact デプロイメント設定

このドキュメントでは、GitHub ActionsからOIDC認証を使用してAWS CodeArtifactにPythonパッケージをアップロードするための設定手順を説明します。

## 前提条件

- AWS アカウント
- GitHub リポジトリ
- AWS CodeArtifact ドメインとリポジトリが作成済み

## AWS側の設定

### 1. OIDC Identity Provider の作成

AWS IAMコンソールで以下の設定でOIDC Identity Providerを作成します：

- Provider URL: `https://token.actions.githubusercontent.com`
- Audience: `sts.amazonaws.com`

### 2. IAM Role の作成

以下のような信頼ポリシーを持つIAMロールを作成します：

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::YOUR_ACCOUNT_ID:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
        },
        "StringLike": {
          "token.actions.githubusercontent.com:sub": "repo:YOUR_GITHUB_USERNAME/YOUR_REPO_NAME:*"
        }
      }
    }
  ]
}
```

### 3. IAM Policy の作成とアタッチ

以下の権限を持つポリシーを作成し、上記のロールにアタッチします：

参考

- [AWS CodeArtifact アクセス許可リファレンス](https://docs.aws.amazon.com/ja_jp/codeartifact/latest/ug/auth-and-access-control-permissions-reference.html)
- [IAM ユーザーのプロビジョニング](https://docs.aws.amazon.com/ja_jp/codeartifact/latest/ug/get-set-up-provision-user.html)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "codeartifact:GetAuthorizationToken",
        "codeartifact:GetRepositoryEndpoint",
        "codeartifact:PublishPackageVersion"
      ],
      "Resource": [
        "arn:aws:codeartifact:YOUR_REGION:YOUR_ACCOUNT_ID:domain/YOUR_DOMAIN",
        "arn:aws:codeartifact:YOUR_REGION:YOUR_ACCOUNT_ID:repository/YOUR_DOMAIN/YOUR_REPOSITORY",
        "arn:aws:codeartifact:YOUR_REGION:YOUR_ACCOUNT_ID:package/YOUR_DOMAIN/YOUR_REPOSITORY/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "sts:GetServiceBearerToken",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "sts:AWSServiceName": "codeartifact.amazonaws.com"
        }
      }
    }
  ]
}
```

## GitHub側の設定

### Repository Secrets の設定

GitHubリポジトリの Settings > Secrets and variables > Actions で以下のシークレットを設定します：

| シークレット名 | 説明 | 例 |
|---|---|---|
| `AWS_ROLE_ARN` | 作成したIAMロールのARN | `arn:aws:iam::123456789012:role/GitHubActions-CodeArtifact` |
| `AWS_REGION` | AWSリージョン | `us-east-1` |
| `CODEARTIFACT_DOMAIN` | CodeArtifactドメイン名 | `my-company` |
| `CODEARTIFACT_DOMAIN_OWNER` | ドメインオーナーのAWSアカウントID | `123456789012` |
| `CODEARTIFACT_REPOSITORY` | CodeArtifactリポジトリ名 | `python-packages` |

## ワークフローの実行

### 自動実行

バージョンタグ（例：`v1.0.0`）をプッシュすると自動的にワークフローが実行されます：

```bash
git tag v1.0.0
git push origin v1.0.0
```

**バージョン自動更新機能:**
- タグから`v`プレフィックスを除いたバージョン番号（例：`1.0.0`）が自動的に抽出されます
- `yamause/__about__.py`ファイルの`__version__`が自動的に更新されます
- 更新されたバージョンでパッケージがビルドされ、CodeArtifactにアップロードされます

### 手動実行

GitHub ActionsのUIから手動でワークフローを実行することも可能です。
手動実行の場合は、現在の`yamause/__about__.py`のバージョンが使用されます。

## トラブルシューティング

### よくあるエラー

1. **OIDC認証エラー**
   - IAMロールの信頼ポリシーでリポジトリ名が正しく設定されているか確認
   - OIDC Identity Providerが正しく作成されているか確認

2. **CodeArtifact権限エラー**
   - IAMポリシーでCodeArtifactの必要な権限が付与されているか確認
   - ドメインとリポジトリのARNが正しいか確認

3. **パッケージアップロードエラー**
   - パッケージのビルドが正常に完了しているか確認
   - twineの設定が正しいか確認

### 依存関係がCodeArtifact上にある場合

現在のワークフローは、依存関係がない、またはPyPI上にある場合を想定しています。
もしパッケージの依存関係がCodeArtifact上のプライベートパッケージを含む場合は、
ビルド前にpipの設定を追加する必要があります：

```yaml
- name: Configure pip for CodeArtifact
  run: |
    pip config set global.index-url https://aws:${{ env.CODEARTIFACT_AUTH_TOKEN }}@${{ env.CODEARTIFACT_REPO_URL }}simple/
```

この設定を「Build package」ステップの前に追加してください。

### ログの確認

GitHub Actionsのログでエラーの詳細を確認できます。特に以下のステップのログを確認してください：

- AWS認証情報の設定
- CodeArtifact認証トークンの取得
- パッケージのアップロード

## セキュリティ考慮事項

- IAMロールの権限は最小限に設定する
- 信頼ポリシーで特定のリポジトリのみからのアクセスを許可する
- 定期的にアクセスログを確認する
- CodeArtifact認証トークンは`::add-mask::`でマスクされ、ログに表示されません
- 機密情報の漏洩を防ぐため、適切なログマスキングが実装されています
