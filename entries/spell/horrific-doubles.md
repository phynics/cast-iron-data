+++
id = "ref/spell/horrific-doubles"
kind = "spell"
title = "Horrific Doubles"
aon = "SpellDisplay.aspx?ItemName=Horrific%20Doubles"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "horrific_doubles", path = "json/spells5.json" },
]
[[sources]]
publication = "horror-adventures"
page = "120"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium, Mesmerist, Psychic\
4: Arcanist, Bloodrager, Bard, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Figment
:::

You create several illusory doubles of yourself, where you and each image all seem slightly off or
wrong in appearance. Treat this spell as mirror image, except as noted.

Each creature that can see the doubles must succeed at a Will save or become shaken for as long as
it can see any of the doubles. A successful saving throw negates the shaken condition and renders
the creature immune to the further effects of this spell (beyond the usual effects of mirror image).
In addition, the first time a creature that failed its initial saving throw destroys one of the
images, it must succeed at a Will save or its perception of the double shifts at the last second.
The double takes on the face of the attacker, the face of a loved one, or some other equally
disturbing image, causing the attacker to become frightened for 1 round and take 1d3 points of
Wisdom damage from the traumatic shock. Both additional effects are mind-affecting fear effects, and
[spell resistance](ref/rule/spell-resistance) applies against them.

If your campaign uses [the sanity system](ref/rule/sanity), a creature takes 1d8 points of sanity
damage instead of Wisdom damage.
