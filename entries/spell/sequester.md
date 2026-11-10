+++
id = "ref/spell/sequester"
kind = "spell"
title = "Sequester"
aon = "SpellDisplay.aspx?ItemName=Sequester"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sequester", path = "json/spells15.json" },
]
[[sources]]
publication = "core-rulebook"
page = "340"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a basilisk eyelash and gum arabic)"
range = "touch"
effects = [
  { label = "Target", value = "one willing creature or object (up to a 2-ft. cube/level) touched" },
]
duration = "1 day/level (D)"
saving_throw = "none or Will negates (object)"
spell_resistance = "no or yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Summoner\
6: Unchained Summoner\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a basilisk eyelash and gum arabic)
Range: touch
Duration: 1 day/level (D)
Saving throw: none or Will negates (object)
Spell resistance: no or yes (object)
Target: one willing creature or object (up to a 2-ft. cube/level) touched
:::

When cast, this spell prevents divination spells from detecting or locating the target and also
renders the affected target invisible (as the [invisibility](ref/spell/invisibility) spell). The
spell does not prevent the subject from being discovered through tactile means or through the use of
devices. Creatures affected by sequester become comatose and are effectively in a state of suspended
animation until the spell ends.

_Note:_ The Will save prevents an attended or magical object from being sequestered. There is no
save to see the sequestered creature or object or to detect it with a divination spell.
