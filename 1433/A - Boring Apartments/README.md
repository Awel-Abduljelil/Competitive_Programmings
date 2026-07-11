<h2><a href="https://codeforces.com/contest/1433/problem/A" target="_blank" rel="noopener noreferrer">1433A — Boring Apartments</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | C++23 (GCC 14-64, msys2) |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1433A](https://codeforces.com/contest/1433/problem/A) |

## Topics
`implementation` `math`

---

## Problem Statement

<div class="header"><div class="title">A. Boring Apartments</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>There is a building consisting of $$$10~000$$$ apartments numbered from $$$1$$$ to $$$10~000$$$, inclusive.</p><p>Call an apartment <span class="tex-font-style-bf">boring</span>, if its number consists of <span class="tex-font-style-it">the same digit</span>. Examples of boring apartments are $$$11, 2, 777, 9999$$$ and so on.</p><p>Our character is a troublemaker, and he calls the intercoms of all <span class="tex-font-style-bf">boring</span> apartments, till someone answers the call, in the following order:</p><ul> <li> First he calls all apartments consisting of digit $$$1$$$, in increasing order ($$$1, 11, 111, 1111$$$). </li><li> Next he calls all apartments consisting of digit $$$2$$$, in increasing order ($$$2, 22, 222, 2222$$$) </li><li> And so on. </li></ul><p>The resident of the boring apartment $$$x$$$ answers the call, and our character <span class="tex-font-style-bf">stops</span> calling anyone further.</p><p>Our character wants to know how many digits he pressed in total and your task is to help him to count the total number of keypresses.</p><p>For example, if the resident of boring apartment $$$22$$$ answered, then our character called apartments with numbers $$$1, 11, 111, 1111, 2, 22$$$ and the total number of digits he pressed is $$$1 + 2 + 3 + 4 + 1 + 2 = 13$$$.</p><p>You have to answer $$$t$$$ independent test cases.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains one integer $$$t$$$ ($$$1 \le t \le 36$$$) — the number of test cases.</p><p>The only line of the test case contains one integer $$$x$$$ ($$$1 \le x \le 9999$$$) — the apartment number of the resident who answered the call. It is guaranteed that $$$x$$$ consists of the same digit.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print the answer: how many digits our character pressed in total.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0017315899226625198" id="id005815859562571175" class="input-output-copier">Copy</div></div><pre id="id0017315899226625198">4
22
9999
1
777
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id003130677531671533" id="id004930798735993913" class="input-output-copier">Copy</div></div><pre id="id003130677531671533">13
90
1
66
</pre></div></div></div>