+++
id = "ref/carried/bestiary/rules/universal-monster-rules/regeneration"
kind = "rule"
title = "Regeneration"
source_ids = ["bestiary"]
section = ["Rules", "Universal Monster Rules"]
parent = "ref/carried/bestiary/rules/universal-monster-rules"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Rules/Universal Monster Rules/Regeneration", path = "bestiary/rules/universal_monster_rules.json" },
]

[fields]
kind = "none"
+++

::: statblock
Ability Type: Extraordinary
:::

A creature with this ability is difficult to kill. Creatures with regeneration heal damage at a
fixed rate, as with [fast healing](ref/umr/fast-healing), but they cannot die as long as their
regeneration is still functioning (although creatures with regeneration still fall unconscious when
their hit points are below 0). Certain attack forms, typically fire and acid, cause a creature's
regeneration to stop functioning on the round following the attack. During this round, the creature
does not heal any damage and can die normally. The creature's descriptive text describes the types
of damage that cause the regeneration to cease functioning.

Attack forms that don't deal hit point damage are not healed by regeneration. Regeneration also does
not restore hit points lost from starvation, thirst, or suffocation. Regenerating creatures can
regrow lost portions of their bodies and can reattach severed limbs or body parts if they are
brought together within 1 hour of severing. Severed parts that are not reattached wither and die
normally.

A creature must have a Constitution score to have the regeneration ability.

## Format {#format}

regeneration 5 (fire, acid); _Location_: hp.
