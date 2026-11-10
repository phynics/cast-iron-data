+++
id = "ref/arc-druid/devolutionist"
kind = "archetype"
title = "Devolutionist"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Devolutionist"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "devolutionist", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "horror-adventures"
page = "50"

[fields]
kind = "archetype"
replaces = ["Resist nature's lure", "Venom immunity"]
alters = ["Nature bond"]
replaces_features = ["resist-nature-s-lure", "venom-immunity"]
alters_features = ["nature-bond"]
+++

Full of simmering hatred toward civilization and those who dwell within it, devolutionists believe
that the world would be better off without any sentient life at all. They transform intelligent
creatures and domesticated animals into throwbacks to their feral ancestors.

**Devolved Companion (Ex)**

**Alters:** Nature bond

**Choice:** A devolutionist must choose a devolved humanoid as an animal companion for her _nature
bond._ Use the stats for an [ape](ref/companion/ape) animal companion.

**At 4th Level:** The devolved humanoid doesn't increase to size Large (it still gains all the other
benefits at 4th level).

**Undomesticate (Su)**

**Ability:** A devolutionist can spend 1 minute with a willing or restrained domesticated animal to
undo the effects of domestication, transforming it into a wild animal and causing it to lose any
tricks it knew. The animal no longer recognizes any humanoids as friends or allies and gladly tears
former playmates apart for food. Handle Animal checks don't work on an undomesticated creature,
though _wild empathy_ does.

**Gained:** At 4th Level

**Replaces:** Resist nature's lure

**Special:** This ability doesn't function on animal companions, special mounts, or the like, and
other exceptional domesticated animals can attempt a Will save (DC = 10 +
[half](ref/misc/fractions-and-rounding) the devolutionist's druid level + her Wisdom modifier) to
negate the effect and become immune to it for 24 hours. Though this ability is instantaneous,
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), or [wish](ref/spell/wish) can reverse the effects.

**Devolution (Sp)**

**Action:** Ability

**Gained:** At 9th Level

**Replaces:** Venom immunity

**Special:** This ability counters and dispels [awaken](ref/spell/awaken), and only _awaken,
miracle,_ or _[wish](ref/spell/wish)_ can reverse it.

A devolutionist can perform a 24-hour ritual to irrevocably transform a humanoid or animal into a
devolved feral state. There is no saving throw, but the target must be present and stay relatively
still for the entire ritual, which typically requires a willing or restrained target. An affected
humanoid's Intelligence score is instantly reduced to 2; its type changes to
[animal](ref/type/animal); it loses all spellcasting and abilities that require intelligence; it
can't wield manufactured weapons; it gains two [claw attacks](ref/umr/natural-attacks) and a bite
attack (all dealing 1d4 points of damage for a Medium humanoid or 1d3 for Small humanoids); and it
can't use skills other than Acrobatics, Climb, Escape Artist, Fly, Intimidate, Perception, Stealth,
Survival, and Swim.

An affected animal is _undomesticated_ (see above) if applicable and then either gains the
[advanced](ref/template/advanced) template, except without any increases to mental ability scores,
or becomes a dire version of the animal (if a dire version exists and at the GM's discretion). The
devolved creature starts out friendly toward the devolutionist, though it typically tries to kill
and devour other sentient humanoids. The devolutionist has no special empathy or connection with a
creature she devolves, and if it was her animal companion before, it ceases to be so. The druid can
communicate her desires to a devolved creature using _wild empathy._
