+++
id = "ref/arc-cavalier/vermin-tamer"
kind = "archetype"
title = "Vermin Tamer"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vermin_tamer", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]

[fields]
kind = "archetype"
replaces = ["Expert training", "Demanding challenge"]
alters = ["Mount"]
+++

**Sources:** Heroes of the Darklands pg 17\
Due to the strange terrain, the lack of sunlight, and numerous other hazards, keeping a traditional
mount in the Darklands can prove difficult. Cavaliers native to or traveling the region may choose
to tame local creatures instead. Those who can overcome their revulsion and distrust of Sekamina's
strange fauna often find that such partnerships with native creatures serve both rider and mount
well. While these mounts may be harder to handle than typical mounts, their versatility and
adaptations prove indispensable.

**Darklands Mount (Ex)**

**Action:** Ability

**Alters:** Mount

**Gained:** At 1st Level

A vermin tamer chooses a creature native to the Darklands as his mount. This functions as a
cavalier's mount. He can choose a [giant beetle](ref/companion/beetle-giant),
[giant centipede](ref/companion/centipede-giant), [giant gecko](ref/companion/lizard-giant-gecko),
[giant slug](ref/companion/slug-giant), or [giant spider](ref/companion/spider-giant) as his mount.
These mounts (except the giant gecko) and the rules for vermin companions are detailed here, under
Vermin Companions.

The selected mount is combat trained. The vermin trainer does not take an armor check penalty on
Ride checks while riding his mount. If the vermin tamer's starting mount is large enough to act as a
mount, it gains [Light Armor Proficiency](ref/feat/armor-proficiency-light) as a bonus feat. If the
selected animal companion is too small to act as a proper mount, then the vermin tamer gains
[Undersized Mount](ref/feat/undersized-mount) as a bonus feat.

**Stuck in the Saddle (Ex)**

**Flavor:** A practiced vermin tamer can remain steady in the saddle even in unconventional
situations.

**At 4th Level:** He gains a +4 circumstance bonus on any checks to stay in the saddle when his
mount is climbing walls or flying.

**At 8th Level:** This bonus increases to +8, and he never falls off his mount when he is rendered
unconscious.

**Replaces:** Expert training

**Disorienting Challenge (Ex)**

**Gained:** At 12th Level

**Passive:** Whenever a vermin tamer declares a _challenge,_ he can confound his target with the
erratic movements of his mount. As long as the vermin tamer begins his turn mounted, with his mount
climbing or flying at a higher location than his target, the target of his _challenge_ takes a -2
penalty to its AC.

**Replaces:** Demanding challenge
