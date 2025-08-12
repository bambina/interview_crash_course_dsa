## Arrays and strings
1D arrayとstringは「要素が順に並ぶ」という点で似ている。
Pythonのstringはimmutableなのでlistに変換して解く。stringのランダムアクセスはO(1)。
```Python
list("abc")
"".join(["a","b","c"])
"abc"[2] #=> "c"
```
list末尾への追加はamortized O(1)。最悪の場合は、容量不足の時、通常2倍の長さのリストを作り、要素をコピーするとO(n)。

テクニック
- Two pointers
  - Opposite Ends: 2つのポインタをlist前後から走査する。2つのポインタが出会うまで各ループで近づくので計算時間はO(n)。空間はO(1)。2つのiterablesがある場合はO(n+m)。
  - Sliding window: 2つのポインタを同じ場所から開始して、片方が先に進む。制約条件を満たすcurrを持つsubarrayを探す。計算時間はO(n)。空間はO(1)。valid subarrayの数と長さは right-left+1。
- Prefix sum: 前処理として要素の累積和をO(n)で作る。Prefix sumを使い要素間(i to j)の総和をO(1)で求める。
```python
prefix[j] - prefix[i] + nums[i]
```

## Linked lists

長所:
- 挿入・削除がO(1): 該当ノードの参照があれば、要素のシフトが不要のため
- 動的サイズ: 長さに制限がなく、配列と違いresizingがない

短所:
- ランダムアクセスがO(n): 配列のO(1)と異なり、特定位置まで辿る必要がある
- メモリオーバーヘッド: 各ノードがポインタを保持するため、配列より多くのメモリを消費

使い所
頻繁な挿入・削除があり、ランダムアクセスが少ない場合に有効

テクニック:
- Fast and slow pointers: O(n) でcycle検知やmiddle node取得ができる
- Reversing: ポインタの付け替え。考えた手順と実行手順は必ずしも一致しない

## Stacks


----


## Terms

- **Palindrome**: A string that reads the same forward and backward.  
  _Example_: `"racecar"` is a palindrome.

- **Subarray**: A contiguous section of an array.  
  _Example_: For the array `[1, 2, 3, 4]`, `[2, 3]` is a subarray.

- **Subsequence**: A sequence of characters that can be derived from another string by deleting zero or more characters, without changing the order of the remaining characters.  
  _Example_: `"ace"` is a subsequence of `"abcde"`.
