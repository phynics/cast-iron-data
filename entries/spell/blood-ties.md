+++
id = "ref/spell/blood-ties"
kind = "spell"
title = "Blood Ties"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_ties", path = "json/spells2.json" },
]
[[sources]]
publication = "horror-adventures"
page = "110"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a small length of crimson string)"
range = "unlimited (see text)"
effects = [
  { label = "Target", value = "two living creatures" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin\
5: Cleric, Druid, Hunter, Inquisitor, Oracle, Psychic, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, F (a small length of crimson string)
Range: unlimited (see text)
Duration: 1 day/level (D)
Saving throw: Will negates (see text)
Spell resistance: no
Target: two living creatures
Descriptors: evil
:::

One of the targets of this spell must be a hostage - a bound, pinned, or helpless creature within
your reach (though the spell doesn't end if the hostage later moves beyond your reach). The second
target must be a member of the first target's family. If neither creature successfully saves against
the spell, the second target also takes any damage conferred to the hostage, provided both are still
alive, to a maximum of 10 points of damage per caster level per day (damage beyond that necessary to
kill the first target does not transfer). This transferred damage is typeless and ignores the second
creature's [damage reduction](ref/rule/damage-reduction) and resistances. If either target succeeds
at the saving throw, you can never attempt to exploit the connection between these particular two
creatures again. The connection between your targets weakens when the two are less familiar with one
another. Each target gains a +2 bonus on its save if the two are distant relations or related by
marriage. Each target takes a -2 penalty on its save if the two targets are parent and child or
siblings.
