+++
id = "ref/spell/bind-sage"
kind = "spell"
title = "Bind Sage"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bind_sage", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/planar-binding" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Calling"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one caulborn" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "no and yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard\
5: Occultist, Psychic, Shaman, Witch
Casting time: 10 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: no and yes; see text
Target: one caulborn
Subschool: Calling
:::

**Sources:** Magic Tactics Toolbox pg 17

This variant of planar binding is specifically used to call one of the most knowledgeable types of
outsiders: the immortal and prophetic caulborn. This spell calls a single caulborn into a specially
prepared trap. The caster of this spell can compel a bound caulborn only to provide information
(using its Knowledge skills or detect thoughts); attempts to compel the caulborn to fight, guard a
location, or perform some other task automatically fail.

This spell otherwise functions as [planar binding](ref/spell/planar-binding). The most effective
gifts for a caulborn are unique books or intelligent creatures upon whose thoughts the caulborn can
feed. The true names of caulborn are nearly impossible to discover, as they are not inherently
individualistic, but certain reclusive scholar communities in Kaer Maga may know titles by which
specific caulborn can be called.
