+++
id = "ref/spell/mark-of-spite"
kind = "spell"
title = "Mark of Spite"
aon = "SpellDisplay.aspx?ItemName=Mark%20of%20Spite"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mark_of_spite", path = "json/spells6.json" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "23"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of blood)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Mesmerist\
3: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of blood)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature
:::

Half-drow take substantial pains to ensure their enemies' defeat. You must succeed at a ranged touch
attack to place your mark on the victim. While the mark remains, you may injure yourself as a
standard action, dealing a number of points of damage equal to 1d8 plus your Strength modifier. The
recipient of the mark automatically takes twice the amount of damage that you deal to yourself,
bypassing any [damage reduction](ref/rule/damage-reduction), immunities, or resistances.
