+++
id = "ref/arc-wizard/first-world-caller"
kind = "archetype"
title = "First World Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20First%20World%20Caller"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "first_world_caller", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "17"

[fields]
kind = "archetype"
replaces = ["Arcane school", "Scribe Scroll", "10th- and 15th-level bonus feats"]
alters = ["Arcane bond"]
replaces_features = ["arcane-school", "scribe-scroll"]
alters_features = ["arcane-bond"]
+++

Some wizards, typically First World [gnomes](ref/race/gnome), have mystical ties with the First
World, the primordial home of the fey. This bond allows them to more easily conjure creatures and
effects from the First World, giving them the nickname of First World callers.

**Fey Familiar**

**Ability:** A First World caller must select a familiar as his _arcane bond._ This familiar is
often the fey creature that was created when the First World caller's soul passed through the First
World on the way to being born. The familiar counts as both an animal and a fey for the purposes of
effects that depend on its type, rather than counting as a magical beast. It gains only half the
normal natural armor bonus for a familiar based on the First World caller's level (rounded down,
minimum 0), and it doesn't grant its special familiar ability to its master. Instead, the familiar
gains the [fey-touched creature](ref/template/fey-touched-creature) template.

**Alters:** Arcane bond

**At 10th Level:** The familiar grows a pair of delicate, gossamer wings, gaining a fly speed equal
to its land speed and average maneuverability. If the familiar could already fly, its
maneuverability improves by one step instead.

**Fey Summoner**

**Action:** Ability

**Replaces:** Arcane school, Scribe Scroll

A First World caller is able to conjure fey creatures. He gains
[Augment Summoning](ref/feat/augment-summoning) as a bonus feat. He adds the following creatures to
the [summon monster](ref/spell/summon-monster) list of the same level, allowing him to summon them
with the appropriate _[summon monster](ref/spell/summon-monster)_ spell.

- 1st-[grimple](ref/monster/gremlin-grimple) (gremlin), [mite](ref/monster/mite),
  [sprite](ref/monster/sprite)
- 2nd-[atomie](ref/monster/atomie), [fuath](ref/monster/gremlin-fuath) (gremlin),
  [nixie](ref/monster/nixie)
- 3rd-[leprechaun](ref/monster/leprechaun), [nuglub](ref/monster/gremlin-nuglub) (gremlin),
  [pooka](ref/monster/pooka)
- 4th-[kelpie](ref/monster/kelpie), [korred](ref/monster/korred), [twigjack](ref/monster/twigjack)
- 5th-[lampad](ref/monster/lampad), [lurker in light](ref/monster/lurker-in-light),
  [swan maiden](ref/monster/swan-maiden)
- 6th-[cold rider](ref/monster/cold-rider), [oceanid](ref/monster/oceanid),
  [sangoi](ref/monster/sangoi)
- 7th-[alp](ref/monster/alp), [bogeyman](ref/monster/bogeyman), [ijiraq](ref/monster/ijiraq)
- 8th-[banelight](ref/monster/banelight), [fastachee](ref/monster/fastachee),
  [rusalka](ref/monster/rusalka)
- 9th-[ankou](ref/monster/ankou), [kamaitachie](ref/monster/kamaitachie),
  [wild hunt archer](ref/monster/wild-hunt-wild-hunt-archer).

This ability is a function of the First World caller himself, and it applies even if he uses a
scroll, wand, or other magic item to cast a _[summon monster](ref/spell/summon-monster)_ spell. If
he creates such an item and it is used by another character, the spell functions as an ordinary
_[summon monster](ref/spell/summon-monster)_ spell.

**Warp Reality (Su)**

**At 10th Level:** A First World caller can reshape the nearby area at his whim, as he pulls in
aspects of the mutable and primal First World. To use this ability, he must expend a spell slot of
5th level or higher as a **standard action** and succeed at a DC 15 Charisma check. If he succeeds,
he can apply one of the following [planar traits](ref/rule/planar-traits) to the area in a 60-foot
radius for 2d4 minutes: _normal gravity, heavy gravity, light gravity, mildly aligned_ (chaos, evil,
good, or law), _enhanced magic,_ or _impeded magic._

**At 15th Level:** He can instead expend a slot of 7th level or higher and attempt a DC 20 Charisma
check. If successful, he can apply two planar traits from the previous list, or any one of the
following traits: _no gravity, subjective directional gravity, erratic time, fire-dominant,
water-dominant, negative-dominant, positive-dominant,_ or _wild magic._

**Replaces:** 10th- and 15th-level bonus feats
