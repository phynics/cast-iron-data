+++
id = "ref/spell/smite-abomination"
kind = "spell"
title = "Smite Abomination"
source_ids = ["inner-sea-gods", "pathfinder-44-trial-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "smite_abomination", path = "json/spells9.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "241"
[[sources]]
publication = "pathfinder-44-trial-of-the-beast"
page = "69"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Inquisitor\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

Drawing upon positive energy, you emulate some of a paladin's power to smite undead. Choose one
undead creature as your target. Your melee attacks against that target gain a bonus equal to your
Charisma or Wisdom modifier, whichever is higher, on your attack rolls, and a bonus equal to your
caster level on damage rolls. Your melee attacks also bypass the target's
[damage reduction](ref/rule/damage-reduction). These bonuses do not stack with the bonuses from a
paladin's smite.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
