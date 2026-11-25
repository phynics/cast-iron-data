+++
id = "ref/arc-skald/warlord"
kind = "archetype"
title = "Warlord"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Warlord"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warlord", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "49"

[fields]
kind = "archetype"
features = [
  { anchor = "intimidating-prowess" },
  { anchor = "unshakable", level = 2 },
  { anchor = "raging-song" },
  { anchor = "minions", level = 7 },
  { anchor = "intimidated-push", level = 8 },
]
trades = [
  { replaces = "Scribe Scroll feat", feature = "scribe-scroll", by = ["intimidating-prowess"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["unshakable"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["raging-song"] },
  { replaces = "Lore master", feature = "lore-master", by = ["minions"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["intimidated-push"] },
]
+++

The warlord wields his force of personality like a weapon, intimidating his allies and ensuring that
his followers heed his commands. The warlord doesn't inspire his followers so much as instill fear
in them. Always watching his foes for moments of vulnerability, the warlord seeks to exploit his
enemies' weaknesses to gain victory.

## Intimidating Prowess {#intimidating-prowess}

A warlord gains [Intimidating Prowess](ref/feat/intimidating-prowess) as a bonus feat.

This feat replaces the Scribe Scroll feat.

## Unshakable (Ex) {#unshakable}

At 2nd level, a warlord develops an unshakable resolve, gaining a +2 bonus on saving throws against
fear effects.

This ability replaces well-versed.

## Raging Song (Su) {#raging-song}

A warlord gains the following raging song.

_Fear Me_ (Su): At 5th level, the warlord can remind his allies that failing him is far more
frightening than the opposition. This raging song works like distraction, except that it applies to
saving throws against fear effects instead of patterns and figments, and the warlord attempts an
Intimidate check with a -10 penalty instead of a Perform check. Additionally, the warlord's allies
can use the warlord's Intimidate check result (with the -10 penalty) as the DC for attempts to
demoralize them using Intimidate.

This ability replaces spell kenning.

## Minions (Ex) {#minions}

At 7th level, a warlord attracts a group of followers through his fearsome reputation and gains the
[Leadership](ref/feat/leadership) feat as a bonus feat.

This replaces the lore master ability.

## Intimidated Push (Ex) {#intimidated-push}

At 8th level, a warlord inspires fear in his cohort and followers, ensuring they do not fail and
thus suffer his wrath. When he uses inspired rage, his cohort increases her morale bonus on Will
saves from inspired rage by 1 and his followers increase their morale bonuses on Will saves from
inspired rage by 2.

This replaces improved uncanny dodge.
