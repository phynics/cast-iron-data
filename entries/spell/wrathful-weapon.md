+++
id = "ref/spell/wrathful-weapon"
kind = "spell"
title = "Wrathful Weapon"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wrathful_weapon", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "transmutation [see text]"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "melee weapon touched (see text)" },
]
duration = "1 minute/level"
saving_throw = "Will (harmless, object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation \[see text\]
Level: 4: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will (harmless, object)
Spell resistance: yes (object)
Target: melee weapon touched (see text)
:::

**Sources:** Advanced Class Origins pg 31

You grant the targeted weapon one of the following weapon special abilities:
[anarchic](ref/magic-enh/anarchic), [axiomatic](ref/magic-enh/axiomatic),
[holy](ref/magic-enh/holy), or [unholy](ref/magic-enh/unholy). If anarchic, this spell has the chaos
descriptor; if axiomatic, the law descriptor; if holy, the good descriptor; and if unholy, the evil
descriptor. If the caster attempts to place a special ability on a weapon that already has that
special ability, the spell fails.

If a warpriest casts this spell on his sacred weapon, the duration doubles. Warpriests with unarmed
strike as a sacred weapon can cast this spell on their unarmed strike.
