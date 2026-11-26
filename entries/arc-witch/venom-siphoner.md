+++
id = "ref/arc-witch/venom-siphoner"
kind = "archetype"
title = "Venom Siphoner"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Venom%20Siphoner"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "venom_siphoner", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "potions-and-poisons"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "poisonous-familiar", level = 1 },
  { anchor = "venom-expert", level = 2 },
  { anchor = "toxic-blood", level = 6 },
]
trades = [
  { replaces = "Hex gained at 1st level", feature = "hex", levels = [1], by = ["poisonous-familiar"] },
  { replaces = "the familiar's alertness special ability", by = ["poisonous-familiar"] },
  { replaces = "Hex gained at 2nd level", feature = "hex", levels = [2], by = ["venom-expert"] },
  { replaces = "Hex gained at 6th level", feature = "hex", levels = [6], by = ["toxic-blood"] },
]
+++

Witches are no strangers to [poisons](ref/rule/poisons), using them alongside their various brews,
curses, spells, and other tools of the trade. A number of witches are masters of poison, receiving
toxic gifts that allow them and their familiars to use poison in unparalleled manners.

## Poisonous Familiar (Ex) {#poisonous-familiar}

The venom siphoner chooses either her familiar's bite attack or its claw attacks; once chosen, this
selection can't be changed. The chosen natural attack gains the following poison ability: _Siphoner
Poison:_ Natural attack—injury; _save_ Fort DC 10 + half the witch's level + the witch's
Intelligence modifier; _frequency_ 1/round for 6 rounds; effect 1d2 Dex; _cure_ 1 save.

Familiars without an appropriate natural attack instead gain the ability to spit the poison as a
ranged touch attack. This spit attack deals no damage, but it exposes the struck creature to the
poison, forcing it to attempt a saving throw to resist the poison as normal. If the familiar already
has a poison, the witch can instead empower its poison. An empowered poison's frequency increases by
50%. If the witch ever replaces her familiar, she must choose how this ability applies to her new
familiar as soon as she receives it.

This replaces the hex gained at 1st level and the familiar's alertness special ability.

## Venom Expert (Ex) {#venom-expert}

At 2nd level, a venom siphoner does not risk exposure to her familiar's poison when attempting to
[milk venom](ref/rule/harvesting-poisons) from it (see page 142 of _Pathfinder RPG Ultimate
Wilderness_).

This replaces the hex gained at 2nd level.

## Toxic Blood (Ex) {#toxic-blood}

At 6th level, the venom siphoner's blood becomes toxic, empowering her abilities. Any creature that
deals [bleed](ref/rule/bleed) damage to her with a natural, light, or one-handed weapon is
automatically exposed to the same poison granted to her familiar and must succeed at the save or be
affected by the poison. Additionally, when casting spells that have a single target and require a
Fortitude save, she can cause the spell to deliver this poison as a free action; a target who
succeeds at the save against the spell also avoids being affected by the poison. She can cause
spells to deliver poison in this way a number of times per day equal to 3 + her Intelligence
modifier. This ability refreshes when the venom siphoner communes with her familiar to prepare her
daily spells.

This replaces the hex gained at 6th level.
