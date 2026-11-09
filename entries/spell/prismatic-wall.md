+++
id = "ref/spell/prismatic-wall"
kind = "spell"
title = "Prismatic Wall"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prismatic_wall", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "325"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "wall 4 ft./level wide, 2 ft./level high" },
]
duration = "10 minutes/level (D)"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: see text
Spell resistance: see text
Effect: wall 4 ft./level wide, 2 ft./level high
:::

Prismatic wall creates a vertical, opaque wall - a shimmering, multicolored plane of light that
protects you from all forms of attack. The wall flashes with seven colors, each of which has a
distinct power and purpose. The wall is immobile, and you can pass through and remain near the wall
without harm. Any other creature with less than 8 HD that is within 20 feet of the wall is blinded
by the colors for 2d4 rounds if it looks at the wall.

The wall's maximum proportions are 4 feet wide per caster level and 2 feet high per caster level. A
prismatic wall spell cast to materialize in a space occupied by a creature is disrupted, and the
spell is wasted.

Each color in the wall has a special effect. The accompanying table shows the seven colors of the
wall, the order in which they appear, their effects on creatures trying to attack you or pass
through the wall, and the magic needed to negate each color.

The wall can be destroyed, color by color, in consecutive order, by casting the specified spells on
the wall; however, the first color must be brought down before the second can be affected, and so
on. A [rod of cancellation](ref/magic-rod/rod-of-cancellation) or a
[mage's disjunction](ref/spell/mages-disjunction) spell destroys a prismatic wall, but an
[antimagic field](ref/spell/antimagic-field) fails to penetrate it.
[Dispel magic](ref/spell/dispel-magic) and [greater dispel magic](ref/spell/dispel-magic-greater)
can only be used on the wall once all the other colors have been destroyed.
[Spell resistance](ref/rule/spell-resistance) is effective against a prismatic wall, but the caster
level check must be repeated for each color present.

Prismatic wall can be made permanent with a [permanency](ref/spell/permanency) spell.

|Order|Color|Effect of Color|Negated By|
| --- | --- | --- | --- |
|1st|Red|Stops nonmagical ranged weapons. Deals 20 points of fire damage (Reflex half).|[Cone of cold](ref/spell/cone-of-cold)|
|2nd|Orange|Stops magical ranged weapons. Deals 40 points of acid damage (Reflex half).|[Gust of wind](ref/spell/gust-of-wind)|
|3rd|Yellow|Stops poisons, gases, and petrification. Deals 80 points of electricity damage (Reflex half).|[Disintegrate](ref/spell/disintegrate)|
|4th|Green|Stops breath weapons. _Poison: (*frequency:* 1/rd for 6 rd.; *init. effect:* death, *sec. effect:* 1 Con/rd.; *cure* 2 consecutive Fort saves)._|[Passwall](ref/spell/passwall)|
|5th|Blue|Stops divination and mental attacks. Turned to stone (Fortitude negates).|[Magic missile](ref/spell/magic-missile)|
|6th|Indigo|Stops all spells. Will save or become insane (as insanity spell).|[Daylight](ref/spell/daylight)|
|7th|Violet|Energy field destroys all objects and effects.^[1](ref/spell/prismatic-wall#footnote-v)^ Creatures sent to another plane (Will negates).|[Dispel magic](ref/spell/dispel-magic) or [greater dispel magic](ref/spell/dispel-magic-greater)|

###### ^1^ {#footnote-v}

The violet effect makes the special effects of the other six colors redundant, but these six effects
are included here because certain magic items can create prismatic effects one color at a time, and
[spell resistance](ref/rule/spell-resistance) might render some colors ineffective (see above).
