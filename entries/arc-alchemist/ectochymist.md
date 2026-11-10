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
replaces = ["Bombs", "Poison resistance", "Poison use", "Swift poisoning", "The 8th-level alchemist discovery", "Poison immunity"]
replaces_features = ["poison-resistance", "poison-use", "swift-poisoning"]
+++

Ectochymists study the effects of alchemy on soul and spirit, focusing on fighting ghosts and other
incorporeal creatures.

**Gained class skills:** kr

**Ectoplasmic Blanche (Su)**

**Fullround:** An ectochymist can alchemically treat a melee weapon so that it deals full damage to
incorporeal creatures. This lasts until the next time that weapon is used to make an attack.

**Replaces:** Bombs

**Usage:** alchemist level + Intelligence modifier times/day

**Cool-Headed (Ex)**

**At 2nd Level:** An ectochymist gains a +2 bonus on saves against death, fear, and negative energy
effects.

**At 5th Level:** This bonus increases to +4.

**At 8th Level:** This bonus increases to +6.

**Replaces:** Poison resistance

**Advanced Ectochymistry (Su)**

**Gained:** At 2nd Level

**Passive:** A weapon coated in an ectochymist's ectoplasmic blanche also deals full damage to
haunts.

**Replaces:** Poison use

**Swift Ectochymistry (Su)**

**Gained:** At 6th Level

**Replaces:** Swift poisoning

**Swift:** An ectochymist can use ectoplasmic blanche on one of his own weapons. When coated on a
weapon wielded by the ectochymist, ectoplasmic blanche lasts for a number of attacks equal to his
Intelligence modifier (minimum 1 attack).

**Ghost Trap (Su)**

**Gained:** At 8th Level

**Replaces:** The 8th-level alchemist discovery

**Special:** An ectochymist can throw a trap to capture an incorporeal creature of up to 1 Hit Die
per alchemist level he possesses.

**Standard:** The ectochymist can expend a use of ectoplasmic blanche to coat the inside of a
container with his blanche and throw it at an incorporeal creature as a ranged touch attack. If he
hits, the creature receives a Will save to escape the trap (DC = 10 +
[half](ref/misc/fractions-and-rounding) his alchemist level + his Intelligence modifier). If the
creature fails its save, it is sealed within the vessel until someone breaks or opens that vessel.
The ghost trap automatically survives being thrown at the incorporeal creature, but otherwise is
only as durable as the vessel (normally [hardness](ref/umr/hardness) 5, 1 hp for a glass bottle).

**Ectochymical Analysis (Sp)**

**Ability:** An ectochymist can use alchemical processes to uncover esoteric knowledge from a
haunted area that would normally require divinations to ascertain. This process takes 10 minutes and
expends one use of ectoplasmic blanche. Treat this effect as
[speak with haunt](ref/spell/speak-with-haunt) with a saving throw DC equal to 10 + 1/2 the
ectochymist's class level + the ectochymist's Charisma modifier and a caster level equal to the
ectochymist's class level.

**Gained:** At 10th Level

**Replaces:** Poison immunity

**Special:** Because the ectochymist is performing an analysis to answer his questions and not
speaking with the haunt directly, he uses Craft (alchemy) rather than Sense Motive to oppose any
Bluff checks the spirit might attempt in order to mislead him.

**Discoveries:** The following discoveries complement the ectochymist archetype:
[alchemical simulacrum](ref/discovery/alchemical-simulacrum),
[cognatogen](ref/discovery/cognatogen), [grand cognatogen](ref/discovery/grand-cognatogen),
[greater alchemical simulacrum](ref/discovery/greater-alchemical-simulacrum), and
[mummification](ref/discovery/mummification).
