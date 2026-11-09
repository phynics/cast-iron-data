+++
id = "ref/spell/inflict-light-wounds"
kind = "spell"
title = "Inflict Light Wounds"
aon = "SpellDisplay.aspx?ItemName=Inflict%20Light%20Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_light_wounds", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "300"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Cleric, Inquisitor, Occultist, Oracle, Shaman, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: creature touched
:::

When laying your hand upon a creature, you channel negative energy that deals 1d8 points of damage +
1 point per caster level (maximum +5).

Since undead are powered by negative energy, this spell cures such a creature of a like amount of
damage, rather than harming it.
