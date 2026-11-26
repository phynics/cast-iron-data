+++
id = "ref/arc-familiar/soulbound-familiar"
kind = "archetype"
title = "Soulbound Familiar"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soulbound_familiar", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "213"

[fields]
kind = "archetype"
features = [
  { anchor = "soul-focus" },
  { anchor = "alignment-variation" },
]
trades = [
  { replaces = "Alertness", by = ["soul-focus"] },
  { replaces = "Speak with animals of its kind", by = ["alignment-variation"] },
  { replaces = "scry on familiar", by = ["alignment-variation"] },
]
+++

Soulbound familiars are born when a master uses the magical principles behind soulbound dolls to
bind a soul fragment to an animal.

## Soul Focus (Ex) {#soul-focus}

The soul fragment bound to the familiar lives within a focus crystal surgically inserted into the
animal. As long as this soul focus remains intact, it can be used to bind the soul fragment into
another familiar, with the same cost and time requirements as replacing a familiar. Once bound into
the soul focus, the soul continues to learn, and so if it is later put into a new familiar body, the
soul retains its personality and memories from its previous body or bodies. A soul focus has
[hardness](ref/umr/hardness) 8, 12 hit points, and a break DC of 20, though it can be attacked only
when surgically removed from the familiar. If the soul focus is destroyed, creating a new soul focus
with none of the old one's memories costs as much as replacing a familiar, in addition to the normal
cost of replacing the familiar itself. Because it is born of another creature's soul, a soulbound
familiar can never serve as a witch's familiar, a shaman's spirit animal, or any other
spell-granting familiar. The soulbound familiar gains [Skill Focus](ref/feat/skill-focus) in a skill
important to the creature whose soul provided the fragment.

This replaces alertness.

## Alignment Variation (Ex) {#alignment-variation}

A soulbound familiar's alignment is always at least partially neutral, although it can also be
chaotic, evil, good, or lawful, depending on the creature whose soul provided the fragment rather
than on the master's alignment (unless the master donates a fragment of her own soul). At 8th level,
it gains one of the following [spell-like abilities](ref/umr/spell-like-abilities), usable once per
day and based on its alignment (caster level = its master's caster level - 3): chaotic neutral:
_[rage](ref/spell/rage)_; lawful neutral: _[suggestion](ref/spell/suggestion)_; neutral:
_[deep slumber](ref/spell/deep-slumber)_; neutral evil:
_[inflict serious wounds](ref/spell/inflict-serious-wounds)_; or neutral good:
_[heroism](ref/spell/heroism)_. At 13th level, its caster level increases to its master's caster
level.

This replaces speak with animals of its kind and scry on familiar.
