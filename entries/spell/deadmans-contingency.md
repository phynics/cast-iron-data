+++
id = "ref/spell/deadmans-contingency"
kind = "spell"
title = "Deadman's Contingency"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deadmans_contingency", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/contingency" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "at least 10 minutes; see text"
components = "V, S, M (quicksilver and an eyelash of a spell-using creature), F (ivory statuette of you worth 1,500 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 day/level (d) or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Occultist, Psychic, Sorcerer, Wizard
Casting time: at least 10 minutes; see text
Components: V, S, M (quicksilver and an eyelash of a spell-using creature), F (ivory statuette of you worth 1,500 gp)
Range: personal
Duration: 1 day/level (d) or until discharged
Saving throw: none
Spell resistance: no
Target: you
:::

### Deadman's Contingency

**Sources:** Ultimate Intrigue pg 210

This spell functions as [contingency](ref/spell/contingency), except as noted above. This spell also
only comes into effect after your death and works only with certain spells. The companion spell
triggers 1d6 rounds after your death. All decisions made involving the companion spell must be made
when deadman's contingency is cast (including messages and recipients for spells like magic mouth or
sending). If the spell targets an object or appears in a certain location, it must target or be
centered on your corpse.

The following spells can be companion spells for deadman's contingency:
[animate dead](ref/spell/animate-dead) (animating your corpse as an uncontrolled skeleton or
zombie), [disintegrate](ref/spell/disintegrate), [fireball](ref/spell/fireball),
[gentle repose](ref/spell/gentle-repose), [magic mouth](ref/spell/magic-mouth),
[major image](ref/spell/major-image) (with a duration of 3 rounds),
[permanent image](ref/spell/permanent-image), [sending](ref/spell/sending),
[stinking cloud](ref/spell/stinking-cloud), and [teleport object](ref/spell/teleport-object).
