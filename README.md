# 放物運動シミュレーション

初速度・投射角を変えて、放物運動の軌道・飛行時間・最高点・水平到達距離を可視化するツールです。重力加速度は \(g = 9.8\,\mathrm{m/s^2}\) です。

同じ計算を、実行環境に合わせて次の 3 ファイルで提供しています。

| ファイル | 用途 | 操作 UI |
| --- | --- | --- |
| [`parabolic_motion_streamlit.py`](parabolic_motion_streamlit.py) | ブラウザで動かす Web アプリ | Streamlit のスライダー |
| [`parabolic_motion_colab.ipynb`](parabolic_motion_colab.ipynb) | Google Colab で動かすノートブック | `ipywidgets` のスライダー |
| [`parabolic_motion_local.ipynb`](parabolic_motion_local.ipynb) | 手元の PC（Cursor / Jupyter）で動かすノートブック | matplotlib のスライダー |

どれを使うかは環境で選んでください。

- **PC に Python を入れて、ブラウザのスライダーで試す** → Streamlit（操作画面はブラウザだが、起動は手元の `streamlit run` が必要。Colab 上では普通は動かさない）
- **ブラウザだけで、インストールなしに試す** → Colab
- **Cursor 上でノートブックを動かす** → ローカル用ノートブック（Cursor では `ipywidgets` のスライダーが出ないため）

---

## 共通の操作

いずれも次の値を変えて軌道を更新します。

- **初速度 \(v_0\)** \([\mathrm{m/s}]\)
- **投射角 \(\theta\)** \([\mathrm{°}]\)
- **グラフの X / Y 軸上限** \([\mathrm{m}]\)

表示される数値は次のとおりです。

- 飛行時間（地面に戻るまで）
- 最高点
- 水平到達距離

---

## 1. Streamlit アプリ（`parabolic_motion_streamlit.py`）

ローカルで Web サーバーを起動し、ブラウザからスライダーを操作します。インストールと実行が簡単で、Cursor でも問題なく使えます。

### 必要なもの

- Python 3.12 以降（このリポジトリの仮想環境は 3.12）
- `streamlit`, `numpy`, `matplotlib`

### 実行方法

リポジトリのルートで:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install streamlit numpy matplotlib
streamlit run parabolic_motion_streamlit.py
```

macOS / Linux では有効化は `source .venv/bin/activate` です。

起動するとブラウザが開き、タイトル「放物運動シミュレーション」の画面が出ます。スライダーや数値入力を変えると、飛行時間・到達距離・最高点と軌道グラフが更新されます。終了するときはターミナルで `Ctrl+C` を押します。

---

## 2. Google Colab 用ノートブック（`parabolic_motion_colab.ipynb`）

クラウド上の Jupyter 環境で動かします。PC へのパッケージ導入は不要です。`ipywidgets` でスライダーを出すため、**Colab（または通常の Jupyter）向け**です。Cursor のノートブック UI ではスライダーが表示されません。

### 閲覧・実行方法

1. 次のバッジから Colab で開く（GitHub 上の `main` ブランチを参照します）。

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Amplil/physics_sim/blob/main/parabolic_motion_colab.ipynb)

2. または [Google Colab](https://colab.research.google.com/) で「GitHub」から `Amplil/physics_sim` の `parabolic_motion_colab.ipynb` を開く。
3. ランタイムに接続したあと、**上から順にセルを実行**する（メニューの「ランタイム → すべてのセルを実行」でも可）。

スライダー（初速度・角度）と数値入力（軸上限）が出るので、値を変えるとグラフと数値がその場で更新されます。Colab 上の `numpy` / `matplotlib` / `ipywidgets` で動作します。追加インストールは通常不要です。

---

## 3. ローカル用ノートブック（`parabolic_motion_local.ipynb`）

手元の Jupyter カーネルで動かす版です。Cursor では `ipywidgets` が使えないため、**別ウィンドウの matplotlib 図**にスライダーを付けています。セル内ではなく、開いた図ウィンドウ側で操作します。

`%matplotlib tk` を使うので、**GUI が表示できる環境**（Windows のデスクトップなど）が必要です。ヘッドレス環境や Colab では動きません。Colab で試す場合は `parabolic_motion_colab.ipynb` を使ってください。

### 必要なもの

- Python 3
- `numpy`, `matplotlib`
- Tk が使える matplotlib バックエンド（Windows の公式 Python なら通常そのまま使えます）

### 実行・閲覧方法

1. Cursor または Jupyter で `parabolic_motion_local.ipynb` を開く。
2. **カーネルを再起動**してから、**上から順にセルを実行**する。
3. 図ウィンドウが開くので、下部のスライダーで初速度・角度・軸範囲を変える。

グラフ上に飛行時間・最高点・水平到達距離が表示されます。日本語フォント（游ゴシック / メイリオ / MS ゴシックなど）があれば軸ラベルも日本語になります。

JupyterLab / クラシック Notebook から開く場合の例:

```bash
.venv\Scripts\activate
pip install numpy matplotlib jupyter
jupyter notebook parabolic_motion_local.ipynb
```

---

## どれを使えばよいか

```text
手元の Python でブラウザ UI を出したい → parabolic_motion_streamlit.py
インストールせずクラウドで動かしたい   → parabolic_motion_colab.ipynb
Cursor でノートブックとして動かしたい → parabolic_motion_local.ipynb
```
