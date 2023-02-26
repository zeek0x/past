# past
PAST(Practical Algorithm Skill Test) の練習レポジトリ

## 環境構築

- [`oj`](https://github.com/online-judge-tools/oj) のインストール
- [`atcoder-cli`](https://github.com/Tatamo/atcoder-cli) のインストール

```console
oj login https://atcoder.jp/contests
acc login
cd `acc config-dir`
mkdir py && cd py
touch main.py template.json

# 以下を template.json に書き込む
{
  "task":{
    "program": ["main.py"],
    "submit": "main.py"
  }
}

acc config default-template
# 以下を ~/.zshrc などに書き込む
alias t='oj t -c "python3 ./main.py" -d ./tests/'
alias s='acc s --skip-filename -- -y --guess-python-interpreter pypy'
alias ts='t && s'
```

## 実行例

```console
$ acc new past202004-openx
past202004-open/contest.acc.json created.
create project of 第二回 アルゴリズム実技検定 過去問
? select tasks (Press <space> to select, <a> to toggle all, <i> to invert selection)
❯◉ A Elevator
 ◯ B Plurality Voting
 ◯ C Landslide
 ◯ D String Match
 ◯ E Permutation
 ◯ F Tasking
 ◯ G String Query

...

$ cd past202004-open/b/
$ t
[INFO] online-judge-tools 11.5.1 (+ online-judge-api-client 10.10.1)
[INFO] 4 cases found
[WARNING] GNU time is not available: gtime
[HINT] You can install GNU time with: $ brew install gnu-time

[INFO] sample-1
[INFO] time: 0.023990 sec
[SUCCESS] AC
...
$ s
```
