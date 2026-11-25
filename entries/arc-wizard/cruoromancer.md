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
features = [
  { anchor = "blood-infusion", level = 1 },
  { anchor = "blood-command", level = 5 },
  { anchor = "blood-desecration", level = 10 },
  { anchor = "blood-ability", level = 15 },
  { anchor = "perfect-infusion", level = 20 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["blood-infusion"] },
  { replaces = "5th-level bonus feat", feature = "bonus-feats", levels = [5], by = ["blood-command"] },
  { replaces = "10th-level bonus feat", feature = "bonus-feats", levels = [10], by = ["blood-desecration"] },
  { replaces = "15th-level bonus feat", feature = "bonus-feats", levels = [15], by = ["blood-ability"] },
  { replaces = "The 20th-level wizard bonus spell", by = ["perfect-infusion"] },
]
+++

To those who know how to manipulate it, the blood of a dhampir can be a powerful component to magic.
A cruoromancer infuses his necromantic magic with the power of his unique mixture of living blood
and undead ichor. As his power increases in this strange arcane art, a cruoromancer finds potent
ways to infuse his unique blood with necromancy spells. A cruoromancer has the following class
features.

## Blood Infusion (Su) {#blood-infusion}

When a cruoromancer casts a spell of the necromancy school, he can opt to infuse that spell with his
undead-tainted blood as a swift action. As he increases in level, the power and effects of such
infusions become more potent. Each time a cruoromancer uses blood infusion, he drains a portion of
his own blood either by cutting himself with a blade or by opening a scab from a previous wound.
When he does this, he takes an amount of damage equal to 1d4 + the level of the spell being infused.
A cruoromancer can only affect a spell with a single type of blood infusion. At 1st level, he can
infuse his necromancy spells in either of the following ways.

### Focused Infusion {#focused-infusion}

When the cruoromancer uses this infusion, he adds +1 to the DC of the infused necromancy spell.

### Sickening Infusion {#sickening-infusion}

When the cruoromancer uses this infusion, any creature damaged by the infused necromancy spell
becomes [sickened](ref/misc/sickened) for 1 round.

This ability replaces arcane bond.

## Blood Command (Su) {#blood-command}

At 5th level, a cruoromancer can control up to 5 Hit Dice worth of undead creatures per caster level
instead of the normal 4 Hit Dice of undead when casting the _[animate dead](ref/spell/animate-dead)_
spell. He also gains the following blood infusion ability.

### Commanding Infusion {#commanding-infusion}

When using this infusion with _[animate dead](ref/spell/animate-dead)_, the cruoromancer can create
a number of Hit Dice of undead equal to three times his caster level instead of twice his caster
level.

This ability replaces the 5th-level wizard bonus feat.

## Blood Desecration (Su) {#blood-desecration}

At 10th level, a cruoromancer gains the following blood infusion.

### Desecrating Infusion {#desecrating-infusion}

When the cruoromancer uses this infusion, he can choose to center a
_[desecrate](ref/spell/desecrate)_ effect on himself or a single target of the spell modified by
this infusion (he chooses upon casting). This effect is like the _[desecrate](ref/spell/desecrate)_
spell, but lasts for 1 minute per caster level of the cruoromancer, and does not interact with
altars, shrines, or permanent fixtures that boost the _[desecrate](ref/spell/desecrate)_ effect.
This ability replaces the 10th-level wizard bonus feat.

## Blood Ability (Su) {#blood-ability}

At 15th level, a cruoromancer can choose to scry through a single undead creature he created with a
spell modified by a commanding infusion. The undead creature is treated as if imbued with an
_[arcane eye](ref/spell/arcane-eye)_ spell (caster level equal to the cruoromancer's wizard level).
This ability replaces the 15th-level wizard bonus feat.

## Perfect Infusion (Su) {#perfect-infusion}

At 20th level, a cruoromancer can use his blood infusions without taking damage. This ability
replaces the 20th-level wizard bonus spell.
