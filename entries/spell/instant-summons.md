+++
id = "ref/spell/instant-summons"
kind = "spell"
title = "Instant Summons"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instant_summons", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (sapphire worth 1,000 gp)"
range = "see text"
effects = [
  { label = "Target", value = "one object weighing 10 lbs. or less whose longest dimension is 6 ft. or less" },
]
duration = "permanent until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (sapphire worth 1,000 gp)
Range: see text
Duration: permanent until discharged
Saving throw: none
Spell resistance: no
Target: one object weighing 10 lbs. or less whose longest dimension is 6 ft. or less
Subschool: Summoning
:::

**Sources:** PRPG Core Rulebook pg 301

You call some nonliving item directly to your hand from virtually any location.

First, you must place your arcane mark on the item. Then you cast this spell, which magically and
invisibly inscribes the name of the item on a sapphire worth at least 1,000 gp. Thereafter, you can
summon the item by speaking a special word (set by you when the spell is cast) and crushing the gem.
The item appears instantly in your hand. Only you can use the gem in this way.

If the item is in the possession of another creature, the spell does not work, but you know who the
possessor is and roughly where that creature is located when the summons occurs.

The inscription on the gem is invisible. It is also unreadable, except by means of a
[read magic](ref/spell/read-magic) spell, to anyone but you.

The item can be summoned from another plane, but only if no other creature has claimed ownership of
it.

### Greater Instant Summons

**Sources:** Ultimate Intrigue pg 217

This spell functions as instant summons, except that you can target multiple objects. You must use a
separate sapphire worth 1,000 gp for each one. For each item you target, you can touch a creature,
granting that creature the ability to speak the special word for that item (each item has its own
special word) while crushing the matched gem to call the item to hand. Only you or the touched
creature can activate the gem or see the arcane mark upon it.
