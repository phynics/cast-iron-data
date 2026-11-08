+++
id = "ref/spell/magic-fang-greater"
kind = "spell"
title = "Greater Magic Fang"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_fang_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-fang" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter, Ranger, Spiritualist, Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

## Magic Fang

**Sources:** PRPG Core Rulebook pg 308

Magic fang gives one natural weapon or unarmed strike of the subject a +1 enhancement bonus on
attack and damage rolls. The spell can affect a slam attack, fist, bite, or other natural weapon.
The spell does not change an unarmed strike's damage from nonlethal damage to lethal damage.

Magic fang can be made permanent with a [permanency](ref/spell/permanency) spell.

### Mythic Magic Fang

**Sources:** Mythic Adventures pg 100

The spell affects an additional number of the target's natural weapons equal to your tier. For
example, if you're 3rd tier, it could affect two claws and one bite).

### Greater Magic Fang

**Sources:** PRPG Core Rulebook pg 309

This spell functions like [magic fang](ref/spell/magic-fang), except that the enhancement bonus on
attack and damage rolls is +1 per four caster levels (maximum +5). This bonus does not allow a
natural weapon or unarmed strike to bypass [damage reduction](ref/rule/damage-reduction) aside from
magic.

Alternatively, you may imbue all of the creature's natural weapons with a +1 enhancement bonus
(regardless of your caster level).

Greater magic fang can be made permanent with a [permanency](ref/spell/permanency) spell.

### Greater Mythic Magic Fang

**Sources:** Mythic Adventures pg 100

This functions like mythic magic fang. You can add one of the following weapon special abilities to
natural attacks or unarmed strikes affected by the spell: [flaming](ref/magic-enh/flaming),
[frost](ref/magic-enh/frost), [keen](ref/magic-enh/keen), [merciful](ref/magic-enh/merciful),
[shock](ref/magic-enh/shock), or [thundering](ref/magic-enh/thundering). You must choose only one
with each casting of the spell. For example, you can't add flaming to a tiger's bite and keen to its
claws with the same casting. If the target has an Intelligence score less than 3, these abilities
are always on (the target can't activate or deactivate the effect) and it might react with fear if
its attacks make noise or create visible energy.

_Augmented (5th):_ If you expend two uses of mythic power, you can reduce the granted enhancement
bonuses by 1 to add two of the above abilities or one of the following abilities:
[flaming burst](ref/magic-enh/flaming-burst), [icy burst](ref/magic-enh/icy-burst), or
[shocking burst](ref/magic-enh/shocking-burst).
