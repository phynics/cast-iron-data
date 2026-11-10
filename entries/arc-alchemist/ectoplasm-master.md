+++
id = "ref/arc-alchemist/ectoplasm-master"
kind = "archetype"
title = "Ectoplasm Master"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Ectoplasm%20Master"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ectoplasm_master", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "14"

[fields]
kind = "archetype"
replaces = ["Brew Potion"]
alters = ["Extracts"]
replaces_features = ["brew-potion"]
alters_features = ["extracts"]
+++

Able to distill spectral horrors into alchemical reagents, the eccentric techniques of the ectoplasm
master originated among agents of the [Whispering Way](ref/rule/f-gravepath), though their secrets
have since been exposed and spread to the winds by their rivals in the Esoteric Order of the
Palatine Eye. Today, the ectoplasm master is not automatically regarded as an agent of sinister evil
as a result.

**Ectoplasmic Extracts (Su)**

**Alters:** Extracts

**Gained:** At 1st Level

**Passive:** As a result of his eccentric techniques and use of odd alchemical components, an
ectoplasm master has an expanded formula list. He adds all sorcerer/wizard spells of 6th level or
lower from the necromancy school to his alchemist formula list (but must still learn each of these
spells normally). If a spell appears on both the alchemist formula list and the sorcerer/wizard
spell list, the ectoplasm master uses the lower of the two spell levels listed for the spell.

**Replaces:** Brew Potion

**Special:** Instead of using alchemical reagents in order to create alchemical items (including his
bombs, extracts, and mutagens), an ectoplasm master uses reagents such as corpse dust, crystallized
ectoplasm, and similar reagents as alchemical catalysts. Just as with standard alchemists, the costs
of these materials are insignificant and are comparable to the costs of the valueless material
components of most spells.

**Ectoplasm Master Discoveries (Su)**

**Passive:** An ectoplasm master is able to select the following three alchemist discoveries, in
addition to general discoveries.

**Ectoplasmic Mutagen**

**Passive:** Whenever the ectoplasm master imbibes a mutagen, his living flesh transmutes into
ectoplasm, causing him to take on a semi-liquid form. He no longer gains a natural armor bonus from
his mutagen, but instead becomes immune to critical hits and precision damage (such as sneak
attacks) while under the mutagen's effects.

**Prereq:** 6th-level alchemist

**Ectoplasmic Servant**

**Ability:** Whenever he summons a creature using an ectoplasmic extract, the creature must appear
in a square adjacent to his own, and it gains the
[ectoplasmic creature template](ref/template/ectoplasmic). Creatures summoned using ectoplasmic
extracts cannot have templates other than the ectoplasmic creature template.

**Passive:** An ectoplasm master who selects this discovery adds all
[summon monster](ref/spell/summon-monster) spells of 6th level or lower to his alchemist formula
list as ectoplasmic extracts.

**Siphon Bomb**

**Passive:** The ectoplasm master's bombs can be modified to neutralize and crystallize the
ectoplasmic energy of haunts and incorporeal undead. A siphon bomb deals full damage to incorporeal
creatures as if it were a force effect, but deals only nonlethal damage to corporeal creatures. A
siphon bomb also damages haunts, provided the siphon bomb explodes within a haunt's area of effect.
This discovery modifies the alchemist's bombs and doesn't stack with other discoveries that modify
bombs (Primary Bomb Discoveries).
