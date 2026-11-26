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
features = [
  { anchor = "fey-familiar", level = 1 },
  { anchor = "fey-summoner", level = 1 },
  { anchor = "warp-reality", level = 10 },
]
trades = [
  { replaces = "Arcane school", feature = "arcane-school", by = ["fey-summoner"] },
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["fey-summoner"] },
  { replaces = "Bonus feats gained at 10th and 15th level", feature = "bonus-feats", levels = [10, 15], by = ["warp-reality"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["fey-familiar"] },
]
+++

Some wizards, typically First World [gnomes](ref/race/gnome), have mystical ties with the First
World, the primordial home of the fey. This bond allows them to more easily conjure creatures and
effects from the First World, giving them the nickname of First World callers.

## Fey Familiar {#fey-familiar}

A First World caller must select a familiar as his arcane bond. This familiar is often the fey
creature that was created when the First World caller's soul passed through the First World on the
way to being born. The familiar counts as both an animal and a fey for the purposes of effects that
depend on its type, rather than counting as a magical beast. It gains only half the normal natural
armor bonus for a familiar based on the First World caller's level (rounded down, minimum 0), and it
doesn't grant its special familiar ability to its master. Instead, the familiar gains the
[fey-touched creature](ref/template/fey-touched-creature) template (see sidebar). At 10th level, the
familiar grows a pair of delicate, gossamer wings, gaining a fly speed equal to its land speed and
average maneuverability. If the familiar could already fly, its maneuverability improves by one step
instead.

This alters arcane bond.

## Fey Summoner {#fey-summoner}

A First World caller is able to conjure fey creatures. He gains
[Augment Summoning](ref/feat/augment-summoning) as a bonus feat. He adds the following creatures to
the _[summon monster](ref/spell/summon-monster)_ list of the same level, allowing him to summon them
with the appropriate _[summon monster](ref/spell/summon-monster)_ spell:
1st—[grimple](ref/monster/gremlin-grimple) (gremlin), [mite](ref/monster/mite),
[sprite](ref/monster/sprite); 2nd—[atomie](ref/monster/atomie), [fuath](ref/monster/gremlin-fuath)
(gremlin), [nixie](ref/monster/nixie); 3rd—[leprechaun](ref/monster/leprechaun),
[nuglub](ref/monster/gremlin-nuglub) (gremlin), [pooka](ref/monster/pooka);
4th—[kelpie](ref/monster/kelpie), [korred](ref/monster/korred), [twigjack](ref/monster/twigjack);
5th—[lampad](ref/monster/lampad), [lurker in light](ref/monster/lurker-in-light),
[swan maiden](ref/monster/swan-maiden); 6th—[cold rider](ref/monster/cold-rider),
[oceanid](ref/monster/oceanid), [sangoi](ref/monster/sangoi); 7th—[alp](ref/monster/alp),
[bogeyman](ref/monster/bogeyman), [ijiraq](ref/monster/ijiraq);
8th—[banelight](ref/monster/banelight), [fastachee](ref/monster/fastachee),
[rusalka](ref/monster/rusalka); 9th—[ankou](ref/monster/ankou), kamaitachi,
[wild hunt archer](ref/monster/wild-hunt-wild-hunt-archer).

This ability is a function of the First World caller himself, and it applies even if he uses a
scroll, wand, or other magic item to cast a _[summon monster](ref/spell/summon-monster)_ spell. If
he creates such an item and it is used by another character, the spell functions as an ordinary
_[summon monster](ref/spell/summon-monster)_ spell.

This replaces arcane school and Scribe Scroll.

## Warp Reality (Su) {#warp-reality}

At 10th level, a First World caller can reshape the nearby area at his whim, as he pulls in aspects
of the mutable and primal First World. To use this ability, he must expend a spell slot of 5th level
or higher as a standard action and succeed at a DC 15 Charisma check. If he succeeds, he can apply
one of the following [planar traits](ref/rule/planar-traits) to the area in a 60-foot radius for 2d4
minutes: normal gravity, heavy gravity, light gravity, mildly aligned (chaos, evil, good, or law),
enhanced magic, or impeded magic. At 15th level, he can instead expend a slot of 7th level or higher
and attempt a DC 20 Charisma check. If successful, he can apply two planar traits from the previous
list, or any one of the following traits: no gravity, subjective directional gravity, erratic time,
fire-dominant, water-dominant, negative-dominant, positive-dominant, or wild magic. See page 58 of
_Pathfinder RPG Planar Adventures_ for more information on planar traits.

This replaces the bonus feats gained at 10th and 15th level.
