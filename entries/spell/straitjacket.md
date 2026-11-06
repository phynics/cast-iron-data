+++
id = "ref/spell/straitjacket"
kind = "spell"
title = "Straitjacket"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "straitjacket", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (leather strap)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Inquisitor, Occultist\
5: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (leather strap)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Target: one creature
Subschool: Creation
:::

**Sources:** Horror Adventures pg 128

You cause a straitjacket to spring into existence to restrain the target creature. You attempt a
combat maneuver against the target's CMD. Your CMB for this check is equal to your caster level + 5
due to the straightjacket's Strength. This combat maneuver doesn't provoke an attack of opportunity,
and if it succeeds, the target is restrained. This is similar to the grappled condition, except the
target is able to move at its normal speed, the restraint doesn't cause the target to require
concentration checks to use abilities that require concentration, and the target can't take actions
that require one or more hands or arms to perform (including casting spells that require a somatic
or material component).

Once it has been restrained for 1 round, the target can attempt an additional saving throw against a
magical effect that makes it confused, a curse, a fear effect, or a madness. The caster chooses
which effect the target gets an extra save against. This extra save applies to only effects with
durations of 10 minutes per level or less, and it doesn't apply to instantaneous effects. This extra
save occurs only once per casting of straitjacket.

A creature can attempt to escape the straitjacket with a combat maneuver check or Escape Artist
check, with a DC equal to 10 + your caster level + your Intelligence, Wisdom, or Charisma modifier,
whichever is highest.
