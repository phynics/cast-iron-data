+++
id = "ref/spell/opportunistic-loyalty"
kind = "spell"
title = "Opportunistic Loyalty"
source_ids = ["pathfinder-115-trail-of-the-hunted"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "opportunistic_loyalty", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Antipaladin, Cleric, Inquisitor, Mesmerist, Oracle, Psychic, Warpriest, Witch
Casting time: 1 immediate action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
:::

**Sources:** Pathfinder \#115: Trail of the Hunted pg 75

Cast this spell when a creature within range casts a spell that provides an effect for its allies
(such as bless or prayer). You are considered an ally of the caster for the purposes of that spell.
Although you are momentarily considered an ally, the caster need not target you if the spell
requires that the caster select one or more allies to be affected by the spell (as does haste). This
spell does not allow a target spell to affect more creatures than described in its target entry. If
this spell would raise the total number of affected targets above that allowed by the target spell,
opportunistic loyalty has no effect.
