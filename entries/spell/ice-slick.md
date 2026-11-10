+++
id = "ref/spell/ice-slick"
kind = "spell"
title = "Ice Slick"
aon = "SpellDisplay.aspx?ItemName=Ice%20Slick"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ice_slick", path = "json/spells5.json" },
]
[[sources]]
publication = "monster-codex"
page = "69"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "5-ft.-radius burst" },
]
duration = "instantaneous (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Druid, Hunter, Magus, Ranger, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous (see text)
Saving throw: none
Spell resistance: no
Area: 5-ft.-radius burst
Descriptors: cold
:::

You create a blast of intense cold, coating all solid surfaces in the area with a thin coating of
ice. Any creature in the area when the spell is cast takes 1d6 points of cold damage + 1 point per
caster level (maximum +10) and falls prone; creatures that succeed at a Reflex save take half damage
and don't fall prone. [Spell resistance](ref/rule/spell-resistance) applies to this initial effect.

A creature can walk within or through the area of ice at half its normal speed with a successful DC
10 Acrobatics check. Failure by 4 or less means the creature can't move that round (and must succeed
at a Reflex save or fall); failure by 5 or more means it falls (see the
[Acrobatics skill](ref/skill/acrobatics) for details). Creatures that do not move on their turn do
not need to attempt this check.

A 5-foot square of ice has [hardness](ref/umr/hardness) 0 and 3 hit points. The ice is an
instantaneous effect, but persists as nonmagical ice. Under temperate conditions, the ice lasts 1
minute per level. In tropical environments, it might last only half as long. In cold environments
where ice and snow persist without melting, it could last indefinitely.
