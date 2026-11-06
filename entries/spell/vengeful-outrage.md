+++
id = "ref/spell/vengeful-outrage"
kind = "spell"
title = "Vengeful Outrage"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vengeful_outrage", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Skald\
6: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, language-dependant, mind-affecting
:::

**Sources:** Ultimate Magic pg 246

You place a magical command upon a creature to seek out and destroy a single enemy that has
inflicted some perceived or actual harm to the target. You designate the enemy at the time of
casting, which must be known by the target (such as "your brother's murderer") or can easily
identify by sight (such as "the hill giant king"). The target is under the effect of a geas to find
and capture or kill this enemy, and the target takes the penalties of that spell as long as it is
not actively trying to reach the enemy. When the target enters combat with the enemy, it gains a +6
morale bonus to Strength and Constitution, a +3 morale bonus on Will saves, and is immune to the
shaken and frightened conditions.

If you designate one of the target's friends or loved ones as the enemy, the target gains another
saving throw to overcome the spell as soon as it enters combat with the enemy.
