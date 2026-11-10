+++
id = "ref/arc-alchemist/plague-bringer"
kind = "archetype"
title = "Plague Bringer"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Plague%20Bringer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plague_bringer", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "advanced-race-guide"
page = "153"

[fields]
kind = "archetype"
replaces = ["Mutagen", "Poison resistance", "poison immunity"]
replaces_features = ["mutagen", "poison-resistance"]
+++

The plague bringer sees disease as the ultimate weapon, and has worked tirelessly to master new
diseases and disease-delivery systems. A plague bringer feels no more remorse at unleashing his
armaments on his enemies than an archer does when firing an arrow in the heat of battle. Disease is
a tool, and the plague bringer is its master. A plague bringer has the following class features.

**Prerequisites:** Ratfolk

**Plague Vial (Su)**

**Ability:** As a **standard action**, the plague bringer can infect a weapon with this sickness
(typically by licking it or wiping his blood or pus on it). The disease on the weapon works like a
poisoned weapon, except the source is a disease instead of a poison (so a dwarf's resistance to
poison does not apply).

**Flavor:** A plague bringer can create a plague vial, an alchemically grown and concentrated
disease sample.

**Info:** It takes 1 hour to prepare a plague vial, and once prepared, the vial remains potent until
used. A plague bringer can only maintain 1 plague vial at a time - if he prepares a second vial, any
existing plague vial becomes inert. A plague vial that is not in a plague bringer's possession
becomes inert until a plague bringer picks it up again.

**Gained:** At 1st Level

**Replaces:** Mutagen

**Special:** The plague bringer is immune to the effect of his own plague vial, but not that of
another's plague vial. The effects of multiple plague vials do not stack. Unless he learns how to
brew a mutagen by taking the [mutagen](ref/discovery/mutagen) discovery, he can never benefit from a
mutagen and reacts to it as if he were a non-alchemist. At any particular time, a plague bringer can
only be under the effect of either a plague vial or a mutagen (not both); drinking another
immediately ends the effects of any ongoing plague vial or mutagen. All limitations to mutagens
apply to plague vials as if they were the same substance. The
[infuse mutagen](ref/discovery/infuse-mutagen) discovery and _persistent mutagen_ class ability
apply to plague vials. The [sticky poison](ref/discovery/sticky-poison) discovery applies to a
weapon infected with a plague vial. The plague vial is a disease effect.

**Standard:** A plague bringer can drink a plague vial. Anyone other than a plague bringer
(including another alchemist) who drinks a plague vial must make a saving throw against the vial's
DC or become [nauseated](ref/misc/nauseated) for 1 hour. Upon being imbibed, the plague vial infects
the plague bringer's blood, sweat, tears, and other bodily fluids for 10 minutes per class level.
Any creature that harms him with melee attacks (except with reach weapons) must make a Fortitude
save (DC 10 + [half](ref/misc/fractions-and-rounding) the plague bringer's level + the plague
bringer's Intelligence modifier) or become [sickened](ref/misc/sickened) for 1 round per plague
bringer level.

**Disease Resistance (Ex)**

**At 10th Level:** A plague bringer becomes completely immune to disease (including magical
diseases).

**At 5th Level:** This bonus increases to +4.

**At 8th Level:** This bonus increases to +6.

**Gained:** At 2nd Level

**Passive:** A plague bringer gains a +2 bonus on all saving throws against disease.

**Replaces:** Poison resistance, poison immunity

**Discoveries:** The following discoveries complement the plague bringer archetype:
[explosive bomb](ref/discovery/explosive-bomb), [precise bombs](ref/discovery/precise-bombs),
[smoke bomb](ref/discovery/smoke-bomb), [breath weapon bomb](ref/discovery/breath-weapon-bomb),
[fast bombs](ref/discovery/fast-bombs), [nauseating flesh](ref/discovery/nauseating-flesh);
[plague bomb](ref/discovery/plague-bomb).
