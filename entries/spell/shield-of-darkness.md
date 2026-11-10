+++
id = "ref/spell/shield-of-darkness"
kind = "spell"
title = "Shield of Darkness"
aon = "SpellDisplay.aspx?ItemName=Shield%20of%20Darkness"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_darkness", path = "json/spells9.json" },
]
[[sources]]
publication = "blood-of-shadows"
page = "29"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness", "shadow"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Antipaladin, Cleric, Inquisitor, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: darkness, shadow
:::

You shield yourself with darkness, reducing the illumination level in your space to magical darkness
and granting you [total concealment](ref/rule/concealment). Your opponents are automatically aware
of which squares you occupy, preventing you from attempting Stealth checks using this concealment
unless every square adjacent to you has an illumination level of darkness or lower. Shield of
darkness does not hinder your vision, and creatures that can see in magical darkness ignore this
effect.
