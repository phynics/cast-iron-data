+++
id = "ref/spell/akashic-form"
kind = "spell"
title = "Akashic Form"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "akashic_form", path = "json/spells.json" },
]
[[sources]]
publication = "occult-adventures"
page = "156"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Psychic", level = 9 },
]
casting_time = "1 hour"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Psychic
Casting time: 1 hour
Components: V, S
Range: personal
Duration: 24 hours
Saving throw: none
Spell resistance: no
Target: you
:::

You create a perfect record of your physical body in the [Akashic Record](ref/rule/akashic-record)
at the time the spell is cast. This record includes your current hit point total, physical ability
scores (Strength, Dexterity, and Constitution), and any conditional modifiers or conditions such as
ability damage to physical ability scores, disease, negative levels, and poison. If at any point
within the duration of the spell you are reduced to fewer than 0 hit points or are slain by a death
effect that is not mind-affecting, you can immediately let your current physical body die and assume
the record of your physical body on your next turn. When this happens, your corpse disappears, and
you can either resume the place of your dead body (already wearing any clothing still attached to
the corpse) or appear in any place you've been within 500 feet of where your corpse lies (but
without any of your gear).

You still retain your original mind, and therefore don't regain any spells. You are still under any
mental influences and energy drain effects you were under when you recalled the record of your
physical body, but don't retain any physical effects such as bleed damage or poison (unless you
suffered from these conditions at the time the spell was cast). Spells affecting you when you store
a record of yourself abide by their normal durations. For example, if you were affected by cat's
grace when you created the record and you restore your body 1 hour later, you won't be under that
effect anymore since its duration has already expired. This spell doesn't allow you to avoid dying
of old age. Casting this spell again replaces any previous version you cast; you can't store more
than one copy of yourself in the Akashic Record.
