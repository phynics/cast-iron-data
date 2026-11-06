+++
id = "ref/spell/body-capacitance"
kind = "spell"
title = "Body Capacitance"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "body_capacitance", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["electricity"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (an iron coil)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level or until discharged (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Arcanist, Investigator, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (an iron coil)
Range: personal
Duration: 1 minute/level or until discharged (see text)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: electricity
:::

**Sources:** Advanced Class Guide pg 176

If you take electricity damage while this spell is active, some of the energy is stored on your
skin, as with holding the charge on a touch spell. You can release this stored electricity by making
a melee touch attack. You gain a +3 bonus on the attack roll if your opponent is wearing metal
armor, is carrying a metal weapon, or is made of metal. The target of your touch attack is dealt
electricity damage equal to half the amount of electricity damage you took after you cast this spell
(for example, if you saved for half damage against a lightning bolt and took only 15 points of
electricity damage, your next touch attack deals 7 points of electricity damage). This spell is
discharged once you hit with a melee touch attack to deliver its damage. If you take electricity
damage multiple times while this spell is active, use the largest amount of electricity damage you
took to determine your touch attack damage.
