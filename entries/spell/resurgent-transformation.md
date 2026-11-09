+++
id = "ref/spell/resurgent-transformation"
kind = "spell"
title = "Resurgent Transformation"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resurgent_transformation", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "239"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Investigator", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of meteoric iron worth 100 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level or until triggered, then 1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Alchemist, Investigator
Casting time: 1 standard action
Components: V, S, M (a pinch of meteoric iron worth 100 gp)
Range: personal
Duration: 1 hour/level or until triggered, then 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
:::

Resurgent transformation grants you the ability to recover from deadly wounds with restored vitality
and a will to fight, but at a price. Once cast, resurgent transformation lies dormant for up to 1
hour per level until you are reduced to one-quarter hit points or less. Once triggered, you
immediately gain a +4 enhancement bonus to Constitution and Strength,
[damage reduction](ref/rule/damage-reduction) 5/-, and the benefits of a haste spell. In addition,
you heal 4d8 points of damage + 1 point per caster level (maximum +25). Resurgent transformation can
even save you from death by healing the damage from an otherwise mortal wound, though it does not
prevent death from massive damage or from causes other than hit point loss. Your mental faculties
are impaired by this magical transformation, however, causing 1d4 points of Intelligence and Wisdom
damage.

The advantages from your transformation persist for 1 round per caster level after the spell is
triggered. Once the spell ends, it takes a heavy toll, leaving you exhausted and inflicting 1d4
points of Constitution damage. Utilizing more than one resurgent transformation in a day is
particularly risky. The expiration of a second resurgent transformation in a 24-hour period inflicts
an additional 1d4 points of Constitution damage and results in death from system shock unless you
succeed at a DC 15 Fortitude save, made after the Constitution damage has been applied.

If the spell expires or is dispelled before the transformation has been triggered, no adverse
effects result.
