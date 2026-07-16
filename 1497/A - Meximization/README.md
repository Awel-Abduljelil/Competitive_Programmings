<h2><a href="https://codeforces.com/contest/1497/problem/A" target="_blank" rel="noopener noreferrer">1497A — Meximization</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1497A](https://codeforces.com/contest/1497/problem/A) |

## Topics
`brute force` `data structures` `greedy` `sortings`

---

## Problem Statement

<div class="header"><div class="title">A. Meximization</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>You are given an integer $$$n$$$ and an array $$$a_1, a_2, \ldots, a_n$$$. You should reorder the elements of the array $$$a$$$ in such way that the sum of $$$\textbf{MEX}$$$ on prefixes ($$$i$$$-th prefix is $$$a_1, a_2, \ldots, a_i$$$) is maximized.</p><p>Formally, you should find an array $$$b_1, b_2, \ldots, b_n$$$, such that the sets of elements of arrays $$$a$$$ and $$$b$$$ are equal (it is equivalent to array $$$b$$$ can be found as an array $$$a$$$ with some reordering of its elements) and $$$\sum\limits_{i=1}^{n} \textbf{MEX}(b_1, b_2, \ldots, b_i)$$$ is maximized.</p><p>$$$\textbf{MEX}$$$ of a set of nonnegative integers is the minimal nonnegative integer such that it is not in the set.</p><p>For example, $$$\textbf{MEX}(\{1, 2, 3\}) = 0$$$, $$$\textbf{MEX}(\{0, 1, 2, 4, 5\}) = 3$$$.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ $$$(1 \le t \le 100)$$$  — the number of test cases.</p><p>The first line of each test case contains a single integer $$$n$$$ $$$(1 \le n \le 100)$$$.</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ $$$(0 \le a_i \le 100)$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print an array $$$b_1, b_2, \ldots, b_n$$$  — the optimal reordering of $$$a_1, a_2, \ldots, a_n$$$, so the sum of $$$\textbf{MEX}$$$ on its prefixes is maximized.</p><p>If there exist multiple optimal answers you can find any.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0017419856046870996" id="id007954186275438757" class="input-output-copier">Copy</div></div><pre id="id0017419856046870996">3
7
4 2 0 1 3 3 7
5
2 2 8 6 9
1
0
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008092835676530077" id="id0007653724161415376" class="input-output-copier">Copy</div></div><pre id="id008092835676530077">0 1 2 3 4 7 3 
2 6 8 9 2 
0 
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case in the answer $$$\textbf{MEX}$$$ for prefixes will be: </p><ol> <li> $$$\textbf{MEX}(\{0\}) = 1$$$ </li><li> $$$\textbf{MEX}(\{0, 1\}) = 2$$$ </li><li> $$$\textbf{MEX}(\{0, 1, 2\}) = 3$$$ </li><li> $$$\textbf{MEX}(\{0, 1, 2, 3\}) = 4$$$ </li><li> $$$\textbf{MEX}(\{0, 1, 2, 3, 4\}) = 5$$$ </li><li> $$$\textbf{MEX}(\{0, 1, 2, 3, 4, 7\}) = 5$$$ </li><li> $$$\textbf{MEX}(\{0, 1, 2, 3, 4, 7, 3\}) = 5$$$ </li></ol> The sum of $$$\textbf{MEX} = 1 + 2 + 3 + 4 + 5 + 5 + 5 = 25$$$. It can be proven, that it is a maximum possible sum of $$$\textbf{MEX}$$$ on prefixes.</div>