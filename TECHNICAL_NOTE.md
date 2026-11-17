# A 12-Word Ternary Code of Length 12 and Minimum Levenshtein Distance 8

**Theresa Rainaldi**  
Velorin Intelligence  
16 November 2026

## Abstract

We exhibit a ternary code of 12 distinct words of length 12 with minimum pairwise unit-cost Levenshtein distance 8. Hence \(E_3(12,8)\ge 12\), improving the previously listed lower bound 11. Four generators and their cyclic alphabet shifts specify the code. A complete certificate and standalone verifier accompany this note. Abraham Yeung independently verified the construction and updated his edit-code bounds table on 16 November 2026.

## 1. Definition and result

Let \(E_q(n,d)\) denote the maximum cardinality of a subset \(C\subseteq\{0,\ldots,q-1\}^n\) such that any two distinct words have Levenshtein distance at least \(d\), with unit cost for insertion, deletion and substitution.

**Proposition.** \(E_3(12,8)\ge12\).

## 2. Explicit construction

Let \(\sigma_k\) apply the cyclic alphabet shift \(x\mapsto(x+k)\bmod3\) to each symbol. Use these four generators:

```text
000002222211
000111111222
002120201010
022222002222
```

Define \(C=\{\sigma_k(g):g\text{ is a listed generator},\ k\in\{0,1,2\}\}\). Its 12 distinct words, sorted lexicographically, are:

```text
000002222211
000111111222
002120201010
022222002222
100000110000
110201012121
111110000022
111222222000
211111221111
221012120202
222000000111
222221111100
```

## 3. Certificate verification and proof

For words \(a\) and \(b\), compute unit-cost Levenshtein distance using \(D(i,0)=i\), \(D(0,j)=j\) and

\[
D(i,j)=\min\{D(i-1,j)+1,\ D(i,j-1)+1,\ D(i-1,j-1)+[a_i\ne b_j]\}.
\]

The accompanying Python program checks the 12 distinct length-12 ternary words, the exact canonical certificate file, and all 66 unordered pairs. The pairwise distance histogram is 57 at distance 8, 3 at distance 9, 3 at distance 10, and 3 at distance 11. In particular every distinct pair has distance at least 8, so \(C\) witnesses \(E_3(12,8)\ge12\). The minimum distance of this particular \(C\) is exactly 8.

## 4. Computational provenance and independent verification

The construction was found through AI-assisted computational search described in the submission as seeded alphabet-shift orbit search with exact compatibility repair. The original search source and execution logs are not included in this release; accordingly the discovery pipeline is not claimed to be reproducible. The explicit construction and distance certificate are reproducible.

On 16 November 2026 Abraham Yeung reported independently reconstructing the codewords, matching the certificate SHA-256, and verifying the result using five independently implemented methods: ball marking, sort-based ball collision, ordinary pairwise, bit-parallel pairwise, and brute-force all-pairs checks. He accepted the improved lower bound and credited Theresa Rainaldi (Velorin Intelligence) in his public table.

## 5. Scope, artifacts and provenance

This result improves a constructive lower bound only; it does not determine the exact value of \(E_3(12,8)\) or alter its upper bound. The canonical `codewords.txt` uses ASCII, lexicographic order, and a trailing newline. Its SHA-256 is:

```text
7cec0c303acdc6cbc1bf7018ad9af0ab96f89e9d4c37e18c5b4d54887c42b102
```

Run `python verify_edit_code.py` in the same directory as `codewords.txt`.

## References

1. A. Yeung, *Edit Codes*, bounds table, entry \(E_3(12,8)\), https://abrahamyeung.com/edit-codes/#r3-12-8 (accessed 16 November 2026).
2. A. Yeung, email to T. Rainaldi, 16 November 2026, independent verification and acceptance (private correspondence).
3. T. Rainaldi, original certificate submission to A. Yeung, 16 November 2026 (private correspondence).
