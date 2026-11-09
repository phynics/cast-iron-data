+++
id = "ref/spell/enervation"
kind = "spell"
title = "Enervation"
aon = "SpellDisplay.aspx?ItemName=Enervation"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enervation", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "277"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray of negative energy" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Bloodrager, Mesmerist, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Effect: ray of negative energy
:::

You point your finger and fire a black ray of negative energy that suppresses the life force of any
living creature it strikes. You must make a ranged touch attack to hit. If you hit, the subject
gains 1d4 temporary [negative levels](ref/rule/energy-drain-and-negative-levels). Negative levels
stack.

Assuming the subject survives, it regains lost levels after a number of hours equal to your caster
level (maximum 15 hours). Usually, negative levels have a chance of becoming permanent, but the
negative levels from enervation don't last long enough to do so.

An undead creature struck by the ray gains 1d4 × 5 temporary hit points for 1 hour.
