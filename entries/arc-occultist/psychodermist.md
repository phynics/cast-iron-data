+++
id = "ref/arc-occultist/psychodermist"
kind = "archetype"
title = "Psychodermist"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Psychodermist"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychodermist", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "25"

[fields]
kind = "archetype"
replaces = ["Magic item skill", "Object reading", "Aura sight", "Outside contact", "Binding circles", "fast circles"]
alters = ["Implements"]
+++

Rather than tapping the psychic energy residing within esoteric items, psychodermists form
supernatural bonds with trophies taken from creatures they have slain. Through these mementos, these
occultists manifest not only their own magic, but also the unique powers of their fallen foes.

**Gained class skills:** heal, kna, kl, sur

**Lost class skills:** dd, ke, kh, soh

**Trophies (Su)**

**Ability:** The psychodermist gains [Harvest Parts](ref/feat/harvest-parts) as a bonus feat, and he
can select one monster part per implement school he knows to become a permanently preserved trophy
so long as it remains in his possession. Each trophy functions as the psychodermist's implement for
its associated implement school. A trophy that fits multiple implement categories, such as a hand
with clawed fingers, can function for only one implement school at a time.

**Alters:** Implements

**Flavor:** A psychodermist learns how to siphon power from pieces of creatures he has slain.

**Info:** A trophy can be integrated into another item, such as an ornament or a magic item, but
otherwise does not take up a magic item slot, even when worn. A psychodermist can replace trophies
with new ones harvested from slain foes, although doing so causes the old trophies to rot at their
normal rate. In order to craft a trophy, the psychodermist must have been present during the
creature's death.

**Gained:** At 1st Level

**Special:** Psychodermists use the following monster parts for each implement school.

**Abjuration**

**Info:** Chitin, hides, scales, and other natural armor.

**Conjuration**

**Info:** Gizzards, glands, hearts, livers, and other internal organs.

**Divination**

**Info:** Ears, eyes, tongues, and other sensory organs.

**Enchantment**

**Info:** Feathers, fur, hair, spines, and other decorative features.

**Evocation**

**Info:** Claws, fangs, horns, and other natural weapons.

**Illusion**

**Info:** Fingers, tendrils, toes, and other prehensile digits.

**Necromancy**

**Info:** Bones, bile, and life-sustaining fluids, such as blood.

**Transmutation**

**Info:** Feet, hands, paws, wings, and other appendages tied to locomotion.

**Monster Hunting Lore (Ex)**

**Gained:** At 2nd Level

**Passive:** A psychodermist gains a bonus equal to half his occultist level on skill checks made to
craft trophies and Knowledge checks made to identify the abilities and weaknesses of creatures.

**Replaces:** Magic item skill

**Discern Death (Su)**

**Fullround:** A psychodermist can glean information from a creature's corpse. The psychodermist
must study at least one drop of the creature's blood, a small portion of its flesh, or a fragment of
one of its bones as a part of this action. This ability otherwise functions as
[blood biography](ref/spell/blood-biography), using the psychodermist's occultist level as his
caster level.

**Gained:** At 2nd Level

**Provokes attack of opportunity:** Yes

**Replaces:** Object reading

**Usage:** 1 time/day + 1 per 3 occultist levels beyond 2nd

**Seek Prey (Su)**

**Gained:** At 5th Level

**Replaces:** Aura sight

**Standard:** A psychodermist can supernaturally detect creatures around him. This functions as the
spell [aura sight](ref/spell/aura-sight), except the duration is 1 round and the psychodermist
learns the locations and power of all auras of a specific creature type, similar to
[detect undead](ref/spell/detect-undead) except the psychodermist can choose any creature type
represented among the trophies he has selected for that day.

**Residual Hatred (Su)**

**Ability:** The psychodermist can spend mental focus invested in a trophy to gain the ranger's
[favored enemy](ref/ability/favored-enemy) class feature against the kind of creature from which the
trophy was crafted. The favored enemy bonus is +2, and it applies against the specific creature
variety, not the creature type; a psychodermist could use a red dragon scale trophy to gain favored
enemy (red dragon), but not favored enemy (dragon).

**Flavor:** A psychodermist can tap into the psychic death throes of the monsters his trophies are
derived from, increasing his efficiency at slaying similar beasts.

**At 10th Level:** Each point of mental focus spent grants a cumulative +2 favored enemy bonus, with
a maximum bonus of +4.

**At 15th Level:** The maximum bonus becomes +3.

**At 20th Level:** The maximum bonus increases to +4.

**Gained:** At 8th Level

**Replaces:** Outside contact

**Special:** This benefit lasts until the psychodermist regains his mental focus.

**Manifest Abilities (Su)**

**Ability:** Alternatively, he can spend 1 point of mental focus as a **standard action** to add any
two of the creature's [spell-like abilities](ref/umr/spell-like-abilities) to his list of spells
known. To determine the spell's level for this ability, use the level as it appears on the spell
list for an occultist, wizard, or cleric, in that order; if it appears on none of those lists, use
the spell's highest spell level. (For example, [lesser restoration](ref/spell/restoration-lesser)
would be a 2nd-level spell, despite appearing on the paladin's 1st-level list.)

**Ability2:** He can instead spend 2 points of mental focus to activate either ability as a **move
action**, or 3 points to activate it as a **swift action**.

**Flavor:** A psychodermist can use the latent energy within his trophies to replicate his victims'
special abilities.

**At 16th Level:** The psychodermist adds abilities offered by
[monstrous physique IV](ref/spell/monstrous-physique-4) to the options he can select using the first
ability.

**Gained:** At 12th Level

**Replaces:** Binding circles, fast circles

**Special:** Both uses of this ability last for 1 minute per psychodermist level. The saving throw
DC for creature special abilities is equal to 10 + half the psychodermist's level + his Intelligence
modifier.

**Standard:** He can spend 1 point of mental focus invested in a trophy to gain one of that
creature's special abilities that could be granted by the spell
[monstrous physique III](ref/spell/monstrous-physique-3).
