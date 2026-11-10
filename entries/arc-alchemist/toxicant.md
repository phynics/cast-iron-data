+++
id = "ref/arc-alchemist/toxicant"
kind = "archetype"
title = "Toxicant"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxicant", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "7"

[fields]
kind = "archetype"
replaces = ["Mutagen", "Persistent mutagen"]
replaces_features = ["mutagen", "persistent-mutagen"]
+++

In lands such as Daggermark and Katapesh where poisons are legal and may be openly studied and sold,
some alchemists obsess over the myriad ways that poisons and venoms can be applied and delivered.
Known as toxicants, these deadly artists induce the production of deadly secretions within their own
bodies in order to better inflict crippling conditions upon their foes.

**Toxic Secretion (Ex)**

**Ability:** Once per day, in a process that takes 10 minutes, the toxicant can create and imbibe a
tincture that causes her skin to secrete a mild toxin. The toxicant is immune to this secretion, but
any creature that hits her with a natural attack or unarmed strike must succeed at a Fortitude save
(DC = 10 + [half](ref/misc/fractions-and-rounding) the toxicant's alchemist level + the toxicant's
Intelligence modifier). On a failed save, the target takes an amount of damage equal to the
toxicant's Intelligence modifier. This is a poison effect.

**Flavor:** A toxicant has learned to mimic creatures with the ability to secrete harmful toxins
through the skin.

**At 12th Level:** The toxicant chooses a fourth choice from the previous lists, or can replace
_fatigued_ with [exhausted](ref/misc/exhausted).

**At 15th Level:** The toxicant chooses a fifth choice from the previous options.

**At 18th Level:** The toxicant chooses a sixth choice from the previous options, or can replace
_exhausted **and** staggered_ with [stunned](ref/misc/stunned).

**At 3rd Level:** The toxicant can choose a condition to have her toxin impose. Once this choice is
made, it can't be changed. A creature that fails its save against the toxic secretion also gains
this condition until it succeeds at a save against the secretion, or until the toxin's duration
ends. The initial list of conditions is: [bleed](ref/rule/bleed) (1d6), [dazzled](ref/misc/dazzled),
[fatigued](ref/misc/fatigued), or [sickened](ref/misc/sickened). At higher alchemist levels, the
toxicant gains access to stronger conditions; some replace lower-level conditions, which must be
selected first.

**At 4th Level:** A target that fails its save must succeed at a second save 1 round later or take
the same amount of damage again. This effect repeats as long as the target continues to fail its
saving throws, to a maximum number of rounds equal to 1 + 1 for every 4 alchemist levels the
toxicant possesses (to a maximum of 6 rounds at 20th level).

**At 6th Level:** The toxicant gains a second condition that her toxin imposes. She can choose from
the previous list, or [dazed](ref/misc/dazed) or [shaken](ref/misc/shaken).

**At 9th Level:** The toxicant chooses a third condition from the previous lists, or can replace
_dazzled_ with [blinded](ref/misc/blinded), or _dazed_ with [staggered](ref/misc/staggered).

**Gained:** At 1st Level

**Replaces:** Mutagen

**Standard:** The toxicant can suppress this secretion, in which case it remains suppressed for 1
hour or until the toxicant reactivates it (also a **standard action**).

**Swift:** The toxicant can collect and concentrate this secretion into a poison she can deliver as
a touch attack or apply to a weapon. Targets of such attacks must attempt saving throws as if they
had touched the toxicant's toxic secretion. The toxicant can do this a number of times per day equal
to her alchemist level + her Intelligence modifier.

**Toxic Digestion (Ex)**

**Gained:** At 14th Level

**Replaces:** Persistent mutagen

**Special:** The alchemist can maintain only a single digested poison at a time. If she digests a
new poison, any older digested poison is lost.

**Standard:** A toxicant can drink a poison and suspend it within her own body. She is not affected
by the poison, and doesn't need to attempt saving throws against it. When the toxicant next uses her
toxic secretion on a creature that attacks her with a natural or unarmed attack, she can expose the
attacker to the digested poison (with that poison's normal duration, effects, and save DC) rather
than her normal toxic secretion, even if the digested poison isn't normally a contact poison.
