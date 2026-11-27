+++
id = "ref/arc-antipaladin/knight-of-the-sepulcher"
kind = "archetype"
title = "Knight of the Sepulcher"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Knight%20of%20the%20Sepulcher"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "knight_of_the_sepulcher", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "ultimate-combat"
page = "64"

[fields]
kind = "archetype"
features = [
  { anchor = "touch-of-the-crypt", level = 5 },
  { anchor = "fortitude-of-the-crypt", level = 8 },
  { anchor = "cloak-of-the-crypt", level = 10 },
  { anchor = "will-of-the-crypt", level = 11 },
  { anchor = "weapons-of-sin", level = 14 },
  { anchor = "crypt-lord", level = 15 },
  { anchor = "soul-of-the-crypt", level = 17 },
  { anchor = "undying-champion", level = 20 },
]
trades = [
  { replaces = "Fiendish boon", feature = "fiendish-boon", by = ["touch-of-the-crypt"] },
  { replaces = "Aura of despair", feature = "aura-of-despair", by = ["fortitude-of-the-crypt"] },
  { replaces = "The smite good use gained at 10th level", feature = "smite-good", levels = [10], by = ["cloak-of-the-crypt"] },
  { replaces = "Aura of vengeance", feature = "aura-of-vengeance", by = ["will-of-the-crypt"] },
  { replaces = "Aura of sin", feature = "aura-of-sin", by = ["weapons-of-sin"] },
  { replaces = "Cruelty", feature = "cruelty", by = ["crypt-lord"] },
  { replaces = "Aura of depravity", feature = "aura-of-depravity", by = ["soul-of-the-crypt"] },
  { replaces = "Unholy champion", feature = "unholy-champion", by = ["undying-champion"] },
]
+++

Not content with the antipaladin's mere corruption of the soul, the knight of the sepulcher
sacrifices mortality along with morality.

The knight of the sepulcher archetype is available only to the antipaladin alternate class.

## Touch of the Crypt (Ex) {#touch-of-the-crypt}

At 5th level, a knight of the sepulcher gains a +2 bonus on saving throws against mind-affecting
effects, death effects, and poison. He is harmed by positive energy effects and healed by negative
energy effects as though he were undead, although negative energy effects that don't heal undead
(such as [enervation](ref/spell/enervation)) affect him normally. The knight of the sepulcher has a
25% chance of ignoring critical hits and the bonus damage from
[sneak attacks](ref/ability/sneak-attack) as though he were wearing _armor of light fortification_.
This ability replaces the fiendish boon ability.

## Fortitude of the Crypt (Ex) {#fortitude-of-the-crypt}

At 8th level, a knight of the sepulcher gains immunity to poison. He also gains
[darkvision](ref/rule/darkvision) 60 feet if he does not already possess it. This ability replaces
the aura of despair ability.

## Cloak of the Crypt (Ex) {#cloak-of-the-crypt}

At 10th level, the knight of the sepulcher gains immunity to energy drain and harmful negative
energy effects. His chance of ignoring critical hits and sneak attacks increases to 50%, as though
he were wearing _armor of moderate fortification_. This ability replaces the smite good use gained
at 10th level.

## Will of the Crypt (Ex) {#will-of-the-crypt}

At 11th level, a knight of the sepulcher's bonus on saving throws against mind-affecting effects and
death effects increases to +4. This ability replaces the aura of vengeance ability.

## Weapons of Sin (Su) {#weapons-of-sin}

At 14th level, a knight of the sepulcher's weapons are treated as evil-aligned for the purposes of
overcoming [damage reduction](ref/rule/damage-reduction). This ability replaces aura of sin.

## Crypt Lord (Ex) {#crypt-lord}

At 15th level, a knight of the sepulcher's chance of ignoring critical hits and sneak attacks
increases to 75%, as though he were wearing _armor of heavy fortification_. He gains immunity to
death effects, paralysis, sleep effects, and stunning. He no longer sleeps. The knight of the
sepulcher also gains immunity to effects that cause fatigue, and effects that would cause him to
become [exhausted](ref/misc/exhausted) instead cause him to become [fatigued](ref/misc/fatigued).
This ability replaces cruelty.

## Soul of the Crypt (Su) {#soul-of-the-crypt}

At 17th level, a knight of the sepulcher gains DR 5/bludgeoning and good. This ability replaces aura
of depravity.

## Undying Champion (Ex) {#undying-champion}

At 20th level, a knight of the sepulcher joins the ranks of the [undead](ref/type/undead). His DR
increases to 10/bludgeoning and good. His type changes to undead, and he acquires all
[undead traits](ref/umr/undead-traits). Although immune to disease, he can still carry and spread
diseases with the antipaladin's plague bringer ability. The undying champion no longer has a
Constitution score. He uses his Charisma score for calculating hit points, Fortitude saves, and any
special abilities that rely on Constitution. This ability replaces unholy champion.
