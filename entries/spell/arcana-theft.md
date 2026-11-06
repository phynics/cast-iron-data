+++
id = "ref/spell/arcana-theft"
kind = "spell"
title = "Arcana Theft"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcana_theft", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Magus", level = 4 },
  { class = "Psychic", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Magus\
5: Psychic
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: creature touched
:::

**Sources:** Ultimate Magic pg 206

This spell functions as a targeted [dispel magic](ref/spell/dispel-magic) spell, except it only
affects creatures and it requires a melee touch attack. If the melee touch attack is successful and
the spell successfully dispels one spell affecting the target, that spell is instead transferred to
you, treating you as the original target. You do not receive a new saving throw or
[spell resistance](ref/rule/spell-resistance) check against this spell and must accept its affects
even if they are not beneficial. This does not alter the spell's duration; for example, if the spell
only has 4 rounds of duration remaining when it is stolen, it only affects you for 4 rounds. If the
spell or effect has a duration of permanent, its duration continues for 1 hour per caster level of
the original caster, after which it ends. The stolen spell does not revert to the original target.
