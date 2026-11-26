+++
id = "ref/arc-sorcerer/sorcerer-of-sleep"
kind = "archetype"
title = "Sorcerer of Sleep"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Sorcerer%20of%20Sleep"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sorcerer_of_sleep", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "black-markets"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "pesh-expert" },
  { anchor = "sahir-afiyun", level = 1 },
  { anchor = "pesh-touch", level = 1 },
]
trades = [
  { replaces = "Bloodline arcana", feature = "bloodline", power = "bloodline arcana", by = ["pesh-expert"] },
  { replaces = "Eschew materials", feature = "eschew-materials", by = ["sahir-afiyun"] },
  { replaces = "1st-level bloodline power", feature = "bloodline", levels = [1], power = "bloodline power", by = ["pesh-touch"] },
]
+++

Some sorcerers have trouble accessing their innate gifts and must find another way to unlock them.
For a sorcerer of sleep, the mind-altering drug [pesh](ref/drug/pesh) (see page 19) is the key. The
garbled visions the drug provides allow a sorcerer of sleep to reach an ideal state for channeling
her [arcane](ref/sorcbloodline/arcane) power. The arcane and
[dreamspun](ref/sorcbloodline/dreamspun) bloodlines are the sorcerer heritages most often associated
with pesh, though a sorcerer of sleep might exhibit any bloodline; pesh is a tool to enhance her
gifts, rather than their source.

## Pesh Expert {#pesh-expert}

A sorcerer of sleep adds 1/2 her sorcerer level (minimum 1) on Appraise, Craft (alchemy), Heal, and
Knowledge (local) checks related to pesh and other drugs. This ability replaces bloodline arcana.

## Sahir-Afiyun {#sahir-afiyun}

A sorcerer of sleep gains [Sahir-Afiyun](ref/feat/sahir-afiyun) (see page 18) as a bonus feat at 1st
level, even if she does not meet the prerequisites. A sorcerer of sleep adds
[Pesh Euphoria](ref/feat/pesh-euphoria), [Pesh Healing](ref/feat/pesh-healing),
[Pesh Rejuvenation](ref/feat/pesh-rejuvenation), and Sahir-Afiyun (see page 18 for these feats) to
her list of bloodline feats. This ability replaces eschew materials.

## Pesh Touch (Su) {#pesh-touch}

As a standard action, a sorcerer of sleep can make a melee touch attack against a living creature to
cause one of the following effects (sorcerer's choice): the target gains a +2 enhancement bonus to
Strength, the target is [fatigued](ref/misc/fatigued), or the target takes a -2 penalty on saving
throws against illusion and mind-affecting effects. The effects of pesh touch last a number of
rounds equal to 1/2 the sorcerer of sleep's sorcerer level. The effects of pesh touch are not
cumulative, and cannot make the target [exhausted](ref/misc/exhausted). A sorcerer of sleep can use
pesh touch a number of times per day equal to 3 + her Charisma modifier. This ability replaces the
1st-level bloodline power.
