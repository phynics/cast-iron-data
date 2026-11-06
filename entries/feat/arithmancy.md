+++
id = "ref/feat/arithmancy"
kind = "feat"
title = "Arithmancy"
source_ids = ["occult-mysteries"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arithmancy", path = "json/feat01.json" },
]

[fields]
kind = "feat"
prerequisites = "Int 13, Spell Focus (divination), Spellcraft 3 ranks."
prerequisite_feats = ["ref/feat/spell-focus"]
benefit = "Immediately before casting a spell, as a swift action, you can attempt to augment a spell's casting using Arithmancy. To do so, determine the digital root of the name of the spell you are casting."
+++

**Sources:** Occult Mysteries pg 48

You are able to unravel the hidden meanings behind words by translating them into numerical
equations. You can apply this insight to empower your magical effects.\
**Prerequisites:** Int 13, [Spell Focus](ref/feat/spell-focus) (divination), Spellcraft 3 ranks.\
**Benefit:** Immediately before casting a spell, as a swift action, you can attempt to augment a
spell's casting using Arithmancy. To do so, determine the digital root of the name of the spell you
are casting.

To find the digital root of a spell name, first assign a numerical value to each letter of the name,
per the Letter Values table. Once you have a string of digits, sum them.

|Numerical Value|Associated Letters|
| --- | --- |
|1|a, j, s|
|2|b, k, t|
|3|c, l, u|
|4|d, m, v|
|5|e, n, w|
|6|f, o, x|
|7|g, p, y|
|8|h, q, z|
|9|i, r|

If the result has more than one digit, sum those digits. Repeat this process until you arrive at a
single number, called the digital root.

Once you've translated the name of the spell into a single digital root, attempt a Spellcraft check
with a DC equal to 10 + the spell level + the digital root. If your check succeeds, the spell is
cast at +1 caster level. If your check fails, the spell is cast at -1 caster level. If you do not
cast the spell you intended to augment with arithmancy, the spell is expended with no effect, though
you retain the action you would have spent to cast it. Metamagic effects are not included in a
spell's name when determining the spell's digital root, but they increase the spell's level as
normal when determining the DC of the Spellcraft check.

You can use this ability a number of times per day equal to the number of caster levels you possess.

For example, Ezren wants to use Arithmancy to cast an augmented [fireball](ref/spell/fireball).
First, he translates the spell name into numbers. Fireball translates to 6, 9, 9, 5, 2, 1, 3, 3.
Then he calculates the digital root. In this case, 6 + 9 + 9 + 5 + 2 + 1 + 3 + 3 = 38, 3 + 8 = 11,
and 1 + 1 = 2. Therefore, the digital root of _[fireball](ref/spell/fireball)_ is 2. He then
attempts a Spellcraft check against a DC of 15 (10 + 3 \[_fireball's_ spell level\] + 2
\[_fireball's_ digital root\]). If his check succeeds, he can cast the
_[fireball](ref/spell/fireball)_ this round at +1 caster level. If he fails, he can cast the spell
at -1 caster level this round. He may also choose not to cast _[fireball](ref/spell/fireball)_ and
perform another action, though he expends the spell.
