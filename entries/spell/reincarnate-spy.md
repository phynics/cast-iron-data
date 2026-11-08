+++
id = "ref/spell/reincarnate-spy"
kind = "spell"
title = "Reincarnate Spy"
source_ids = ["core-rulebook", "inner-sea-races", "arcane-anthology", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reincarnate_spy", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/reincarnate" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (oils worth 1,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter, Medium, Shaman\
5: Witch
Casting time: 10 minutes
Components: V, S, DF, M (oils worth 1,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
:::

### Reincarnate Spy

**Sources:** Ultimate Intrigue pg 223

This spell functions as [reincarnate](ref/spell/reincarnate) except that you can cause the new body
to resemble a particular creature, matching its age category and sex and rerolling any race result
that would be the wrong size category. The subject further gains a +5 bonus on Disguise checks to
impersonate the chosen creature due to similar features, although it might take a penalty for being
the wrong race.

The spell automatically leaves you with a small piece of the creature's new body, typically a lock
of hair (useful for scrying and other such spells).
