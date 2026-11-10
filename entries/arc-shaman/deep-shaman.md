+++
id = "ref/arc-shaman/deep-shaman"
kind = "archetype"
title = "Deep Shaman"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deep_shaman", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "aquatic-adventures"
page = "51"

[fields]
kind = "archetype"
replaces = ["Elemental form of the true spirit ability"]
alters = ["Spirit", "spirit animal", "Hexes", "Spirit ability", "greater spirit ability"]
alters_features = ["spirit", "spirit-animal"]
+++

While most shamans of the _waves_ spirit have powers associated with surface waters, deep shamans
are tied to spirits from the depths. Some say that the first deep shamans served
[Besmara](ref/faith/besmara) back when she was a water spirit, before she achieved full godhood.

**Deep Spirit**

**Alters:** Spirit, spirit animal

**Info:** A deep shaman must choose the [waves](ref/shamanspirit/waves) spirit. The deep shaman must
choose a spirit animal with the [aquatic](ref/subtype/aquatic) subtype, and it gains the
[amphibious](ref/umr/amphibious) special quality instead of gaining the ability to breathe in water.

**Gained class skills:** swim

**Aquatic Hexes (Su)**

**Ability:** When a deep shaman uses _beckoning chill_ on a creature in the water, that creature
becomes [fatigued](ref/misc/fatigued) due to hypothermia for the duration, and it also becomes
[entangled](ref/rule/entangled) if the creature takes damage from the deep shaman's spirit abilities
and from spells and abilities with the water descriptor.

**Ability2:** Her _crashing waves_ hex applies to her spirit abilities that deal damage as if they
were spells with the water descriptor, raising her effective shaman level for those abilities.

**Alters:** Hexes

**Special:** Instead of _mist's shroud_ and _watersight,_ she can select the two hexes below.

**Buoyancy Control (Sp)**

**Ability:** The deep shaman touches a willing creature and changes its
[buoyancy](ref/rule/buoyancy) to whichever of the five states she wishes for 1 minute. A creature
affected by this hex can't be affected by it again for 24 hours.

**Passive:** The deep shaman has neutral buoyancy, regardless of what her normal buoyancy would be,
though she can end or resume the effect as a **standard action**.

**Deep Heart (Su)**

**Ability:** The deep shaman gains the ability to breathe underwater and gains a swim speed equal to
her unmodified base land speed.

**At 8th Level:** She takes only half the normal amount of [pressure damage](ref/rule/water-dangers)
and she [adjusts to a new pressure](ref/rule/oceanic-zones) all at once after succeeding at five
Fortitude saves, rather than 100 feet at a time.

**Aquatic Spirit Abilities (Su)**

**Ability:** When used underwater, a deep shaman's _wave strike_ deals lethal bludgeoning damage and
pushes the target away 5 feet + an additional 5 feet for every 6 shaman levels she has.

**Alters:** Spirit ability, greater spirit ability

**At 11th Level:** Whenever the deep shaman is underwater, all weapons she holds are treated as if
they had the [impact](ref/magic-enh/impact) special ability instead of
[quenching](ref/magic-enh/quenching). Instead of a swim speed and the ability to breathe underwater,
_fluid mastery_ provides [tremorsense](ref/umr/tremorsense) with a range of 30 feet while in the
water, and when underwater, _fluid mastery's_ torrent deals 1d6 points of damage per shaman level in
a 30-foot cone.

**Brine Dragon Form (Su)**

**Ability:** When a deep shaman gains access to the _true_ version of the waves spirit, she can
assume the form of a Large (or smaller) [brine dragon](ref/family/dragon-primal-brine) as per
[form of the dragon II](ref/spell/form-of-the-dragon-2), with a line of acid breath weapon, acid
resistance 20, and a swim speed of 60 feet.

**At 18th Level:** She can assume the form of a Huge or smaller brine dragon as per
[form of the dragon III](ref/spell/form-of-the-dragon-3) instead.

**Replaces:** Elemental form of the true spirit ability

**Usage:** She can use this ability for 1 hour per shaman level each day, divided any way she
chooses in 1 hour increments, though the spell's breath weapon limit applies across the whole day.
Time she spends underwater doesn't count against this limit, but every minute (or fraction thereof)
that she spends flying expends 1 hour of her daily uses.

**Usage:** She can use this ability for 1 hour per shaman level each day, divided any way she
chooses in 1 hour increments, though the spell's breath weapon limit applies across the whole day.
Time she spends underwater doesn't count against this limit, but every minute (or fraction thereof)
that she spends flying expends 1 hour of her daily uses.
