+++
id = "ref/spell/interposing-hand"
kind = "spell"
title = "Interposing Hand"
aon = "SpellDisplay.aspx?ItemName=Interposing%20Hand"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "interposing_hand", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "301"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a soft glove)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft. hand" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Magus, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a soft glove)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: 10-ft. hand
Descriptors: force
:::

Interposing hand creates a Large magic hand that appears between you and one opponent. This
floating, disembodied hand then moves to remain between the two of you, regardless of where you move
or how the opponent tries to get around it, providing cover (+4 AC) for you against that opponent.
Nothing can fool the hand - it sticks with the selected opponent in spite of darkness, invisibility,
polymorphing, or any other attempt at hiding or disguise. The hand does not pursue an opponent,
however.

An interposing hand is 10 feet long and about that wide with its fingers outstretched. It has as
many hit points as you do when you're undamaged, and is AC 20 (-1 size, +11 natural). It takes
damage as a normal creature, but most magical effects that don't cause damage do not affect it.

The hand never provokes attacks of opportunity from opponents. It cannot push through a wall of
force or enter an antimagic field, but it suffers the full effect of a prismatic wall or prismatic
sphere. The hand makes saving throws as its caster.

[Disintegrate](ref/spell/disintegrate) or a successful [dispel magic](ref/spell/dispel-magic)
destroys it.

Any creature weighing 2,000 pounds or less that tries to push past the hand is slowed to half its
normal speed. The hand cannot reduce the speed of a creature weighing more than 2,000 pounds, but it
still affects the creature's attacks.

Directing the spell to a new target is a move action.
