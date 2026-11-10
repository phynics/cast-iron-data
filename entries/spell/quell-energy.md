+++
id = "ref/spell/quell-energy"
kind = "spell"
title = "Quell Energy"
aon = "SpellDisplay.aspx?ItemName=Quell%20Energy"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "quell_energy", path = "json/spells8.json" },
]
[[sources]]
publication = "occult-origins"
page = "29"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Druid, Hunter, Inquisitor, Occultist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial
Spell resistance: yes
Target: one creature
:::

You reduce the target creature's ability to tap into a single energy type (acid, cold, electricity,
fire, or sonic) of your choice. This reduces damage of the selected type the creature deals with
spells, [spell-like abilities](ref/umr/spell-like-abilities), and supernatural abilities by 10
points. Multiple castings of this spell stack. Damage from sources other than the creature, such as
objects and magic items, is not reduced. If the damage of one of the creature's effects is negated
entirely, any additional effects associated with that damage (such being stunned by sound burst or
set on fire by a fire elemental) are also negated. At 13th level, you reduce the target's damage by
20 points, and at 19th level, you reduce the target's damage by 30 points.

If the target succeeds on its saving throw, the spell's duration is reduced to 1 round.
