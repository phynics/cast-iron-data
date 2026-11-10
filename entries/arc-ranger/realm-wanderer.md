+++
id = "ref/arc-ranger/realm-wanderer"
kind = "archetype"
title = "Realm Wanderer"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Realm%20Wanderer"
source_ids = ["distant-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "realm_wanderer", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "distant-realms"
page = "22"

[fields]
kind = "archetype"
replaces = ["Track", "Swift tracker", "Master hunter"]
alters = ["Hunter's bond"]
replaces_features = ["track", "swift-tracker", "master-hunter"]
alters_features = ["hunter-s-bond"]
+++

Some of the most free-roaming rangers are those who tread between locales so varied that they may as
well be separate worlds altogether - and quite often these disparate places are literally
[Hell](ref/rule/hell) and the Material Plane. Like the Queen of Dis, whom many of them admire, these
rangers take to heart the lessons they've learned from their vastly contrasting experiences and know
that creatively embracing this wisdom is sometimes the difference between life and death.

**Gained class skills:** diplo, bluff

**Lost class skills:** intm, stl

**Deceptive Subtlety (Ex)**

**Ability:** A realm wanderer adds half his level (minimum 1) to Diplomacy checks to influence a
creature's attitude, to make requests of creatures, and for similar uses of the skill. He also adds
half his level (minimum 1) to Bluff checks to deceive, lie, or convey secret messages.

**Replaces:** Track

**Queen's Bond (Ex)**

**Action:** Ability

**Alters:** Hunter's bond

**Gained:** At 4th Level

A realm wanderer must choose an animal companion for his _hunter's bond._ This animal companion
gains the [fiendish](ref/template/fiendish) template, likely either due to time it spent near a gate
to Hell or due to infernal influences in its place of birth. Due to this insidious influence, this
[animal companion](ref/sidekick/animal-companion) always takes a penalty on attack rolls equal to
[one-fifth](ref/misc/fractions-and-rounding) of the realm wanderer's level (minimum 1).

If the realm wanderer releases his animal companion from service or it perishes, he can gain a new
fiendish animal companion by completing the required ceremony. Alternatively, when the realm
wanderer releases his animal companion or it dies in his service, he can use his influence over its
fiendish nature to cause the animal to lose the fiendish template. If the animal companion is then
raised or otherwise brought back from the dead after the realm wanderer removes its fiendish
template, the animal companion no longer takes the penalty on attacks described above. (He cannot,
however, gain a new non-fiendish animal companion by completing the ceremony to replace an animal
companion.)

**Dual Master (Ex)**

**Gained:** At 8th Level

**Passive:** The realm wanderer's bonuses from _deceptive subtlety_ are doubled when he is in either
of his two _favored terrain_ types. However, this benefit applies only to the first two _favored
terrain_ types he selected; as he gains additional _favored terrains_ at higher levels, this benefit
does not apply in those additional terrain types.

**Replaces:** Swift tracker

**Shrewdest Monarch (Su)**

**Flavor:** The realm wanderer has become a true master of the territories with which he is
familiar.

**Gained:** At 20th Level

**Passive:** The realm wanderer also gains a bonus on attack rolls equal to his Wisdom modifier
against creatures that have successfully learned his alignment (using
[detect chaos/evil/good/law](ref/spell/detect-evil), as appropriate, or similar effects).

**Replaces:** Master hunter

**Standard:** He can make a single attack at his full attack bonus against an enemy in one of the
terrains chosen using the _dual master_ ability. If the attack hits, the target takes damage
normally and must succeed at a Fortitude saving throw or die. The DC of this saving throw is equal
to 10 + half the realm wanderer's level + his Wisdom modifier. A realm wanderer can instead deal an
amount of nonlethal damage equal to the creature's current hit points; the target can attempt a
Fortitude save at the same DC to negates this damage.

**Usage:** Four times/day, but not against the same creature more than once in a 24-hour period

**Usage:** Four times/day, but not against the same creature more than once in a 24-hour period
