+++
id = "ref/arc-warpriest/libertys-blade"
kind = "archetype"
title = "Liberty's Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Liberty%27s%20Blade"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "libertys_blade", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-origins"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "freedom-s-focus", level = 1 },
  { anchor = "devilslayer", level = 4 },
  { anchor = "channel-liberty", level = 4 },
  { anchor = "shield-against-hellspawn", level = 7 },
]
trades = [
  { alters = "Blessings", feature = "blessings", by = ["freedom-s-focus"] },
  { alters = "Sacred weapon", feature = "sacred-weapon", by = ["devilslayer"] },
  { alters = "Channel energy", feature = "channel-energy", by = ["channel-liberty"] },
  { alters = "Sacred armor", feature = "sacred-armor", by = ["shield-against-hellspawn"] },
]
+++

There are some who find in the call to freedom something primal and spiritual, even more so than
other Andorens. These liberty's blades become warpriests of deities who spread freedom, and they
head to lives of adventure as [Eagle Knights](ref/rule/aff-vangard) or adventurers, championing
liberty wherever they go.

## Freedom's Focus (Su) {#freedom-s-focus}

A liberty's blade must worship a good deity who grants the [Liberation](ref/blessing/liberation)
blessing, and he must select the Liberation blessing. He does not gain a second blessing. This
ability alters blessings.

## Devilslayer (Su) {#devilslayer}

At 4th level, a liberty's blade adds _[devil-bane](ref/magic-enh/bane)_ to the list of enhancements
he can add to his sacred weapon. This ability alters sacred weapon.

## Channel Liberty (Su) {#channel-liberty}

At 4th level, when a liberty's blade channels energy to heal, the effects of his healing is halved,
but all creatures affected by his healing instantly benefit as if from a
_[liberating command](ref/spell/liberating-command)_ spell at the liberty's blade's caster level.
When channeling to harm, the liberty's blade harms devils as if using
[Alignment Channel](ref/feat/alignment-channel) instead of harming undead, and she deals double the
normal amount of damage. This ability alters channel energy.

## Shield Against Hellspawn (Su) {#shield-against-hellspawn}

At 7th level, a liberty's blade adds _[devil-defiant](ref/magic-enh/defiant)_ to the list of
enhancements that he can add to his sacred armor. This ability alters sacred armor.
