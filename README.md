# practice-azure-serverless

azure環境でサーバレスアプリケーションを実現するための練習用プログラム。
ついでにフロントエンドとしてSvelteも触ってみる。

## 参考

- [svelte documentation](https://svelte.jp/docs#getting-started)
- AzureのPython SDK関連
  - [SDKの公式サンプルコード](https://github.com/Azure/azure-sdk-for-python)
  - [cosmos関連の関数についてまとめているページ](https://learn.microsoft.com/ja-jp/azure/cosmos-db/nosql/samples-python)
  - [azure-cosmos package documentation](https://learn.microsoft.com/ja-jp/python/api/azure-cosmos/azure.cosmos?preserve-view=true&view=azure-python)
  - [pythonでcosomosを利用するためのtutorialプログラム](https://github.com/Azure-Samples/azure-cosmos-db-python-getting-started/blob/main/cosmos_get_started.py)

## 作業ログ

### 初期設定

setup svelte

```powershell
npm create vite@latest practice-azure-serverless -- --template svelte
```

Azure Functions のローカルでのセットアップ。
VSCode Extentionsでセットアップするのではなく、powershellでfunc(Azureからダウンロード)を利用しないと、指定したディレクトリにFunctionsのプログラムを展開できなかったので、このコマンドを使った。

```powershell
func init api
```

その後、VSCode上で Azure - WORKSPACE(左下にある)から`Local Project`を選択し、initみたいなやつをクリックすると`.vscode/extentions.json`にazurefunctionとその言語について追記してくれて、
GUI上で作ったfunctionが作ったディレクトリ(ここでは`api`)に収まるようになる。

### Azure Cosmos DB Emulatorとの接続まで

localに環境変数を設定するのは億劫なので`api.local.settings.json`に設定ファイルを置く。
その内容の例は[api.local.settings.example.json](./api/local.settings.example.json)を参照。

ローカルでのFunctionの実行は、VSCode Extentionを使えばできる。
WORKSPACE(左下にある)のLocalProjectを選択してF5で起動し、テストしたい関数を右クリックで実行すればよい。

> TODO: F5を押したときエラーが起きるが、`Debug anyway`を押せば動く。しかし、意味をわかっていないので、調査が必要。
