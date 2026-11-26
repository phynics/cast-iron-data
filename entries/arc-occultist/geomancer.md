+++
id = "ref/arc-occultist/geomancer"
kind = "archetype"
title = "Geomancer"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Geomancer"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geomancer", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "66"

[fields]
kind = "archetype"
features = [
  { anchor = "geomantic-focus" },
  { anchor = "geomancy" },
  { anchor = "survivalist", level = 2 },
  { anchor = "terrain-stride", level = 5 },
  { anchor = "dominion", level = 7 },
  { anchor = "wall-of-terrain", level = 13 },
]
trades = [
  { replaces = "Magic item skill", feature = "magic-item-skill", by = ["survivalist"] },
  { replaces = "Aura sight", feature = "aura-sight", by = ["terrain-stride"] },
  { replaces = "Focus power gained at 7th level", feature = "focus-powers", levels = [7], by = ["dominion"] },
  { replaces = "Focus power gained at 13th level", feature = "focus-powers", levels = [13], by = ["wall-of-terrain"] },
  { alters = "Mental focus", feature = "mental-focus", by = ["geomantic-focus"] },
  { alters = "Implements", feature = "implements", by = ["geomancy"] },
  { alters = "Class skills" },
]
+++

A geomancer studies every type of land, deriving power from the differences between types of
terrain.

## Class Skills {#class-skills}

A geomancer adds Knowledge (geography), Knowledge (nature), and Survival to his list of class skills
instead of Disable Device, Knowledge (engineering), and Knowledge (religion).

This alters the occultist's class skills.

## Geomantic Focus (Su) {#geomantic-focus}

When a geomancer invests mental focus into his implements for the day, he can store some of it in
the surrounding terrain. As long as he remains in physical contact with the terrain, he gains the
survivalist resonant power and the ability to use the terrain stride, dominion, and wall of terrain
focus powers as appropriate for his level.

This alters mental focus.

## Geomancy (Su) {#geomancy}

A geomancer learns one fewer implement school at 1st level. Instead, the spells that he knows are
partially determined by the type of terrain he is currently in (and the level of spells he can
cast). When he leaves a type of terrain, he loses knowledge of the spells that terrain grants and
instead knows the spells granted by the new type of terrain he has entered. If a specific terrain
falls into more than one category, the geomancer chooses which list of spells he receives when he
enters the terrain. The spells at each spell level for the various types of terrain are listed
below.

_Cold:_ 1st—_frostbite_, 2nd—_frigid touch_, 3rd—_sleet storm_, 4th—_creeping ice_, 5th—_icy
prison_, 6th—_freezing sphere._

_Desert:_ 1st—_sun metal_, 2nd—_shifting sand_, 3rd—_cup of dust_, 4th—_fire shield_, 5th—_flame
strike_, 6th—_sirocco_.

_Forest:_ 1st—_entangle_, 2nd—_tree shape_, 3rd—_speak with plants_, 4th—_arboreal hammer_,
5th—_tree stride_, 6th—_liveoak_.

_Jungle:_ 1st—_nauseating dart_, 2nd—_sickening entanglement_, 3rd—_venomous bolt_, 4th—_poison_,
5th—_snake staff_, 6th—_swarm skin_.

_Mountain:_ 1st—_stone fist_, 2nd—_stone call_, 3rd—_stone shape_, 4th—_obsidian flow_, 5th—_cave
fangs_, 6th—_move earth_.

_Plains:_ 1st—_mount_, 2nd—_gust of wind_, 3rd—_plant growth_, 4th—_aspect of the stag_,
5th—_control winds_, 6th—_whip of ants._

### Planes (Other Than the Material Plane) {#planes-other-than-the-material-plane}

1st—_endure elements_, 2nd—_rope trick_, 3rd—_blink_, 4th—_dimensional anchor_, 5th—_planar
adaptation_, 6th—_plane shift_.

_Swamp:_ 1st—_mudball_, 2nd—_burst of nettles_, 3rd—_lily pad stride_, 4th—_slowing mud_,
5th—_insect plague_, 6th—_mass fester_.

_Underground:_ 1st—_expeditious excavation_, 2nd—_[darkvision](ref/rule/darkvision)_, 3rd—_meld into
stone_, 4th—_echolocation_, 5th—_suffocation_, 6th—_conjure black pudding_.

_Urban:_ 1st—_urban grace_, 2nd—_share language_, 3rd—_urban step_, 4th—_zone of silence_,
5th—_telepathic bond_, 6th—_statue_.

_Water:_ 1st—_air bubble_, 2nd—_slipstream_, 3rd—_water breathing_, 4th—_fluid form_, 5th—_geyser_,
6th—_control water_.

This alters implements.

## Survivalist (Su) {#survivalist}

At 2nd level, a geomancer gains a +1 bonus on Survival checks for every point of mental focus
invested in the terrain (to a maximum equal to his occultist level).

This replaces magic item skill.

## Terrain Stride (Su) {#terrain-stride}

At 5th level, as a swift action, a geomancer can expend 1 point of mental focus invested in the
terrain to increase all of his movement speeds by 10 feet. At 5th level, the geomancer can expend 2
points of mental focus invested in the terrain to instead increase all of his movement speeds by 20
feet. This affects only movement speeds he already has.

This replaces aura sight.

## Dominion (Su) {#dominion}

At 7th level, as a standard action, a geomancer can expend 1 or more points of mental focus invested
in the terrain to infuse himself and each of his allies within 30 feet of him with the might of the
land. Affected creatures gain a +1 morale bonus on attack rolls, damage rolls, and Fortitude saves
for every point of mental focus expended. These bonuses last for 1 minute and can't exceed
one-quarter the geomancer's occultist level.

This replaces the focus power gained at 7th level.

## Wall of Terrain (Sp) {#wall-of-terrain}

At 13th level, as a standard action, a geomancer can expend 3 points of mental focus invested in the
terrain to fashion a solid wall of the surrounding terrain, no matter its actual composition. This
functions as per _[wall of stone](ref/spell/wall-of-stone)_, using the geomancer's occultist level
as his caster level. By expending an extra point of generic mental focus, he can increase the
[hardness](ref/umr/hardness) of the wall to 10 and give it an extra 5 hit points per inch of
thickness.

This replaces the focus power gained at 13th level.
