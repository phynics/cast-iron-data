+++
id = "ref/spell/cure-light-wounds"
kind = "spell"
title = "Cure Light Wounds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cure_light_wounds", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "263"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Alchemist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
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
saving_throw = "Will half (harmless)"
spell_resistance = "yes (harmless); see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Adept, Alchemist, Bard, Cleric, Druid, Hunter, Inquisitor, Investigator, Occultist, Oracle, Paladin, Shaman, Skald, Spiritualist, Warpriest, Witch\
2: Ranger
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half (harmless)
Spell resistance: yes (harmless); see text
Target: creature touched
Subschool: Healing
:::

When laying your hand upon a living creature, you channel positive energy that cures 1d8 points of
damage + 1 point per caster level (maximum +5). Since undead are powered by negative energy, this
spell deals damage to them instead of curing their wounds. An undead creature can apply
[spell resistance](ref/rule/spell-resistance), and can attempt a Will save to take half damage.
