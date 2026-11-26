+++
id = "ref/arc-rogue/eldritch-scoundrel"
kind = "archetype"
title = "Eldritch Scoundrel"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Eldritch%20Scoundrel"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_scoundrel", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "arcane-anthology"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "alarm-sense", level = 3 },
  { anchor = "sneak-attack", level = 3 },
  { anchor = "rogue-talents", level = 4 },
  { anchor = "uncanny-training", level = 4 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["alarm-sense"] },
  { alters = "Armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Skills" },
  { alters = "Sneak attack progression", feature = "sneak-attack", by = ["sneak-attack"] },
  { alters = "Rogue talent progression", feature = "rogue-talents", by = ["rogue-talents"] },
  { alters = "advanced talent", feature = "advanced-talents", by = ["rogue-talents"] },
  { alters = "Uncanny dodge", feature = "uncanny-dodge", by = ["uncanny-training"] },
  { alters = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["uncanny-training"] },
]
+++

Students of arcane magic, legerdemain, and stealth, eldritch scoundrels are a rare breed of
adventurer most commonly found seeking lost and valuable arcane writings in the ruins of fallen
empires, such as Thassilon or the Jistka Imperium.

## Armor Proficiencies {#armor-proficiencies}

An eldritch scoundrel is not proficient with any armor or shields. Armor sometimes interferes with
an eldritch scoundrel's gestures, which can cause her spells with somatic components to fail
(_Pathfinder RPG Core Rulebook_ 83). This alters the rogue's armor proficiencies.

## Class Skills {#class-skills}

An eldritch scoundrel gains 4 skill ranks (plus a number of ranks equal to her Intelligence
modifier) at each level instead of a normal 8. She gains Knowledge (arcana) and Spellcraft as class
skills, but not Diplomacy and Disguise. This alters the rogue's skills.

## Spells {#spells}

An eldritch scoundrel casts arcane spells drawn from the [wizard](ref/class/wizard) spell list. An
eldritch scoundrel must choose and prepare her spells ahead of time. She learns, prepares, and casts
spells exactly as a wizard does, including adding new spells to her spellbook and gaining two
additional spells known (of any level she can cast) each time she gains a rogue level with this
archetype.

An eldritch scoundrel can cast only a certain number of spells of each spell level per day. Her base
daily spell allotment is the same as the [magus](ref/class/magus) class (_Pathfinder RPG Ultimate
Magic_ 10).

## Alarm Sense (Su) {#alarm-sense}

At 3rd level, an eldritch scoundrel gains an intuitive sense that warns her when she is near a magic
trap. This functions as the [trap spotter](ref/talent/trap-spotter) rogue talent, but applies only
if the eldritch scoundrel comes within 10 feet of a magic trap. This ability replaces trap sense.

## Sneak Attack (Ex) {#sneak-attack}

The eldritch scoundrel doesn't acquire the sneak attack class feature until 3rd level, when she
gains a +1d6 sneak attack. This increases by 1d6 at 7th level, and again at every 4 rogue levels
thereafter. This modifies the rogue's normal sneak attack progression.

## Rogue Talents {#rogue-talents}

At 4th level and every 4 levels thereafter, the eldritch scoundrel gains a rogue or ninja talent for
which she meets the prerequisites (treating her rogue level as her ninja level). If a talent
requires her to expend points from her ki pool, she can instead expend a spell slot with a spell
level equal to the number of ki points she would normally expend. If a talent functions only if she
has ki in her ki pool, it functions as long as she still has a spell of 1st level or higher
prepared. At 12th level, she can select an advanced talent in place of a rogue talent. This modifies
the normal rogue talent progression and advanced talent.

## Uncanny Training {#uncanny-training}

An eldritch scoundrel does not gain [uncanny dodge](ref/ability/uncanny-dodge) or
[improved uncanny dodge](ref/ability/improved-uncanny-dodge). Beginning at 4th level, she can take
uncanny dodge instead of a rogue talent. Beginning at 12th level, the eldritch scoundrel can choose
to take improved uncanny dodge in place of an advanced talent. This modifies uncanny dodge and
improved uncanny dodge.
