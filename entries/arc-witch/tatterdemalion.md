+++
id = "ref/arc-witch/tatterdemalion"
kind = "archetype"
title = "Tatterdemalion"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Tatterdemalion"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tatterdemalion", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "horror-adventures"
page = "73"

[fields]
kind = "archetype"
features = [
  { anchor = "cantrips", level = 1 },
  { anchor = "dancing-strings", level = 1 },
  { anchor = "witchweaver" },
  { anchor = "moth-eaten", level = 4 },
  { anchor = "lace-weaver", level = 8 },
  { anchor = "sinister-stitching", level = 12 },
  { anchor = "unravel", level = 16 },
]
trades = [
  { replaces = "Hex gained at 1st level", feature = "hex", levels = [1], by = ["dancing-strings"] },
  { replaces = "Hexes gained at 4th, 8th, 12th, and 16th levels", feature = "hex", levels = [4, 8, 12, 16], by = ["unravel"] },
  { alters = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { alters = "Cantrips", feature = "cantrips", by = ["cantrips"] },
  { alters = "Spells", feature = "spells", by = ["dancing-strings"] },
]
+++

Some witches can bend the warp and weft of fabric and thread.

## Weapon Proficiency {#weapon-proficiency}

A tatterdemalion is proficient with [bolas](ref/eq-weapon/bolas), [nets](ref/eq-weapon/net), and
[whips](ref/eq-weapon/whip).

This alters the witch's weapon proficiencies.

## Cantrips {#cantrips}

A tatterdemalion must choose _mage hand, open/close,_ and
_[prestidigitation](ref/spell/prestidigitation)_ as her prepared cantrips at 1st level, and they
require a piece of cloth, string, rope, or other woven material (including clothing) as a focus. Any
action she takes with these cantrips must involve the focus. Starting at 2nd level, she can choose
any cantrip for her remaining cantrip.

This alters the witch's cantrips.

## Dancing Strings (Su) {#dancing-strings}

A tatterdemalion adds _[animate rope](ref/spell/animate-rope)_ to her class spell list and spells
her familiar knows. She can control her clothing and cloth, rope, or woven fabric she wears in a
manner otherwise identical to the [prehensile hair](ref/hex/prehensile-hair) hex.

This alters spells and replaces the hex gained at 1st level.

## Witchweaver {#witchweaver}

A tatterdemalion gains the following unique hexes, with a caster level equal to her witch level.

## Moth-Eaten (Sp) {#moth-eaten}

At 4th level, a tatterdemalion can make a touch attack that damages leather, rope, or cloth like
_[rusting grasp](ref/spell/rusting-grasp)_ damages metal, once per day per witch level.

## Lace Weaver (Sp) {#lace-weaver}

At 8th level, a tatterdemalion can create cloth as per _[minor creation](ref/spell/minor-creation)_
or create one 5-foot cube of tangled skeins of cloth per witch level, affecting the target areas as
per _[web](ref/spell/web)_, once per day for every 4 witch levels she has.

## Sinister Stitching (Su) {#sinister-stitching}

At 12th level, once per day for every 4 witch levels she has, a tatterdemalion can conjure enchanted
threads to hinder a creature she can see (Fortitude negates). The tatterdemalion can choose to
either sew shut the target's eyes ([blinding](ref/misc/blinded) it) or mouth (preventing speech,
bite attacks, breath weapons, verbal components, command words, and the like). The target can end
the effect with a successful Strength check (DC = 15 + 1/2 the tatterdemalion's witch level) as a
standard action, or by slashing the stitches with a magic slashing weapon as a full-round action
that provokes attacks of opportunity. Either way, the victim takes 1d4 points of
[bleed](ref/rule/bleed) damage and either is [dazzled](ref/misc/dazzled) (for stitched eyes) or
takes a -2 penalty on bite attack and damage rolls and a 20% chance of spell failure with verbal
components (for a stitched mouth). Either residual effect lasts 1 minute per witch level. Any
creature can safely remove the enchanted threads with a minute of work and a successful DC 25 Heal
check.

## Unravel (Su) {#unravel}

At 16th level, once per day when a tatterdemalion is hit by a melee or ranged attack, she can
unravel herself as an immediate action, causing her body and gear to appear to collapse into a
bundle of tattered rags and strands while she teleports to any open square within 30 feet. She takes
no damage from the triggering attack, but she must have line of effect to the target square. She can
use this ability twice per day at 20th level.

These replace the hexes gained at 4th, 8th, 12th, and 16th levels.
