+++
id = "ref/spell/kinetic-reverberation"
kind = "spell"
title = "Kinetic Reverberation"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kinetic_reverberation", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (rubber tree sap)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Arcanist, Investigator, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (rubber tree sap)
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: creature touched
:::

**Sources:** Ultimate Combat pg 233

This spell converts the momentum and force from melee attacks made against the target of the spell,
reflecting them back upon the attacker's weapon. After making a successful melee attack against the
target, an attacker must make a Fortitude saving throw for the weapon used. If the weapon fails the
save, it takes damage equal to the damage rolled against the target. Creatures using natural attacks
or unarmed strikes are unaffected by this spell.
