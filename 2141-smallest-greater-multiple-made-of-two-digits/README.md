<h2><a href="https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits">Smallest Greater Multiple Made of Two Digits</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Given three integers, <code>k</code>, <code>digit1</code>, and <code>digit2</code>, you want to find the <strong>smallest</strong> integer that is:</p>

<ul>
	<li><strong>Larger</strong> than <code>k</code>,</li>
	<li>A <strong>multiple</strong> of <code>k</code>, and</li>
	<li>Comprised of <strong>only</strong> the digits <code>digit1</code> and/or <code>digit2</code>.</li>
</ul>

<p>Return <em>the <strong>smallest</strong> such integer. If no such integer exists or the integer exceeds the limit of a signed 32-bit integer (</em><code>2<sup>31</sup> - 1</code><em>), return </em><code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 2, digit1 = 0, digit2 = 2
<strong>Output:</strong> 20
<strong>Explanation:</strong>
20 is the first integer larger than 2, a multiple of 2, and comprised of only the digits 0 and/or 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 3, digit1 = 4, digit2 = 2
<strong>Output:</strong> 24
<strong>Explanation:</strong>
24 is the first integer larger than 3, a multiple of 3, and comprised of only the digits 4 and/or 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 2, digit1 = 0, digit2 = 0
<strong>Output:</strong> -1
<strong>Explanation:
</strong>No integer meets the requirements so return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>0 &lt;= digit1 &lt;= 9</code></li>
	<li><code>0 &lt;= digit2 &lt;= 9</code></li>
</ul>
