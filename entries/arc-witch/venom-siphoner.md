+++
id = "ref/arc-witch/venom-siphoner"
kind = "archetype"
title = "Venom Siphoner"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "venom_siphoner", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]

[fields]
kind = "archetype"
replaces = ["1st-level hex", "the familiar's alertness special ability", "2nd-level hex", "6th-level hex"]
+++

**Sources:** Potions and Poisons pg 10\
Witches are no strangers to [poisons](ref/rule/poisons), using them alongside their various brews,
curses, spells, and other tools of the trade. A number of witches are masters of poison, receiving
toxic gifts that allow them and their familiars to use poison in unparalleled manners.

**Poisonous Familiar (Ex)**

**Action:** Ability

**Choice:** The venom siphoner chooses either her familiar's bite attack or its claw attacks; once
chosen, this selection can't be changed.

**Replaces:** 1st-level hex, the familiar's alertness special ability

**Special:** If the witch ever replaces her familiar, she must choose how this ability applies to
her new familiar as soon as she receives it.

The chosen natural attack gains the poison ability below. Familiars without an appropriate natural
attack instead gain the ability to spit the poison as a ranged touch attack. This spit attack deals
no damage, but it exposes the struck creature to the poison, forcing it to attempt a saving throw to
resist the poison as normal.

**Siphoner Poison**

**Type:** Poison (Natural attack or ranged touch attack-injury)

**Save:** Fortitude 10 + 1/2 the witch's level + her Int modifier

**Frequency:** 1/round for 6 rounds

**Effect:** Dexterity damage 1d2

**Cure:** 1 save

If the familiar already has a poison, the witch can instead _empower_ its poison. An empowered
poison's frequency increases by 50%.

**Venom Expert (Ex)**

**Ability:** A venom siphoner does not risk exposure to her familiar's poison when attempting to
[milk venom](ref/rule/harvesting-poisons) from it.

**Gained:** At 2nd Level

**Replaces:** 2nd-level hex

**Toxic Blood (Ex)**

**Ability:** Additionally, when casting spells that have a single target and require a Fortitude
save, she can cause the spell to deliver this poison as a **free action**; a target who succeeds at
the save against the spell also avoids being affected by the poison.

**Flavor:** The venom siphoner's blood becomes toxic, empowering her abilities.

**Gained:** At 6th Level

**Passive:** Any creature that deals [bleed](ref/rule/bleed) damage to her with a natural, light, or
one-handed weapon is automatically exposed to the same poison granted to her familiar and must
succeed at the save or be affected by the poison.

**Replaces:** 6th-level hex

**Special:** This ability refreshes when the venom siphoner communes with her familiar to prepare
her daily spells.

**Usage:** Intelligence3 modifier times/day
