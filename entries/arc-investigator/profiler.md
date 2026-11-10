+++
id = "ref/arc-investigator/profiler"
kind = "archetype"
title = "Profiler"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "profiler", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "horror-adventures"
page = "55"

[fields]
kind = "archetype"
replaces = ["Trapfinding", "poison lore", "trap sense", "Poison resistance", "poison immunity", "Swift alchemy", "Investigator talent at 7th level"]
replaces_features = ["trapfinding", "poison-lore", "trap-sense", "poison-resistance", "swift-alchemy"]
+++

Profilers understand the human psyche to an intense degree, allowing them to predict the criminals
they hunt.

**Expert Profiler (Ex)**

**At 1st Level:** A profiler gains a bonus equal to 1/2 his class level (minimum +1) on Sense Motive
checks.

**At 2nd Level:** He can use _inspiration_ on any Sense Motive check without expending a use of
_inspiration,_ provided he is trained in the skill.

**At 3rd Level:** He can attempt to predict a creature's movements using his knowledge of the
creature's psychology. He can use this ability only on a creature familiar to him (for example, a
[serial killer](ref/arc-vigilante/serial-killer) whose crimes the profiler has studied will suffice,
even if the profiler hasn't yet identified the serial killer's true identity). To do so, he starts
from a place where he knows that the creature has been and why (most often the scene of a crime) and
attempts a Sense Motive check against a DC equal to 40 or to 20 + the creature's Bluff modifier,
whichever is higher, which the GM rolls in secret. On a failure, the profiler's guess about the
creatures movements is inaccurate. On a success, the profiler is able to track the creature's
general movements as if using Survival to track (though the usual modifiers on Survival checks to
track don't apply, and this ability allows her to track a creature using pass without trace or
otherwise leaving no trail). After at most 1 hour (or sooner if there are many possible options for
the creature to take, at the GM's discretion), if the profiler has not yet found further evidence of
the creature's passing (such as footprints, fingerprints, or any other indication that the creature
came this way), he loses track of the creature's movements; if he does, he can try to guess where
the creature went next by attempting another check.

**Replaces:** Trapfinding, poison lore, trap sense

**Divination Analysis (Su)**

**Ability:** A profiler has analyzed the workings of the mind. His caster level to determine the
duration of his divination extracts increases by 1, and he gains a +1 bonus on saving throws against
divinations.

**At 11th Level:** A profiler can expend one use of _inspiration_ to add 1d6 to the result of a
[concentration](ref/rule/concentration) check when using a divination extract or investigator
[spell-like ability](ref/umr/spell-like-abilities).

**At 5th Level:** The increases to caster level becomes 2 and the bonus on saving throws increases
to +2.

**At 8th Level:** These increase to 3 and +3, respectively.

**Gained:** At 2nd Level

**Replaces:** Poison resistance, poison immunity

**Blood Sleuth (Sp)**

**Ability:** A profiler can expend one use of his _inspiration_ to use
[discern next of kin](ref/spell/discern-next-of-kin) as a
[spell-like ability](ref/umr/spell-like-abilities). Alternatively, he can expend two uses of
_inspiration_ to use [blood biography](ref/spell/blood-biography) as a spell-like ability.

**Gained:** At 4th Level

**Replaces:** Swift alchemy

**Pack Psychology (Su)**

**Gained:** At 7th Level

**Passive:** A profiler can understand the way that groups act together, allowing him to exploit the
vulnerabilities in their attacks. A profiler can't be [flanked](ref/rule/flanking) by creatures with
an Intelligence score and he gains a +1 bonus to his AC against such creatures when they would
otherwise flank him, as he plays their movements against each other.

**Replaces:** Investigator talent at 7th level
