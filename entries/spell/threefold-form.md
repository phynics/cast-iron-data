+++
id = "ref/spell/threefold-form"
kind = "spell"
title = "Threefold Form"
aon = "SpellDisplay.aspx?ItemName=Threefold%20Form"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "threefold_form", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bilocation" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "25"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Witch", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, F (a green, three-pointed knot made of mithral worth 729 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "9 rounds"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 9: Druid, Psychic, Witch
Casting time: 1 standard action
Components: V, S, F (a green, three-pointed knot made of mithral worth 729 gp)
Range: personal
Duration: 9 rounds
Saving throw: none
Spell resistance: no
Target: you
:::

### Threefold Form

You pull forth idealized versions of yourself at various ages from your mind, splitting into three
copies of yourself. Threefold form functions as [bilocation](ref/spell/bilocation), except there are
three of you instead of two, and each of the three bodies is under the effect of threefold aspect
with a different idealized age. Other than the differences from threefold aspect, each body shares
all other effects with you, as normal for bilocation.
