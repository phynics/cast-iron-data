+++
id = "ref/rule/drowning-aa"
kind = "rule"
title = "Drowning"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drowning_aa", path = "json/rules_campaign_types01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Aquatic Adventures\
Drowning is one of the most obvious dangers of underwater adventuring. As creature can typically
hold its breath for a number of rounds equal to twice its Constitution score. Whenever a creature
takes a standard or full-round action, it expends 1 additional round of breath, so practically
speaking, if a creature wants to fight or double move each round, it can do so only for a number of
rounds equal to its Constitution score. Intentionally exhaling breath expends 1 to 3 rounds for each
exhaling action - generally 1 round for a small exhalation, and 3 rounds for an extended exhalation
like singing a song or casting a spell. Certain magic, like the [suffocation](ref/spell/suffocation)
spell, can expel all of a creature's held breath.

Once a creature has used up these rounds of safety, it lives on a knife's edge between life and
death. Each round, the creature must succeed at a Constitution check, with a DC starting at 10 and
increasing by 1 each round after the first. Once it fails this check, the creature begins to drown,
falling unconscious (and dropping to 0 hit points if it currently had more), dropping to -1 hit
points on the next round, and dying on the round after that. At any point, if the creature becomes
able to breathe (perhaps because someone dragged it out of the water or cast a spell to assist it),
it ceases drowning but doesn't regain any lost hit points. Note that if a creature holds its breath
in a situation where it could normally breathe, it won't fall unconscious if it fails its
Constitution check.

Because of the prohibitive limitations of holding one's breath, underwater explorers from the
surface use a variety of techniques to extend their ability to breathe underwater. The most common
is [water breathing](ref/spell/water-breathing), which is extremely long-lasting and can protect an
entire group with one casting. A simpler, short-term solution is [air bubble](ref/spell/air-bubble),
which can protect a single creature for a few minutes - but not usually enough for an underwater
adventure. The most powerful option is [life bubble](ref/spell/life-bubble); while its duration is
half that of water breathing, it also protects against many other underwater hazards such as extreme
temperature and pressure. Those who prefer a mundane alternative to ephemeral (and dispellable)
magic tend to use [air tanks](ref/eq-misc/air-tank-pressurized) to store additional air, but
characters hoping to stay underwater find that carrying around more than a few extra breaths of air
sets their buoyancy to swiftly rising, almost like wearing a giant life preserver, so this solution
is effective only for a strong swimmer or someone with access to magic to alter buoyancy.
