+++
id = "ref/rule/counterspells"
kind = "rule"
title = "Counterspells"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "counterspells", path = "json/rules_basics04.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 207

It is possible to cast any spell as a counterspell. By doing so, you are using the spell's energy to
disrupt the casting of the same spell by another character. Counterspelling works even if one spell
is divine and the other arcane.

**How Counterspells Work:** To use a counterspell, you must select an opponent as the target of the
counterspell. You do this by choosing to ready an action ([see Combat](ref/rule/combat)). In doing
so, you elect to wait to complete your action until your opponent tries to cast a spell. You may
still move at your normal speed, since ready is a standard action.

If the target of your counterspell tries to cast a spell, make a Spellcraft check (DC 15 + the
spell's level). This check is a free action. If the check succeeds, you correctly identify the
opponent's spell and can attempt to counter it. If the check fails, you can't do either of these
things.

To complete the action, you must then cast an appropriate spell. As a general rule, a spell can only
counter itself. If you are able to cast the same spell and you have it prepared (or have a slot of
the appropriate level available), you cast it, creating a counterspell effect. If the target is
within range, both spells automatically negate each other with no other results.

**Counterspelling Metamagic Spells:** Metamagic feats are not taken into account when determining
whether a spell can be countered.

**Specific Exceptions:** Some spells can counter other specific spells, often those with
diametrically opposed effects.

**Dispel Magic as a Counterspell:** You can usually use [dispel magic](ref/spell/dispel-magic) to
counterspell another spell being cast without needing to identify the spell being cast. Dispel magic
doesn't always work as a counterspell (see the spell description).
