+++
id = "ref/arc-slayer/covenbane"
kind = "archetype"
title = "Covenbane"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "covenbane", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "26"

[fields]
kind = "archetype"
replaces = ["Track", "Slayer talent gained at 2nd level", "Stalker", "Swift tracker"]
alters = ["Studied target"]
+++

Covenbane slayers are scarred by arcane magic at a young age, and that resonance gives them
supernatural insight into the psychic bonds between others. They are adept at fighting tight-knit
groups, exploiting their connections to hunt and wound teams. The churches of
[Iomedae](ref/faith/iomedae) and [Milani](ref/faith/milani) in particular dispatch special agents to
rescue hexed children from Irrisen, Razmiran, and other lands plagued by abusive arcanists and then
raise them in this deadly art.

**Hag Sense (Su)**

**Ability:** He can also use his _hag sense_ to recognize whether someone within 30 feet of him is
using magic to hide her true form. To do this, he must succeed at a Perception check against a DC
equal to 15 + the target's CR; success indicates the presence of a magical disguise, but it does not
reveal the creature's true form.

**Passive:** A covenbane's magical scars throb in the presence of magic. A covenbane adds half his
level (minimum +1) on Perception, Sense Motive, and Survival checks to identify, recognize, or track
a [hag](ref/family/hag), arcane spellcaster, or creature with
[spell-like abilities](ref/umr/spell-like-abilities).

**Replaces:** Track

**Studied Coven (Su)**

**Ability:** A covenbane can designate an entire coven as his _studied target_ by studying any
single member. He applies his _studied target_ bonus against all members of the studied creature's
coven, and all members of the coven count as one target for the purposes of determining the maximum
number of _studied targets_ a slayer can maintain. This bonus remains even if one or more members of
the coven die after the covenbane studies them.

**Alters:** Studied target

**At 7th Level:** The covenbane can designate other magically linked creatures, such as those bound
by a [hivemind](ref/template/hivemind-swarm) or a [telepathic bond](ref/spell/telepathic-bond)
spell, as a coven, but he can target only three members of such a link.

**Gained:** At 2nd Level

**Replaces:** Slayer talent gained at 2nd level

**Special:** Studying a coven always requires a **move action**, even if the slayer could normally
study a target with a swift or immediate action.

**Disrupt Coven (Su)**

**At 7th Level:** Anyone the slayer threatens no longer counts as an ally for the purposes of
friendly spellcasting or employing teamwork feats and cannot access any special abilities gained
from being part of a coven (including coven spellcasting).^1^

**Replaces:** Stalker

**Unseen Sense (Su)**

**Ability:** The covenbane learns to use his _hag sense_ to help target concealed or invisible
opponents in combat. He can use his _hag sense_ to detect invisible opponents as well as magically
disguised creatures.

**Gained:** At 11th Level

**Replaces:** Swift tracker

**Special:** He also gains [Blind-Fight](ref/feat/blind-fight) as a bonus feat but gains its
benefits only against spellcasters and creatures with
[spell-like abilities](ref/umr/spell-like-abilities).

^1^ It's not explicitly stated, but since this replaces Stalker and is listed between a 2nd-level
and 11th-level ability, it has been listed here as a 7th-level ability.
