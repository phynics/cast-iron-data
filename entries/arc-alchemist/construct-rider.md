+++
id = "ref/arc-alchemist/construct-rider"
kind = "archetype"
title = "Construct Rider"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Construct%20Rider"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "construct_rider", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "craft-mount", level = 1 },
  { anchor = "diminished-extracts" },
  { anchor = "construct-rider-discoveries" },
]
trades = [
  { replaces = "Brew Potion", feature = "brew-potion", by = ["craft-mount"] },
  { replaces = "mutagen", feature = "mutagen", by = ["craft-mount"] },
  { replaces = "the discovery gained at 4th level", feature = "discovery", levels = [4], by = ["craft-mount"] },
]
+++

A construct rider creates arcane devices to emulate and surpass weak flesh. Class Skills: The
construct rider gains Ride (Dex) and Knowledge (engineering) (Int) as class skills.

## Craft Mount (Su) {#craft-mount}

A construct rider assembles a construct mount shaped like a riding animal. A Medium alchemist can
select a [camel](ref/companion/camel) or a [horse](ref/companion/horse). A Small alchemist can
select a [pony](ref/companion/pony) or [wolf](ref/companion/wolf), but can also select a
[boar](ref/companion/boar) or a [dog](ref/companion/dog) if he's at least 4th level. The GM may
approve other animals as mounts.

This construct mount acts in most ways as a druid [animal companion](ref/sidekick/animal-companion),
using the character's alchemist level as his effective druid level. A construct mount is a
construct, but uses the appropriate animal companion's statistics, gaining Hit Dice, skills, feats,
and Strength and Dexterity adjustments as the alchemist advances in level. A construct mount has no
Constitution score, and instead gains bonus hit points appropriate for a construct of its size. It
has an Intelligence score (and skill points), a lower base attack bonus, and better saving throws
than a normal construct of its Hit Dice. The mount has all the immunities of a construct (except
immunity to mind-affecting effects, since it has a mind). A construct rider can use Craft (alchemy)
instead of Handle Animal for all purposes involving his construct mount, though the check still
takes a -5 penalty due to the construct mount's unusual nature.

To create a construct with a mind and body that are constantly changing and improving, the construct
rider must manufacture vast quantities of clockwork or animating reagents. As such, the construct
rider can never gain the mutagen or cognatogen ability, even from a discovery or another class.

At first, his mount is a singular masterpiece created during a momentary stroke of brilliance. At
4th level, the construct rider gains [Craft Construct](ref/feat/craft-construct) as a bonus feat and
can use his extracts instead of spells to meet spell prerequisites when crafting other constructs.

This ability replaces Brew Potion, mutagen, and the discovery gained at 4th level.

## Diminished Extracts {#diminished-extracts}

A construct rider may prepare one fewer extract of each level than normal. If this reduces the
number to 0, he may prepare extracts of that level only if his Intelligence allows bonus extracts of
that level.

## Construct Rider Discoveries (Su) {#construct-rider-discoveries}

The construct rider can select from the following archetype-specific discoveries in place of an
alchemist discovery.

### Internal Reservoir (Ex, Sp) {#internal-reservoir}

The construct mount contains a reservoir tank than the construct rider can fill with one dose of a
potion or extract the construct rider created. As a move action that doesn't provoke an attack of
opportunity, the construct mount can apply the potion or extract to itself. Refilling the reservoir
is a complicated process that requires a DC 20 Craft (alchemy) check. Failure destroys the potion or
extract. The process requires 1 minute, and provokes attacks of opportunity. A construct rider must
be at least 6th level before selecting this discovery.

### Vaporizing Reservoir (Ex, Su) {#vaporizing-reservoir}

The construct rider upgrades his mount's reservoir, adding a compartment near the mouth which stores
a bomb. Loading the bomb requires the same process as loading an extract or potion. A construct
mount loaded with a bomb can unleash it as a breath weapon in a 15-foot cone or a 30-foot line as a
standard action, dealing damage as a direct hit against all targets in the area of effect. The
alchemist selects a line or cone area when loading the reservoir. Because the construct mount lacks
the alchemist's Throw Anything ability, the alchemist's Intelligence bonus doesn't apply to this
damage. A construct rider must be at least 8th level and possess the internal reservoir discovery
before selecting this discovery.

### Widened Vaporizer (Su) {#widened-vaporizer}

When the construct mount uses its breath weapon from the vaporizing reservoir discovery, it can also
unleash a 30-foot cone or a 60-foot line. A construct rider must be at least 10th level and possess
the internal reservoir and vaporizing reservoir discoveries before selecting this discovery.
