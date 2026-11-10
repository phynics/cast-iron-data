+++
id = "ref/arc-cleric/crashing-wave"
kind = "archetype"
title = "Crashing Wave"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crashing_wave", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "23"

[fields]
kind = "archetype"
replaces = ["Channel energy"]
alters = ["Bonus languages", "Spontaneous casting"]
replaces_features = ["channel-energy"]
alters_features = ["bonus-languages", "spontaneous-casting"]
+++

Clerics of Gozreh revere their deity as the embodiment of nature and the incarnation of wind and
waves. Clerics who live in or near the sea sometimes embrace the watery aspect of
[Gozreh](ref/faith/gozreh) over the deity's other dimensions and take the title of crashing wave. In
aquatic communities, a crashing wave is often a healer and spiritual leader. Such clerics understand
the tempestuousness and cruelty of the sea, but also its generosity and bounty.

Among aquatic creatures, cecaelias, locathahs, and merfolk are the most likely to walk the path of
the crashing wave. Gnomes, halflings, and humans living on coastlines or working aboard ships may
also answer the call to become crashing waves.

**Sworn to the Sea**

**Info:** A crashing wave must select Gozreh as her deity.

**Speech of the Sea**

**Alters:** Bonus languages

**Info:** A crashing wave's bonus language options include Aquan in addition to the bonus languages
available to the character from her race. The crashing wave does not gain Abyssal, Celestial, or
Infernal as bonus language options.

**Balanced Channel (Su)**

**Action:** Standard

**Flavor:** A crashing wave can channel the pure balance of the ocean - its wildness, its calm, its
cruelty, and its gentleness.

**Gained:** At 1st Level

**Provokes attack of opportunity:** No

**Replaces:** Channel energy

**Special:** The cleric must be able to present her holy symbol to use this ability.

**Usage:** Cha3 modifier times/day

This energy can be used to harm or heal creatures, as the crashing wave chooses. Channeling this
energy causes a 30-foot-radius [burst](ref/misc/burst) centered on the cleric. A crashing wave can
choose whether to include herself in the effect.

If the crashing wave chooses to harm, creatures within the burst that are chaotic good, chaotic
evil, lawful good, or lawful evil take 1d6 points of damage plus 1d6 points of damage for every 2
levels the cleric has beyond 1st (2d6 at 3rd, 3d6 at 5th, and so on). Creatures with a neutral
alignment component are unaffected by this energy. Creatures that take damage from the channeled
energy can attempt a Fortitude save (DC = 10 + [half](ref/misc/fractions-and-rounding) the crashing
wave's level + her Charisma modifier) for half damage. This damage is neither negative nor positive
energy, so a creature's resistance to positive or negative energy does not reduce this damage.
(However, resistance to channeled energy in particular, such as that provided by
[channel resistance](ref/umr/channel-resistance), applies normally.)

If the crashing wave chooses to heal, creatures within the burst that have any neutral alignment
component are healed 1d6 points of damage plus 1d6 points of damage for every 2 levels the cleric
has beyond 1st (2d6 at 3rd, 3d6 at 5th, and so on). This healing does not affect creatures that are
chaotic good, chaotic evil, lawful good, or lawful evil. This healing is positive energy, so any
creatures not healed by positive energy (such as undead) receive no healing from this effect, even
if they have a neutral alignment.

**Spontaneous Casting**

**Ability:** A crashing wave does not gain the ability to spontaneously cast _cure_ or _inflict_
spells by sacrificing prepared spells. However, a crashing wave can spontaneously cast the following
spells by sacrificing a prepared spell of the noted level or higher.

**Alters:** Spontaneous casting

**Spells:** Bless water

**Spells:** Slipstream

**Spells:** Water breathing

**Spells:** Control water

**Spells:** Geyser

**Spells:** Fluid form

**Spells:** Elemental body IV\|(water only)

**Spells:** Seamantle

**Spells:** Elemental swarm\|(water only)
