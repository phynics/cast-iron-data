+++
id = "ref/spell/accursed-glare"
kind = "spell"
title = "Accursed Glare"
aon = "SpellDisplay.aspx?ItemName=Accursed%20Glare"
source_ids = ["blood-of-the-moon"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "accursed_glare", path = "json/spells.json" },
]
[[sources]]
publication = "blood-of-the-moon"
page = "9"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

> _The following spell is common among [werebats](ref/template/lycanthrope), bloodmarked
> [skinwalkers](ref/race/skinwalker), and those who associate with them._

You channel a fell curse through your glare. If the target fails its saving throw, it begins to
obsessively secondguess its actions and attract bad luck. Whenever the target attempts an attack
roll or saving throw while the curse lasts, it must roll twice and take the lower result. While you
cast this spell, an ally within range of the subject can attempt an Intimidate check as a move
action (DC = save DC of this spell); on a success, the ally adds its own glare to yours, granting
you a +2 bonus on your caster level check to overcome [spell resistance](ref/rule/spell-resistance)
(if any). Multiple allies can attempt Intimidate checks; this bonus stacks.
