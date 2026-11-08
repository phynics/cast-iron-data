+++
id = "ref/spell/animate-plants"
kind = "spell"
title = "Animate Plants"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animate_plants", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 7 },
  { class = "Shaman", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one Large plant per three caster levels or all plants within range; see text" },
]
duration = "1 round/level or 1 hour/level; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Druid, Shaman
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or 1 hour/level; see text
Saving throw: none
Spell resistance: no
Targets: one Large plant per three caster levels or all plants within range; see text
:::

**Sources:** PRPG Core Rulebook pg 242

You imbue inanimate plants with mobility and a semblance of life. Each animated plant then
immediately attacks whomever or whatever you initially designate as though it were an animated
object of the appropriate size category. You may animate one Large or smaller plant, or a number of
larger plants as follows: a Huge plant counts as two Large or smaller plants, a Gargantuan plant as
four, and a Colossal plant as eight. You can change the designated target or targets as a move
action, as if directing an active spell.

Use the statistics for animated objects, except that plants smaller than Large don't have
[hardness](ref/umr/hardness).

Animate plants cannot affect plant creatures, nor does it affect nonliving vegetable material.

_Entangle:_ Alternatively, you may imbue all plants within range with a degree of mobility, which
allows them to entwine around creatures in the area. This usage of the spell duplicates the effect
of an entangle spell. [Spell resistance](ref/rule/spell-resistance) does not keep creatures from
being entangled. This effect lasts 1 hour per caster level.
