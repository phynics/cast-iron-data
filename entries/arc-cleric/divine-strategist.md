+++
id = "ref/arc-cleric/divine-strategist"
kind = "archetype"
title = "Divine Strategist"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Divine%20Strategist"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_strategist", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "ultimate-combat"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "domains" },
  { anchor = "master-tactician", level = 1 },
  { anchor = "caster-support" },
  { anchor = "tactical-expertise", level = 8 },
]
trades = [
  { replaces = "Channel energy", feature = "channel-energy", by = ["master-tactician"] },
]
+++

The divine strategist leads the armies of the faithful, not from the front lines but through her
clever strategy and tactical acumen.

## Domains {#domains}

A divine strategist gains only a single domain.

## Master Tactician (Ex) {#master-tactician}

A divine strategist can always act in a surprise round even if she fails to make a Perception check
to notice enemies, though she is considered [flat-footed](ref/rule/flat-footed) until she acts. In
addition, the divine strategist gains a bonus on initiative checks equal to 1/2 her cleric level. At
20th level, a divine strategist's initiative roll is automatically a natural 20. Allies able to see
and hear the divine strategist gain a bonus on initiative checks equal to 1/4 the divine
strategist's level. This is a language-dependent ability. This ability replaces channel energy.

## Caster Support (Su) {#caster-support}

A divine strategist can use the [aid another](ref/rule/aid-another-2) action to assist another
divine spellcaster, granting a +2 circumstance bonus on caster level checks and
[concentration](ref/rule/concentration) checks until the beginning of the divine strategist's next
turn. This bonus increases by +1 at 4th level and every four levels thereafter (to a maximum of +7
at 20th level). The allied caster must remain adjacent to the divine strategist to gain this
benefit. Caster support can be used to assist arcane spellcasters or characters using magical items,
but they gain only [half](ref/misc/fractions-and-rounding) the normal bonus.

## Tactical Expertise (Ex) {#tactical-expertise}

At 8th level, a divine strategist knows how to take best advantage of tactical opportunities.
Whenever she is [flanking](ref/rule/flanking) or makes an attack of opportunity, she may add her
Intelligence bonus (if any) as a bonus on the attack roll. In addition, once per day as a swift
action she may add her Intelligence modifier as a bonus on any single d20 roll made as part of a
[readied action](ref/rule/ready). She can use this ability one additional time per day for every two
levels after 8th.
