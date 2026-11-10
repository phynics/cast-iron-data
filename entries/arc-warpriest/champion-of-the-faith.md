+++
id = "ref/arc-warpriest/champion-of-the-faith"
kind = "archetype"
title = "Champion of the Faith"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Champion%20of%20the%20Faith"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "champion_of_the_faith", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-guide"
page = "128"

[fields]
kind = "archetype"
replaces = ["Bonus feat gained at 3rd level", "Channel energy"]
alters = ["Sacred weapon"]
replaces_features = ["channel-energy"]
alters_features = ["sacred-weapon"]
+++

Champions of the faith are crusaders who use the power of their divine patron to annihilate the
faith's enemies.

**Chosen Alignment**

**Choice:** A champion of the faith must select one of the following as his chosen alignment: chaos,
evil, good, or law. This choice must be one of the alignments shared by the champion of the faith
and his deity. Champions of the faith who are neutral with no other alignment components (or whose
deity is) can choose any of the above alignments for this purpose. Additionally, a champion of the
faith must select the blessing corresponding to his chosen alignment, even if it's not on his
deity's list of domains.

His chosen alignment's opposite is referred to as his opposed alignment. Good and evil oppose one
another, just as law and chaos oppose one another.

**Gained:** At 1st Level

**Sacred Weapon (Su)**

**Alters:** Sacred weapon

**At 12th Level:** Once per day as a **swift action**, a champion of the faith can enhance any one
_sacred weapon_ with a weapon special ability based on his chosen alignment
([anarchic](ref/magic-enh/anarchic) for chaos, [unholy](ref/magic-enh/unholy) for evil,
[holy](ref/magic-enh/holy) for good, and [axiomatic](ref/magic-enh/axiomatic) for law). This effect
lasts for 1 minute.

**At 16th Level:** He can use this ability twice a day.

**At 20th Level:** He can use this three times a day.

**At 4th Level:** Any _sacred weapon_ wielded by a champion of the faith counts as having his chosen
alignment for the purposes of overcoming [damage reduction](ref/rule/damage-reduction).

**Info:** A champion of the faith gains the _sacred weapon_ class feature as normal. However, this
ability does not grant the 4th-level ability to enhance the champion of the faith's weapon with
divine power, nor does it grant any subsequent increases to that ability.

**Gained:** At 1st Level

**Detect Alignment (Sp)**

**Flavor:** A champion of the faith can detect his opposed alignment.

**Gained:** At 3rd Level

**Move:** The champion of the faith can focus on a single item or creature within 60 feet and
determine whether it possesses his opposed alignment, as
[detect chaos/evil/good/law](ref/spell/detect-evil), learning the strength of the aura as if he had
studied it for 3 rounds. The champion of the faith does not detect alignment in any other object or
creature when using this ability in this way.

**Replaces:** Bonus feat gained at 3rd level

**Smite (Su)**

**Flavor:** A champion of the faith can focus his powers against his chosen foes.

**Gained:** At 4th Level

**Replaces:** Channel energy

**Special:** Using this ability consumes two uses of his _fervor_ ability.

**Swift:** The champion of the faith chooses one target within sight to _smite._ If this target is
of his opposed alignment, the champion of the faith adds his Charisma bonus (if any) to his attack
rolls and adds his warpriest level to all damage rolls made against the target of his _smite._ If
the target of his _smite_ is an [outsider](ref/type/outsider) with the subtype corresponding to his
opposed alignment, the bonus to damage on the first successful attack increases to 2 points of
damage per warpriest level the champion of the faith possesses. Regardless of the target, _smite_
attacks automatically bypass any DR the target possesses.

In addition, while _smite_ is in effect, the champion of the faith gains a deflection bonus equal to
his Charisma modifier (if any) to his AC against attacks made by the target of the _smite._ If the
_smite_ targets a creature that's not of the champion of the faith's opposed alignment, the _smite_
is wasted with no effect.

The _smite_ effect remains until the target of the _smite_ is dead or the next time the champion of
the faith regains spells.

**Usage:** 1 time/day per 4 warpriest levels
