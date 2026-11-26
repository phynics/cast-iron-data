+++
id = "ref/arc-barbarian/geminate-invoker"
kind = "archetype"
title = "Geminate Invoker"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Geminate%20Invoker"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geminate_invoker", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "adventurers-guide"
page = "166"

[fields]
kind = "archetype"
features = [
  { anchor = "contemplative" },
  { anchor = "trance" },
  { anchor = "haunt-channeler", level = 3 },
  { anchor = "spirit-conduit", level = 4 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["haunt-channeler"] },
  { replaces = "Rage powers gained at 4th, 8th, and 12th levels", feature = "rage-powers", levels = [4, 8, 12], by = ["spirit-conduit"] },
  { alters = "The barbarian's class skills", by = ["contemplative"] },
  { alters = "alignment", by = ["contemplative"] },
  { alters = "Rage", feature = "rage", by = ["trance"] },
]
+++

Geminate invokers are barbarians who use [Rivethun](ref/rule/aff-animists) traditions to invite
spirits into their bodies. The spirits' aid enables them to overcome the distractions of the
flesh—they can ignore pain, and even defy death. These ascetics make up much of the Rivethun martial
forces.

## Contemplative (Ex) {#contemplative}

A geminate invoker adds [Knowledge (history)](ref/skill/knowledge-history),
[Knowledge (religion)](ref/skill/knowledge-religion), and [Linguistics](ref/skill/linguistics) to
his list of class skills. Unlike most barbarians, a geminate invoker can be lawful, but must
maintain a neutral element to his alignment. A geminate invoker who ceases to be neutral-aligned
cannot activate his trance ability.

This alters the barbarian's class skills and alignment.

## Trance (Ex) {#trance}

As a free action, a geminate invoker can enter a self-imposed trance, ignoring the physical limits
of his body. This ability functions similarly to a barbarian's rage, except where noted below, and
feats, spells, and abilities that affect a barbarian's rage (such as the
[Extra Rage](ref/feat/extra-rage) feat) apply to an geminate invoker's trance. A geminate invoker
gains rage powers as per a normal barbarian, but he can never gain totem rage powers (_Pathfinder
RPG Advanced Player's Guide_ 74) via this ability.

Instead of the normal rage bonuses and penalties, a geminate invoker in a trance gains a +4 morale
bonus to his Constitution; gains a +2 morale bonus on Reflex and Will saving throws; takes no
penalties to AC; can still use Dexterity-, Intelligence-, and Charisma-based skills; and gains
[Diehard](ref/feat/diehard) as a bonus feat. The Constitution bonus increases to +6 and the save
bonus increases to +3 when he gains greater rage, and they increase to a +8 Constitution bonus and a
+4 bonus on saves when he gains mighty rage.

This ability alters rage.

## Haunt Channeler (Su) {#haunt-channeler}

At 3rd level, a geminate invoker gains the power to sense and absorb lingering spiritual energy.
This functions identically to the [medium](ref/class/medium) class ability of the same name
(_Pathfinder RPG Occult Adventures_ 31), except the geminate invoker deals 1d6 points of damage to
haunts for every 3 barbarian levels he has.

This ability replaces trap sense.

## Spirit Conduit (Su) {#spirit-conduit}

At 4th level, a geminate invoker can invite a spirit into his body each time he enters a trance,
gaining a lesser totem rage power for the duration of his trance. He can select a new totem each
time he enters his trance, though the GM might rule that certain totem spirits are simply not
available in certain locations (such as channeling a celestial totem in an evil god's temple).
Invoking a totem counter to his alignment (such as a neutral good character invoking a fiend totem)
requires the geminate invoker to succeed at a DC 12 Charisma check each round to dominate the
spirit. Failure indicates the spirit escapes, immediately ending the trance.

At 8th level, the geminate invoker gains a second totem rage power, though it must use the
previously granted lesser totem rage power as a prerequisite. At 12th level, he also gains the
greater totem rage power that uses the previously granted powers as prerequisites.

This ability replaces the rage powers gained at 4th, 8th, and 12th levels.
