# 一般公開の手順

このアプリケーションを一般公開する方法を説明します。

## 方法1: Streamlit Cloud（推奨・無料）

### 1. GitHubにリポジトリを作成

1. [GitHub](https://github.com)にアカウントを作成（まだの場合）
2. 新しいリポジトリを作成
   - リポジトリ名: `image-collector` など
   - Public（公開）を選択
   - README、.gitignore、ライセンスは追加しない（既に作成済み）

### 2. ローカルでGitリポジトリを初期化

```bash
# Gitがインストールされていることを確認
git --version

# リポジトリを初期化
git init

# ファイルを追加
git add app.py requirements.txt README.md .gitignore

# 初回コミット
git commit -m "Initial commit: 画像収集アプリ"

# GitHubリポジトリを追加（YOUR_USERNAMEとYOUR_REPO_NAMEを置き換え）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# プッシュ
git branch -M main
git push -u origin main
```

### 3. Streamlit Cloudにデプロイ

1. [Streamlit Cloud](https://streamlit.io/cloud)にアクセス
2. GitHubアカウントでログイン
3. 「New app」をクリック
4. 設定:
   - **Repository**: 作成したGitHubリポジトリを選択
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. 「Deploy!」をクリック

### 4. 公開URLの取得

デプロイが完了すると、以下のようなURLが生成されます：
```
https://YOUR_APP_NAME.streamlit.app
```

このURLを共有すれば、誰でもアプリにアクセスできます！

## 方法2: その他のクラウドサービス

### Heroku
- 有料プランが必要な場合あり
- 設定がやや複雑

### AWS / GCP / Azure
- より高度な設定が可能
- コストがかかる場合あり

## 注意事項

### セキュリティ
- 公開する前に、機密情報が含まれていないか確認
- 大量のリクエストに対する制限を検討

### 利用規約
- Bing画像検索の利用規約を遵守
- 収集した画像の著作権に注意
- 利用規約を明記することを推奨

### パフォーマンス
- Streamlit Cloudの無料プランには制限があります
- 同時接続数やリソース使用量に注意

## トラブルシューティング

### デプロイエラー
- `requirements.txt`の依存関係を確認
- Streamlit Cloudのログを確認

### アプリが動作しない
- ローカルで動作確認
- エラーメッセージを確認

