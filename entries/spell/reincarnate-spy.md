+++
id = "ref/spell/reincarnate-spy"
kind = "spell"
title = "Reincarnate Spy"
aon = "SpellDisplay.aspx?ItemName=Reincarnate%20Spy"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reincarnate_spy", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/reincarnate" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "223"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Witch", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (oils worth 2,500 gp and a possession or piece of the body of the creature to resemble)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Druid, Hunter, Shaman\
7: Witch
Casting time: 10 minutes
Components: V, S, DF, M (oils worth 2,500 gp and a possession or piece of the body of the creature to resemble)
Range: touch
Duration: instantaneous
Saving throw: none (see text)
Spell resistance: yes
Target: dead creature touched
Subschool: healing
:::

### Reincarnate Spy

This spell functions as [reincarnate](ref/spell/reincarnate) except that you can cause the new body
to resemble a particular creature, matching its age category and sex and rerolling any race result
that would be the wrong size category. The subject further gains a +5 bonus on Disguise checks to
impersonate the chosen creature due to similar features, although it might take a penalty for being
the wrong race.

The spell automatically leaves you with a small piece of the creature's new body, typically a lock
of hair (useful for scrying and other such spells).
