+++
id = "ref/spell/mark-of-blood"
kind = "spell"
title = "Mark of Blood"
source_ids = ["adventurers-guide", "faction-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mark_of_blood", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of your blood)"
range = "touch"
effects = [
  { label = "Target", value = "one weapon touched" },
]
duration = "1 minute and permanent (see text)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bloodrager, Inquisitor, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of your blood)
Range: touch
Duration: 1 minute and permanent (see text)
Saving throw: Will negates
Spell resistance: yes
Target: one weapon touched
Descriptors: curse
:::

**Sources:** Adventurer's Guide pg 160, Faction Guide pg 61

You place a drop of your blood on a weapon and charge it with magic so that you transfer a small
amount of your life essence to the next living creature you strike with the weapon. Thereafter, you
can spend a move action to know the direction and general distance of that creature. The target can
negate this effect with a successful Will save. You must strike a creature within 1 minute of
casting this spell or the magic is wasted, but once the mark of blood takes effect it is permanent
until dispelled or removed via an effect like [remove curse](ref/spell/remove-curse).
