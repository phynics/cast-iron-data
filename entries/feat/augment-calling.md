+++
id = "ref/feat/augment-calling"
kind = "feat"
title = "Augment Calling"
aon = "FeatDisplay.aspx?ItemName=Augment%20Calling"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "augment_calling", path = "json/feat01.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/spell-focus", label = "or" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "13"

[fields]
kind = "feat"
prerequisites = "Spell Focus (conjuration); ability to cast lesser planar ally, lesser planar binding, or a higher-level version of these spells."
prerequisite_feats = ["ref/feat/spell-focus"]
benefit = "Choose a subtype of outsider, such as angel or elemental. When using the *planar ally* or *planar binding* spells, you can call 2 additional Hit Dice of outsiders with the chosen subtype. You also gain an additional benefit depending on what spell you are casting."
special = "You can gain this feat multiple times. Its effects do not stack. Each time you take the feat, it applies to a different subtype of outsider."
+++

Your attempts to bind or call outsiders are highly potent.\
**Prerequisites:** [Spell Focus](ref/feat/spell-focus) (conjuration); ability to cast
[lesser planar ally](ref/spell/planar-ally-lesser),
[lesser planar binding](ref/spell/planar-binding-lesser), or a higher-level version of these spells.\
**Benefit:** Choose a subtype of outsider, such as angel or elemental. When using the
_[planar ally](ref/spell/planar-ally)_ or _[planar binding](ref/spell/planar-binding)_ spells, you
can call 2 additional Hit Dice of outsiders with the chosen subtype. You also gain an additional
benefit depending on what spell you are casting.

When you call an outsider of the chosen subtype with _[planar ally](ref/spell/planar-ally)_ spells,
you reduce the price it demands for service by 25%, to a minimum of 1,000 gp.

When you bind an outsider of the chosen subtype with _[planar binding](ref/spell/planar-binding)_
spells and request a service of the outsider, you gain a +2 bonus on Charisma checks to do so.

**Special:** You can gain this feat multiple times. Its effects do not stack. Each time you take the
feat, it applies to a different subtype of outsider.
