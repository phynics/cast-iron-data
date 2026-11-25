+++
id = "ref/arc-alchemist/ectochymist"
kind = "archetype"
title = "Ectochymist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Ectochymist"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ectochymist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "occult-adventures"
page = "112"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "ectoplasmic-blanche", level = 1 },
  { anchor = "cool-headed", level = 2 },
  { anchor = "advanced-ectochymistry", level = 2 },
  { anchor = "swift-ectochymistry", level = 6 },
  { anchor = "ghost-trap", level = 8 },
  { anchor = "ectochymical-analysis", level = 10 },
]
trades = [
  { replaces = "Bombs", feature = "bomb", by = ["ectoplasmic-blanche"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["cool-headed"] },
  { replaces = "Poison use", feature = "poison-use", by = ["advanced-ectochymistry"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["swift-ectochymistry"] },
  { replaces = "The 8th-level alchemist discovery", feature = "discovery", levels = [8], by = ["ghost-trap"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["ectochymical-analysis"] },
]
+++

Ectochymists study the effects of alchemy on soul and spirit, focusing on fighting ghosts and other
incorporeal creatures.

## Class Skills {#class-skills}

An ectochymist adds Knowledge (religion) to his list of class skills. This alters the alchemist's
class skills.

## Ectoplasmic Blanche (Su) {#ectoplasmic-blanche}

An ectochymist can alchemically treat a melee weapon so that it deals full damage to incorporeal
creatures. The process requires a full-round action and lasts until the next time that weapon is
used to make an attack. An ectochymist can use this ability a number of times per day equal to his
alchemist level + his Intelligence modifier. This ability replaces bombs.

## Cool-Headed (Ex) {#cool-headed}

At 2nd level, an ectochymist gains a +2 bonus on saves against death, fear, and negative energy
effects. This bonus increases to +4 at 5th level, and to +6 at 8th level. This ability replaces
poison resistance.

## Advanced Ectochymistry (Su) {#advanced-ectochymistry}

At 2nd level, a weapon coated in an ectochymist's ectoplasmic blanche also deals full damage to
haunts. This ability replaces poison use.

## Swift Ectochymistry (Su) {#swift-ectochymistry}

At 6th level, an ectochymist can use ectoplasmic blanche on one of his own weapons as a swift
action. When coated on a weapon wielded by the ectochymist, ectoplasmic blanche lasts for a number
of attacks equal to the ectochymist's Intelligence modifier (minimum 1 attack). This ability
replaces swift poisoning.

## Ghost Trap (Su) {#ghost-trap}

At 8th level, an ectochymist can throw a trap to capture an incorporeal creature of up to 1 Hit Die
per alchemist level he possesses. As a standard action, the ectochymist can expend a use of
ectoplasmic blanche to coat the inside of a container with his blanche and throw it at an
incorporeal creature as a ranged touch attack. If he hits, the creature receives a Will save to
escape the trap (DC = 10 + 1/2 his alchemist level + his Intelligence modifier). If the creature
fails its save, it is sealed within the vessel until someone breaks or opens that vessel. The ghost
trap automatically survives being thrown at the incorporeal creature, but otherwise is only as
durable as the vessel (normally [hardness](ref/umr/hardness) 5, 1 hp for a glass bottle).This
ability replaces the 8th-level alchemist discovery.

## Ectochymical Analysis (Sp) {#ectochymical-analysis}

At 10th level, an ectochymist can use alchemical processes to uncover esoteric knowledge from a
haunted area that would normally require divinations to ascertain. This process takes 10 minutes and
expends one use of ectoplasmic blanche. Treat this effect as
_[speak with haunt](ref/spell/speak-with-haunt)_ with a saving throw DC equal to 10 + 1/2 the
ectochymist's class level + the ectochymist's Charisma modifier and a caster level equal to the
ectochymist's class level. Because the ectochymist is performing an analysis to answer his questions
and not speaking with the haunt directly, he uses Craft (alchemy) rather than Sense Motive to oppose
any Bluff checks the spirit might attempt in order to mislead him. This ability replaces poison
immunity.

## Discoveries {#discoveries}

The following discoveries complement the ectochymist archetype:
[alchemical simulacrum](ref/discovery/alchemical-simulacrum),
[cognatogen](ref/discovery/cognatogen), [grand cognatogen](ref/discovery/grand-cognatogen),
[greater alchemical simulacrum](ref/discovery/greater-alchemical-simulacrum), and
[mummification](ref/discovery/mummification).
