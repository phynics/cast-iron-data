+++
id = "ref/arc-magus/spellblade"
kind = "archetype"
title = "Spellblade"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Spellblade"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellblade", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-magic"
page = "49"

[fields]
kind = "archetype"
replaces = ["Spellstrike"]
replaces_features = ["spellstrike"]
+++

A spellblade magus can manifest a ghostly blade of force that can be used as an off-hand weapon.

**Force Athame (Sp)**

**Gained:** At 2nd Level

**Replaces:** Spellstrike

**Special:** The _athame_ acts as a [dagger](ref/eq-weapon/dagger), but the hand holding it is still
considered free for the purpose of casting spells and delivering touch attacks. The magus can use
the _athame_ as if he were [fighting with two weapons](ref/rule/two-weapon-fighting), or can use
that hand to cast spells as part of the _spell combat_ class ability (but not both in the same
round). Attacks with the _athame_ are [force](ref/spelldef/force) attacks and deal force damage.

**Swift:** A spellblade magus can sacrifice a prepared magus spell of 1st level or higher to create
a dagger of force in his off hand. The _athame_ lasts for 1 minute or until dismissed, has an
enhancement bonus on attack and damage rolls equal to the level of the spell sacrificed (maximum
+5), and is considered a weapon the spellblade is holding for purposes of his _arcane pool_ feature
(using the pool to add abilities to a held weapon applies to the magus's physical weapon and to the
_athame_ for no additional cost).

**Spellblade Arcana**

**Ability:** A spellblade gains access to the following magus arcana. He cannot select any arcana
more than once.

**Pool-Sourced Athame (Su)**

**Ability:** Instead of sacrificing a prepared spell to create the _force athame,_ the magus can
spend points from his _arcane pool_ to do so. An _athame_ created this way has an enhancement bonus
equal to the number of _arcane pool_ points spent.

**Spellblade Parry (Su)**

**Immediate:** When an enemy makes a melee attack roll against the magus, he can end the _athame's_
duration to gain a deflection bonus to his Armor Class until the end of his next turn. This bonus is
equal to the level of the spell sacrificed to create the _athame_ (maximum +5).

**Throw Athame (Su)**

**Standard:** A spellblade magus can throw his _athame_ up to 60 feet as a ranged attack (no range
penalty). If the _athame_ misses, it returns automatically to the magus' hand just before his next
turn. If the _athame_ hits, it deals damage and its duration ends; the magus can choose to spend up
to 2 points from his _arcane pool_ to increase the thrown _athame's_ damage by +1d6 for each point
spent.

**Magus Arcana:** The following magus arcana complement the spellblade archetype:
[critical strike](ref/arcana/critical-strike), [hasted assault](ref/arcana/hasted-assault),
[pool strike](ref/arcana/pool-strike), and [spell shield](ref/arcana/spell-shield).
