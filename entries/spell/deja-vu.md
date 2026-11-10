+++
id = "ref/spell/deja-vu"
kind = "spell"
title = "Deja Vu"
aon = "SpellDisplay.aspx?ItemName=Deja%20Vu"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deja_vu", path = "json/spells3.json" },
]
[[sources]]
publication = "occult-adventures"
page = "163"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "2 rounds"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: 2 rounds
Saving throw: none
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You reach into the target's mind and put its thought processes into a temporary loop. Whatever
full-round, standard, or move actions the creature takes on its first turn after you cast this
spell, it must repeat on the turn after that. The creature must take the same type of actions in the
same order (for example, making a full attack, casting a specific spell, withdrawing, attempting a
bull rush combat maneuver, or activating a magic item) and must act against the same target or
targets, but doesn't have to make exactly the same choices (such as using
[Power Attack](ref/feat/power-attack) when attacking, moving exactly 15 feet, or choosing "drop" for
the command spell). If the circumstances would prevent the target from repeating an action, such as
if the target of its attack is dead or the target cannot cast the same spell again, the target
instead becomes confused until the spell ends. A creature currently affected by deja vu can't be
targeted with another deja vu spell. A creature affected by deja vu can't delay, and if it readies
an action on its first turn, it must ready the same action on its second turn.
