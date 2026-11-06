+++
id = "ref/arc-fighter/armor-master"
kind = "archetype"
title = "Armor Master"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "armor_master", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Combat pg 44\
All fighters have two main tools of their trade: weapons and armor. While many fighters hone their
weapon skills to a point of inescapable grace and lethality, there are those who live under the
maxim that a good offense can be accomplished though an impenetrable defense. To these fighters,
proper use of armor and shields ensures that they can fight another day, and that the frustration of
enemies who can't seem to crack an armor master's superior defenses is just the first symptom of his
foes' eventual defeat.

**Deflective Shield (Ex)**

**Flavor:** An armor master specializes in using his shield to deflect attacks.

**Gained:** At 2nd Level

**Passive:** He gains a +1 bonus to his touch AC, and this bonus increases for every four levels
beyond 2nd (+2 at 6th level, +3 at 10th level, +4 at 14th level, and finally +5 at 18th level);
however, this bonus cannot exceed the sum of the armor and enhancement bonus to AC provided by the
shield that the armor master is currently carrying.

**Replaces:** Bravery

**Armored Defense (Ex)**

**At 19th Level:** This [damage reduction](ref/rule/damage-reduction) increases to DR 4/- when
wearing light armor, DR 8/- when wearing medium armor, and DR 12/- when wearing heavy armor.

**Gained:** At 5th Level

**Passive:** An armor master gains DR 1/- when wearing light armor, DR 2/- when wearing medium
armor, and DR 3/- when wearing heavy armor.

**Replaces:** Weapon training 1 and 3, armor mastery

**Special:** This [damage reduction](ref/rule/damage-reduction) stacks with that provided by
[adamantine](ref/eq-material/adamantine) armor, but not with other forms of damage reduction. This
damage reduction does not apply if the armor master is stunned, unconscious, or helpless.

**Fortification (Ex)**

**Flavor:** An armor master can use his armor to shield critical areas from injury.

**At 13th Level:** His armor gains the
[moderate fortification](ref/magic-enh/fortification-moderate) special ability.

**Gained:** At 9th Level

**Passive:** He treats any armor he wears as if it had the
[light fortification](ref/magic-enh/fortification-light) special ability.

**Replaces:** Weapon training 2 and 4

**Special:** This fortification does not stack in any way with armor that has these special
abilities. In these cases the armor master takes the better of the two fortifications.

**Indestructible (Ex)**

**Gained:** At 20th Level

**Passive:** An armor master gains complete immunity to critical hits and sneak attacks while he is
wearing armor. In addition, unless his armor has the [fragile](ref/misc/fragile) armor quality, it
cannot be [sundered](ref/rule/sunder) while he is wearing it.

**Replaces:** Weapon mastery
