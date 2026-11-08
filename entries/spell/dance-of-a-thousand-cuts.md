+++
id = "ref/spell/dance-of-a-thousand-cuts"
kind = "spell"
title = "Dance of a Thousand Cuts"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dance_of_a_thousand_cuts", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dance-of-a-hundred-cuts" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Bard, Skald
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

## Dance of a Hundred Cuts

**Sources:** Ultimate Magic pg 215

You become a lethal combat dancer, swirling and spinning with grace and precision. You gain a morale
bonus on melee attack rolls, melee damage rolls, and Acrobatics checks, and to Armor Class. This
bonus is equal to +1 per 3 caster levels (maximum +5 at 15th level). The bonus to AC is lost under
any circumstances that would cause you to lose your Dexterity bonus to AC. You must remain moving
for the spell to stay in effect. If in any round you do not either move at least 10 feet or make a
melee attack, the spell's duration ends.

### Dance of a Thousand Cuts

**Sources:** Ultimate Magic pg 216

This spell functions as [dance of a hundred cuts](ref/spell/dance-of-a-hundred-cuts), except you
also gain the benefits of haste.
