+++
id = "ref/spell/spellcurse"
kind = "spell"
title = "Spellcurse"
aon = "SpellDisplay.aspx?ItemName=Spellcurse"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellcurse", path = "json/spells9.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "6"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a fragment of a destroyed magical item)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Inquisitor\
3: Cleric, Oracle, Psychic, Witch\
4: Occultist, Shaman
Casting time: 1 standard action
Components: V, S, M (a fragment of a destroyed magical item)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: 1 creature
Descriptors: curse
:::

You disrupt any spell energy affecting your target, causing that energy to crackle with power and
harm the target. The target takes 1d6 points of damage for each spell with a duration of 1 round or
greater currently affecting it. The spells themselves are not dispelled or modified.
