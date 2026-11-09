+++
id = "ref/spell/augury"
kind = "spell"
title = "Augury"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "augury", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "245"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 minute"
components = "V, S, M (incense worth at least 25 gp), F (a set of marked sticks or bones worth at least 25 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Cleric, Medium, Occultist, Oracle, Psychic, Shaman, Spiritualist, Warpriest, Witch
Casting time: 1 minute
Components: V, S, M (incense worth at least 25 gp), F (a set of marked sticks or bones worth at least 25 gp)
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

An augury can tell you whether a particular action will bring good or bad results for you in the
immediate future.

The base chance for receiving a meaningful reply is 70% + 1% per caster level, to a maximum of 90%;
this roll is made secretly. A question may be so straightforward that a successful result is
automatic, or so vague as to have no chance of success. If the augury succeeds, you get one of four
results:

- Weal (if the action will probably bring good results).
- Woe (for bad results).
- Weal and woe (for both).
- Nothing (for actions that don't have especially good or bad results).

If the spell fails, you get the "nothing" result. A cleric who gets the "nothing" result has no way
to tell whether it was the consequence of a failed or successful augury.

The augury can see into the future only about half an hour, so anything that might happen after that
does not affect the result. Thus, the result might not take into account the long-term consequences
of a contemplated action. All auguries cast by the same person about the same topic use the same die
result as the first casting.
