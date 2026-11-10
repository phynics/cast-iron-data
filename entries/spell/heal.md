+++
id = "ref/spell/heal"
kind = "spell"
title = "Heal"
aon = "SpellDisplay.aspx?ItemName=Heal"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heal", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "294"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 5 },
  { class = "Alchemist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 7 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Adept\
6: Alchemist, Cleric, Inquisitor, Investigator, Occultist, Oracle, Spiritualist, Warpriest\
7: Druid, Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

Heal enables you to channel positive energy into a creature to wipe away injury and afflictions. It
immediately ends any and all of the following adverse conditions affecting the target: ability
damage, blinded, confused, dazed, dazzled, deafened, diseased, exhausted, fatigued, feebleminded,
insanity, nauseated, poisoned, sickened, and stunned. It also cures 10 hit points of damage per
level of the caster, to a maximum of 150 points at 15th level.

Heal does not remove negative levels or restore permanently drained ability score points.

If used against an undead creature, heal instead acts like [harm](ref/spell/harm).
