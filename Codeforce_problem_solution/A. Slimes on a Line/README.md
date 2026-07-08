<h2><a href="https://codeforces.com/contest/2127/problem/A" target="_blank" rel="noopener noreferrer">2127A — Slimes on a Line</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 2229A](https://codeforces.com/problemset/problem/2229/A) |

## Topics
`brute force` `greedy` `math` 

---

## Problem Statement

<div class="header">
<div class="title">A. Slimes on a Line</div>
<div class="time-limit">
<div class="property-title">time limit per test</div>
1 second
</div>
<div class="memory-limit">
<div class="property-title">memory limit per test</div>
256 megabytes
</div>
<div class="input-file input-standard" style="font-weight: bold">
<div class="property-title">input</div>
stdin
</div>
<div class="output-file output-standard" style="font-weight: bold">
<div class="property-title">output</div>
stdout
</div>
</div>

<div>
<p>There are <i>n</i> slimes on a line, where slime <i>i</i> is at position <i>a<sub>i</sub></i> on the line.</p>

<p>You may perform the following operation any number of times (possibly zero):</p>

<ul>
<li>Choose an integer <i>x</i>.</li>
<li>For every slime:
<ul>
<li>If <i>a<sub>j</sub> &lt; x</i>, then set <i>a<sub>j</sub> := a<sub>j</sub> + 1</i>.</li>
<li>If <i>a<sub>j</sub> &gt; x</i>, then set <i>a<sub>j</sub> := a<sub>j</sub> - 1</i>.</li>
<li>If <i>a<sub>j</sub> = x</i>, then it remains unchanged.</li>
</ul>
</li>
</ul>

<p>Determine the minimum number of operations required to make all slimes occupy the same position.</p>
</div>

<div class="input-specification">
<div class="section-title">Input</div>

<p>The first line contains an integer <i>t</i> (<b>1 ≤ t ≤ 100</b>) — the number of test cases.</p>

<p>For each test case:</p>

<ul>
<li>The first line contains an integer <i>n</i> (<b>2 ≤ n ≤ 1000</b>).</li>
<li>The second line contains <i>n</i> integers <i>a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub></i> (<b>1 ≤ a<sub>i</sub> ≤ 1000</b>).</li>
</ul>

<p>It is guaranteed that the sum of <i>n</i> over all test cases does not exceed <b>1000</b>.</p>
</div>

<div class="output-specification">
<div class="section-title">Output</div>

<p>For each test case, output the minimum number of operations needed to make all slimes occupy the same position.</p>
</div>

<div class="sample-tests">
<div class="section-title">Examples</div>

<div class="sample-test">

<div class="input">
<div class="title">Input</div>

<pre>
10
5
1 2 3 4 5
5
3 3 3 3 3
6
5 6 7 1 2 3
2
2 5
4
1 3 8 7
4
6 2 1 8
3
1 3 9
5
1 10 1 10 10
8
10 8 5 9 1 6 9 10
2
1 1000
</pre>

</div>

<div class="output">
<div class="title">Output</div>

<pre>
2
0
3
2
4
4
4
5
5
500
</pre>

</div>

</div>
</div>

<div class="note">
<div class="section-title">Note</div>

<p><b>Test Case 1:</b> Perform two operations with <i>x = 3</i>.</p>

<p>After the first operation:</p>

<pre>
[1,2,3,4,5] → [2,3,3,3,4]
</pre>

<p>After the second operation:</p>

<pre>
[2,3,3,3,4] → [3,3,3,3,3]
</pre>

<p>Therefore, the minimum number of operations is <b>2</b>.</p>

<p><b>Test Case 2:</b> All slimes are already at the same position, so the answer is <b>0</b>.</p>

</div>
