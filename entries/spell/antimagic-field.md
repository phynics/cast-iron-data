+++
id = "ref/spell/antimagic-field"
kind = "spell"
title = "Antimagic Field"
aon = "SpellDisplay.aspx?ItemName=Antimagic%20Field"
source_ids = ["core-rulebook", "faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "antimagic_field", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "242"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 8 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (pinch of powdered iron or iron fillings)"
range = "10 ft."
effects = [
  { label = "Area", value = "10-ft.-radius emanation, centered on you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Arcanist, Occultist, Sorcerer, Wizard\
7: Psychic\
8: Cleric, Oracle
Casting time: 1 standard action
Components: V, S, M/DF (pinch of powdered iron or iron fillings)
Range: 10 ft.
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: see text
Area: 10-ft.-radius emanation, centered on you
:::

An invisible barrier surrounds you and moves with you. The space within this barrier is impervious
to most magical effects, including spells, [spell-like abilities](ref/umr/spell-like-abilities), and
supernatural abilities. Likewise, it prevents the functioning of any magic items or spells within
its confines.

An antimagic field suppresses any spell or magical effect used within, brought into, or cast into
the area, but does not dispel it. Time spent within an antimagic field counts against the suppressed
spell's duration.

Summoned creatures of any type wink out if they enter an antimagic field. They reappear in the same
spot once the field goes away. Time spent winked out counts normally against the duration of the
conjuration that is maintaining the creature. If you cast antimagic field in an area occupied by a
summoned creature that has [spell resistance](ref/rule/spell-resistance), you must make a caster
level check (1d20 + caster level) against the creature's spell resistance to make it wink out. (The
effects of instantaneous conjurations are not affected by an antimagic field because the conjuration
itself is no longer in effect, only its result.)

A normal creature can enter the area, as can normal missiles. Furthermore, while a magic sword does
not function magically within the area, it is still a sword (and a masterwork sword at that). The
spell has no effect on golems and other constructs that are imbued with magic during their creation
process and are thereafter self-supporting (unless they have been summoned, in which case they are
treated like any other summoned creatures). Elementals, corporeal undead, and outsiders are likewise
unaffected unless summoned. These creatures' spell-like or supernatural abilities may be temporarily
nullified by the field. [Dispel magic](ref/spell/dispel-magic) does not remove the field.

Two or more antimagic fields sharing any of the same space have no effect on each other. Certain
spells, such as wall of force, prismatic sphere, and prismatic wall, remain unaffected by antimagic
field. Artifacts and deities are unaffected by mortal magic such as this.

Should a creature be larger than the area enclosed by the barrier, any part of it that lies outside
the barrier is unaffected by the field.
