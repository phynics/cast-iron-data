+++
id = "ref/spell/calcific-touch"
kind = "spell"
title = "Calcific Touch"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calcific_touch", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "208"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or creatures touched (up to one per level)" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Bloodrager, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Fortitude partial
Spell resistance: yes
Target: creature or creatures touched (up to one per level)
Descriptors: earth
:::

Your touch progressively transmutes the substance of creatures you touch into stone. Once per round,
you may deliver a touch attack that inflicts 1d4 points of Dexterity damage and
[slows](ref/spell/slow) the target (as the spell) for 1 round. A successful Fortitude save negates
the slow effect but not the ability damage. A target reduced to 0 Dexterity is petrified
permanently. [Break enchantment](ref/spell/break-enchantment), [restoration](ref/spell/restoration),
or [stone to flesh](ref/spell/stone-to-flesh) can reverse the effects of calcific touch.
