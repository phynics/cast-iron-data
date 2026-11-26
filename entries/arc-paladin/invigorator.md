+++
id = "ref/arc-paladin/invigorator"
kind = "archetype"
title = "Invigorator"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Invigorator"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invigorator", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "healers-handbook"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "bestow-hope", level = 1 },
  { anchor = "holy-fount", level = 11 },
  { anchor = "champion-of-life", level = 20 },
]
trades = [
  { replaces = "Smite evil", feature = "smite-evil", by = ["bestow-hope"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["holy-fount"] },
  { replaces = "Holy champion", feature = "holy-champion", by = ["champion-of-life"] },
]
+++

Invigorators devote themselves to keeping their allies bodily whole. These selfless paladins believe
the best way to combat evil is by bolstering the health and spirits of those who fight alongside
them. They play vital roles and often command troops among martial faiths, such as those of
[Iomedae](ref/faith/iomedae) and [Torag](ref/faith/torag).

## Bestow Hope (Su) {#bestow-hope}

Beginning at 1st level, an invigorator is a champion of her faith who can call upon her deity's holy
power to bathe battling allies in protective energy. As a swift action during combat, the
invigorator can choose a number of nonevil allies within sight equal to her Charisma modifier upon
whom to bestow hope. Once activated, bestow hope grants the invigorator and these allies DR 1/—
until the combat ends, at which point the [damage reduction](ref/rule/damage-reduction) immediately
ends.

During a battle, the invigorator can change the allies this ability affects as a swift action.
Ending it is a free action, but each time it is activated during a single combat, another use of the
ability is expended. The invigorator can use this ability a number of times per day equal to 3 + her
Charisma modifier.

The invigorator must participate in the combat to use this ability. If she is frightened, panicked,
paralyzed, stunned, unconscious, or otherwise prevented from participating in the combat, any DR
this ability bestows is temporarily suspended until she can participate in the combat again; this
doesn't count as ending the ability.

At 4th level, and at every 3 paladin levels thereafter, the DR this ability grants increases by 1,
to a maximum of DR 7/— at 19th level.

The DR this ability grants does not stack with the DR the invigorator receives from aura of
righteousness or holy champion. However, at both 7th level and 20th level, an invigorator can choose
to bestow hope upon an additional ally, for a total number of allies equal to 2 + the invigorator's
Charisma modifier at 20th level.

This ability replaces smite evil.

## Holy Fount (Su) {#holy-fount}

At 11th level, an invigorator can expend two uses of bestow hope to radiate healing energies to
bolster her nearby allies. For a number of rounds equal to 1/2 the invigorator's paladin level, the
invigorator and all nonevil allies within a 10-foot radius of her gain
[fast healing](ref/umr/fast-healing) 10. This ability is an aura centered on the invigorator; allies
must be within the aura at the beginning of their turns to benefit from the
[fast healing](ref/umr/fast-healing). Using this ability is a free action.

This ability replaces aura of justice.

## Champion of Life (Sp) {#champion-of-life}

An invigorator's holy resolve can sometimes overcome death—or smite the horror that is undeath. At
20th level, three times per day as a standard action, an invigorator can use
_[breath of life](ref/spell/breath-of-life)_ as a
[spell-like ability](ref/umr/spell-like-abilities), using her paladin level as her caster level.

Creatures brought back to life with this ability do not suffer the normal temporary negative level
the spell imposes.

This ability replaces holy champion.
