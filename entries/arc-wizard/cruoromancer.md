+++
id = "ref/arc-wizard/cruoromancer"
kind = "archetype"
title = "Cruoromancer"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Cruoromancer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cruoromancer", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "advanced-race-guide"
page = "98"

[fields]
kind = "archetype"
replaces = ["Arcane bond", "5th-level bonus feat", "10th-level bonus feat", "15th-level bonus feat", "The 20th-level wizard bonus spell"]
replaces_features = ["arcane-bond"]
+++

To those who know how to manipulate it, the blood of a dhampir can be a powerful component to magic.
A cruoromancer infuses his necromantic magic with the power of his unique mixture of living blood
and undead ichor. As his power increases in this strange arcane art, a cruoromancer finds potent
ways to infuse his unique blood with necromancy spells. A cruoromancer has the following class
features.

**Prerequisites:** Dhampir

**Blood Infusion (Su)**

**Gained:** At 1st Level

**Special:** Each time a cruoromancer uses _blood infusion,_ he drains a portion of his own blood
either by cutting himself with a blade or by opening a scab from a previous wound. When he does
this, he takes an amount of damage equal to 1d4 + the level of the spell being infused. A
cruoromancer can only affect a spell with a single type of _blood infusion._

**Swift:** When a cruoromancer casts a spell of the necromancy school, he can opt to infuse that
spell with his undead-tainted blood, choosing a _blood infusion_ that he knows.

**Focused Infusion**

**Passive:** When the cruoromancer uses this infusion, he adds +1 to the DC of the infused
necromancy spell.

**Sickening Infusion**

**Passive:** When the cruoromancer uses this infusion, any creature damaged by the infused
necromancy spell becomes [sickened](ref/misc/sickened) for 1 round.

**Replaces:** Arcane bond

**Blood Command (Su)**

**Ability:** A cruoromancer can control up to 5 Hit Dice worth of undead creatures per caster level
instead of the normal 4 Hit Dice of undead when casting the [animate dead](ref/spell/animate-dead)
spell.

**Gained:** At 5th Level

**Special:** He also gains the following _blood infusion_ ability.

**Commanding Infusion**

**Ability:** When using this infusion with _[animate dead](ref/spell/animate-dead),_ the
cruoromancer can create a number of Hit Dice of undead equal to three times his caster level instead
of twice his caster level.

**Replaces:** 5th-level bonus feat

**Blood Desecration (Su)**

**Ability:** A cruoromancer gains the following _blood infusion._

**Gained:** At 10th Level

**Desecrating Infusion**

**Ability:** When the cruoromancer uses this infusion, he can choose to center a
_[desecrate](ref/spell/desecrate)_ effect on himself or a single target of the spell modified by
this infusion (he chooses upon casting). This effect is like the [desecrate](ref/spell/desecrate)
spell, but lasts for 1 minute per caster level of the cruoromancer, and does not interact with
altars, shrines, or permanent fixtures that boost the _[desecrate](ref/spell/desecrate)_ effect.

**Replaces:** 10th-level bonus feat

**Blood Ability (Su)**

**Ability:** A cruoromancer can choose to scry through a single undead creature he created with a
spell modified by a _commanding infusion._ The undead creature is treated as if imbued with an
[arcane eye](ref/spell/arcane-eye) spell (caster level equal to the cruoromancer's wizard level).

**Gained:** At 15th Level

**Replaces:** 15th-level bonus feat

**Perfect Infusion (Su)**

**Ability:** A cruoromancer can use his _blood infusions_ without taking damage.

**Gained:** At 20th Level

**Replaces:** The 20th-level wizard bonus spell
