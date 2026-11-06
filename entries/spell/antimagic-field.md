+++
id = "ref/spell/antimagic-field"
kind = "spell"
title = "Antimagic Field"
source_ids = ["core-rulebook", "mythic-adventures", "faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "antimagic_field", path = "json/spells.json" },
]

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

**Sources:** PRPG Core Rulebook pg 242

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

### Mythic Antimagic Field

**Sources:** Mythic Adventures pg 84

Select a number of spell schools equal to half your tier. Spells and effects of the chosen schools
are unaffected by the antimagic field.

### Source Severance

**Sources:** Faiths and Philosophies pg 29

You create an invisible barrier that surrounds you and moves with you, inhibiting one category of
magic. When you cast this spell, choose either arcane or divine magic. This spell functions like
antimagic field, but it suppresses only spells of the chosen type and supernatural and spell-like
class abilities from classes that grant spellcasting of the selected type. Magic items, other
[spell-like abilities](ref/umr/spell-like-abilities), and other supernatural abilities are
unaffected.

While this spell is in effect, you must succeed at a [concentration](ref/rule/concentration) check
(DC 20 + twice the spell level) to cast any spell, whether arcane or divine. If you fail at the
check, you lose the spell as if you had cast it to no effect.
