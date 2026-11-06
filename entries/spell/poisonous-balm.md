+++
id = "ref/spell/poisonous-balm"
kind = "spell"
title = "Poisonous Balm"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poisonous_balm", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["poison", "ruse"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous, then 1 hour or until triggered plus 6 rounds; see text"
saving_throw = "Will partial (harmless), then Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Cleric, Occultist, Oracle, Shaman\
5: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous, then 1 hour or until triggered plus 6 rounds; see text
Saving throw: Will partial (harmless), then Fortitude negates (see text)
Spell resistance: yes
Target: one creature
Subschool: Healing
Descriptors: poison, ruse
:::

**Sources:** Ultimate Intrigue pg 222

You mend the target's injuries, curing 3d8 hit points + 1 point per caster level (maximum +15) as
cure serious wounds, but leaving its body laced with a subtle toxin that remains inert until you
activate it. A target that decides to attempt the Will save and succeeds is healed for half (as cure
serious wounds) and negates the toxin. Otherwise, you can activate the toxin by concentrating on the
spell as a standard action, at which point the victim takes 1d3 points of Strength damage per round
for 6 rounds. Once the poison is active, the target can attempt a Fortitude save each round to
negate that round's damage and end the affliction. If you don't trigger the poison for 1 hour, the
spell ends and leaves the target unharmed.

Detect poison reveals an inert poisonous balm only if the caster succeeds at a caster level check
against a DC equal to 15 + your caster level. Attempts to identify poisonous balm with a skill check
incorrectly identify it as cure serious wounds. A fooled viewer mistakes poisonous balm's aura as
the lingering aura of an instantaneous effect.
