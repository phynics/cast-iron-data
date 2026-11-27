+++
id = "ref/rule/class-ranger/ranger"
kind = "rule"
title = "Ranger"
source_ids = ["core-rulebook", "chronicle-of-legends", "advanced-players-guide"]
section = ["Ranger"]
parent = "ref/class/ranger"
provenance = [
  { dataset = "pathfinder-data-1-e", record = "json/classes7.json#ranger|section:ranger", path = "json/classes7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "64"
[[sources]]
publication = "chronicle-of-legends"
page = "28-29"
[[sources]]
publication = "advanced-players-guide"
page = "72"

[fields]
kind = "none"
+++

For those who relish the thrill of the hunt, there are only predators and prey. Be they scouts,
trackers, or bounty hunters, rangers share much in common: unique mastery of specialized weapons,
skill at stalking even the most elusive game, and the expertise to defeat a wide range of quarries.
Knowledgeable, patient, and skilled hunters, these rangers hound man, beast, and monster alike,
gaining insight into the way of the predator, skill in varied environments, and ever more lethal
martial prowess. While some track man-eating creatures to protect the frontier, others pursue more
cunning game - even fugitives among their own people.

**Role:** Rangers are deft skirmishers, either in melee or at range, capable of skillfully dancing
in and out of battle. Their abilities allow them to deal significant harm to specific types of foes,
but their skills are valuable against all manner of enemies.

**Alignment:** Any

**Hit Die:** d10

**Starting Wealth:** 5d6 × 10 gp (average 175 gp)

**Skill Points per Level:** 6 + Int modifier

**Class Skills (Str):** Climb, Swim

**Class Skills (Dex):** Ride, Stealth

**Class Skills (Int):** Craft (any), Knowledge (dungeoneering), Knowledge (geography), Knowledge
(nature), Spellcraft

**Class Skills (Wis):** Heal, Perception, Profession (any), Survival

**Class Skills (Cha):** Handle Animal, Intimidate

### Class Features and Spells Per Day

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|1st|2nd|3rd|4th|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1st|+1|+2|+2|+0|1st favored enemy, track, wild empathy|-|-|-|-|
|2nd|+2|+3|+3|+0|Combat style feat|-|-|-|-|
|3rd|+3|+3|+3|+1|Endurance, 1st favored terrain|-|-|-|-|
|4th|+4|+4|+4|+1|Hunter's bond|0|-|-|-|
|5th|+5|+4|+4|+1|2nd favored enemy|1|-|-|-|
|6th|+6/+1|+5|+5|+2|Combat style feat|1|-|-|-|
|7th|+7/+2|+5|+5|+2|Woodland stride|1|0|-|-|
|8th|+8/+3|+6|+6|+2|Swift tracker, 2nd favored terrain|1|1|-|-|
|9th|+9/+4|+6|+6|+3|Evasion|2|1|-|-|
|10th|+10/+5|+7|+7|+3|3rd favored enemy, combat style feat|2|1|0|-|
|11th|+11/+6/+1|+7|+7|+3|Quarry|2|1|1|-|
|12th|+12/+7/+2|+8|+8|+4|Camouflage|2|2|1|-|
|13th|+13/+8/+3|+8|+8|+4|3rd favored terrain|3|2|1|0|
|14th|+14/+9/+4|+9|+9|+4|Combat style feat|3|2|1|1|
|15th|+15/+10/+5|+9|+9|+5|4th favored enemy|3|2|2|1|
|16th|+16/+11/+6/+1|+10|+10|+5|Improved evasion|3|3|2|1|
|17th|+17/+12/+7/+2|+10|+10|+5|Hide in plain sight|4|3|2|1|
|18th|+18/+13/+8/+3|+11|+11|+6|4th favored terrain, combat style feat|4|3|2|2|
|19th|+19/+14/+9/+4|+11|+11|+6|Improved quarry|4|3|3|2|
|20th|+20/+15/+10/+5|+12|+12|+6|5th favored enemy, master hunter|4|4|3|3|

### Class Features {#class-features}

All of the following are class features of the ranger.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

A ranger is proficient with all simple and martial weapons and with light armor, medium armor, and
shields (except tower shields).

#### Favored Enemy (Ex) {#favored-enemy}

At 1st level, a ranger selects a creature type from the ranger favored enemies table. He gains a +2
bonus on Bluff, Knowledge, Perception, Sense Motive, and Survival checks against creatures of his
selected type. Likewise, he gets a +2 bonus on weapon attack and damage rolls against them. A ranger
may make Knowledge skill checks untrained when attempting to identify these creatures.

At 5th level and every five levels thereafter (10th, 15th, and 20th level), the ranger may select an
additional favored enemy. In addition, at each such interval, the bonus against any one favored
enemy (including the one just selected, if so desired) increases by +2.

If the ranger chooses humanoids or outsiders as a favored enemy, he must also choose an associated
subtype, as indicated on the table below. (Note that there are other types of humanoid to choose
from in the _Pathfinder RPG Bestiary_—those called out specifically on the table below are merely
the most common.) If a specific creature falls into more than one category of favored enemy, the
ranger's bonuses do not stack; he simply uses whichever bonus is higher.

|Type (Subtype)|Type (Subtype)|
| --- | --- |
|Aberration|Humanoid (other subtype)|
|Animal|Magical beast|
|Construct|Monstrous humanoid|
|Dragon|Ooze|
|Fey|Outsider (air)|
|Humanoid (aquatic)|Outsider (chaotic)|
|Humanoid (dwarf)|Outsider (earth)|
|Humanoid (elf)|Outsider (evil)|
|Humanoid (giant)|Outsider (fire)|
|Humanoid (goblinoid)|Outsider (good)|
|Humanoid (gnoll)|Outsider (lawful)|
|Humanoid (gnome)|Outsider (native)|
|Humanoid (halfling)|Outsider (water)|
|Humanoid (human)|Plant|
|Humanoid (orc)|Undead|
|Humanoid (reptilian)|Vermin|

#### Track (Ex) {#track}

A ranger adds [half](ref/misc/fractions-and-rounding) his level (minimum 1) to Survival skill checks
made to follow tracks.

#### Wild Empathy (Ex) {#wild-empathy}

A ranger can improve the initial attitude of an animal. This ability functions just like a
[Diplomacy](ref/skill/diplomacy) check to improve the attitude of a person (see Chapter 4). The
ranger rolls 1d20 and adds his ranger level and his Charisma bonus to determine the wild empathy
check result. The typical domestic animal has a starting attitude of indifferent, while wild animals
are usually unfriendly.

To use wild empathy, the ranger and the animal must be within 30 feet of one another under normal
visibility conditions. Generally, influencing an animal in this way takes 1 minute, but, as with
influencing people, it might take more or less time.

The ranger can also use this ability to influence a magical beast with an Intelligence score of 1 or
2, but he takes a -4 penalty on the check.

#### Combat Style Feat (Ex) {#combat-style-feat}

At 2nd level, a ranger must select one of two combat styles to pursue: archery or two-weapon combat.
The ranger's expertise manifests in the form of bonus feats at 2nd, 6th, 10th, 14th, and 18th level.
He can choose feats from his selected [combat style](ref/ability/combat-styles), even if he does not
have the normal prerequisites.

If the ranger selects archery, he can choose from the following list whenever he gains a combat
style feat: Far Shot, Point Blank Shot, Precise Shot, and Rapid Shot. At 6th level, he adds Improved
Precise Shot and Manyshot to the list. At 10th level, he adds Pinpoint Targeting and Shot on the Run
to the list.

If the ranger selects two-weapon combat, he can choose from the following list whenever he gains a
combat style feat: Double Slice, Improved Shield Bash, Quick Draw, and Two-Weapon Fighting. At 6th
level, he adds Improved Two-Weapon Fighting and Two-Weapon Defense to the list. At 10th level, he
adds Greater Two-Weapon Fighting and Two-Weapon Rend to the list.

The benefits of the ranger's chosen style feats apply only when he wears light, medium, or no armor.
He loses all benefits of his combat style feats when wearing heavy armor. Once a ranger selects a
combat style, it cannot be changed.

#### Endurance {#endurance}

A ranger gains [Endurance](ref/feat/endurance) as a bonus feat at 3rd level.

#### Favored Terrain (Ex) {#favored-terrain}

At 3rd level, a ranger may select a type of terrain from the Favored Terrains table. The ranger
gains a +2 bonus on initiative checks and Knowledge (geography), Perception, Stealth, and Survival
skill checks when he is in this terrain. A ranger traveling through his favored terrain normally
leaves no trail and cannot be tracked (though he may leave a trail if he so chooses).

At 8th level and every five levels thereafter, the ranger may select an additional favored terrain.
In addition, at each such interval, the skill bonus and initiative bonus in any one favored terrain
(including the one just selected, if so desired), increases by +2.

If a specific terrain falls into more than one category of favored terrain, the ranger's bonuses do
not stack; he simply uses whichever bonus is higher.

- Cold (ice, glaciers, snow, and tundra)
- Desert (sand and wastelands)
- Forest (coniferous and deciduous)
- Jungle
- Mountain (including hills)
- Plains
- Planes (pick one, other than Material Plane)
- Swamp
- Underground (caves and dungeons)
- Urban (buildings, streets, and sewers)
- Water (above and below the surface)

#### Hunter's Bond (Ex) {#hunter-s-bond}

At 4th level, a ranger forms a bond with his hunting companions. This bond can take one of two
forms. Once the form is chosen, it cannot be changed. The first is a bond to his companions. This
bond allows him to spend a move action to grant half his favored enemy bonus against a single target
of the appropriate type to all allies within 30 feet who can see or hear him. This bonus lasts for a
number of rounds equal to the ranger's Wisdom modifier (minimum 1). This bonus does not stack with
any favored enemy bonuses possessed by his allies; they use whichever bonus is higher.

The second option is to form a close bond with an animal companion. A ranger who selects an animal
companion can choose from the following list: badger, bird, camel, cat (small), dire rat (see the
_Pathfinder RPG Bestiary_), dog, horse, pony, snake (viper or constrictor), or wolf. If the campaign
takes place wholly or partly in an aquatic environment, the ranger may choose a shark instead. This
animal is a loyal companion that accompanies the ranger on his adventures as appropriate for its
kind. A ranger's animal companion shares his favored enemy and favored terrain bonuses.

This ability functions like the druid animal companion ability (which is part of the Nature Bond
class feature), except that the ranger's effective druid level is equal to his ranger level - 3.

#### Spells {#spells}

Beginning at 4th level, a ranger gains the ability to cast a small number of divine spells, which
are drawn from the ranger spell list presented in Chapter 10. A ranger must choose and prepare his
spells in advance.

To prepare or cast a spell, a ranger must have a Wisdom score equal to at least 10 + the spell
level. The Difficulty Class for a saving throw against a ranger's spell is 10 + the spell level +
the ranger's Wisdom modifier.

Like other spellcasters, a ranger can cast only a certain number of spells of each spell level per
day. His base daily spell allotment is given on Table 3–12. In addition, he receives
[bonus spells per day](ref/rule/determine-bonuses) if he has a high Wisdom score (see Table 1–3).
When Table 3–12 indicates that the ranger gets 0 spells per day of a given spell level, he gains
only the bonus spells he would be entitled to based on his Wisdom score for that spell level.

A ranger must spend 1 hour per day in quiet meditation to regain his daily allotment of spells. A
ranger may prepare and cast any spell on the ranger spell list, provided that he can cast spells of
that level, but he must choose which spells to prepare during his daily meditation.

Through 3rd level, a ranger has no caster level. At 4th level and higher, his caster level is equal
to his ranger level - 3.

#### Woodland Stride (Ex) {#woodland-stride}

Starting at 7th level, a ranger may move through any sort of undergrowth (such as natural thorns,
briars, overgrown areas, and similar terrain) at his normal speed and without taking damage or
suffering any other impairment.

Thorns, briars, and overgrown areas that are enchanted or magically manipulated to impede motion,
however, still affect him.

#### Swift Tracker (Ex) {#swift-tracker}

Beginning at 8th level, a ranger can move at his normal speed while using Survival to follow tracks
without taking the normal -5 penalty. He takes only a -10 penalty (instead of the normal -20) when
moving at up to twice normal speed while tracking.

#### Evasion (Ex) {#evasion}

When he reaches 9th level, a ranger can avoid even magical and unusual attacks with great agility.
If he makes a successful Reflex saving throw against an attack that normally deals half damage on a
successful save, he instead takes no damage. Evasion can be used only if the ranger is wearing light
armor, medium armor, or no armor. A [helpless](ref/misc/helpless) ranger does not gain the benefit
of evasion.

#### Quarry (Ex) {#quarry}

At 11th level, a ranger can, as a standard action, denote one target within his line of sight as his
quarry. Whenever he is following the tracks of his quarry, a ranger can take 10 on his Survival
skill checks while moving at normal speed, without penalty. In addition, he receives a +2 insight
bonus on attack rolls made against his quarry, and all critical threats are automatically confirmed.
A ranger can have no more than one quarry at a time and the creature's type must correspond to one
of his favored enemy types. He can dismiss this effect at any time as a free action, but he cannot
select a new quarry for 24 hours. If the ranger sees proof that his quarry is dead, he can select a
new quarry after waiting 1 hour.

#### Camouflage (Ex) {#camouflage}

A ranger of 12th level or higher can use the Stealth skill to hide in any of his favored terrains,
even if the terrain doesn't grant [cover](ref/rule/cover) or [concealment](ref/rule/concealment).

#### Improved Evasion (Ex) {#improved-evasion}

At 16th level, a ranger's evasion improves. This ability works like evasion, except that while the
ranger still takes no damage on a successful Reflex saving throw against attacks, he henceforth
takes only half damage on a failed save. A helpless ranger does not gain the benefit of improved
evasion.

#### Hide in Plain Sight (Ex) {#hide-in-plain-sight}

While in any of his favored terrains, a ranger of 17th level or higher can use the Stealth skill
even while being observed.

#### Improved Quarry (Ex) {#improved-quarry}

At 19th level, the ranger's ability to hunt his quarry improves. He can now select a quarry as a
free action, and can now take 20 while using Survival to track his quarry, while moving at normal
speed without penalty. His insight bonus to attack his quarry increases to +4. If his quarry is
killed or dismissed, he can select a new one after 10 minutes have passed.

#### Master Hunter (Ex) {#master-hunter}

A ranger of 20th level becomes a master hunter. He can always move at full speed while using
Survival to follow tracks without penalty. He can, as a standard action, make a single attack
against a favored enemy at his full attack bonus. If the attack hits, the target takes damage
normally and must make a Fortitude save or die. The DC of this save is equal to 10 + 1/2 the
ranger's level + the ranger's Wisdom modifier. A ranger can choose instead to deal an amount of
nonlethal damage equal to the creature's current hit points. A successful save negates this damage.
A ranger can use this ability once per day against each favored enemy type he possesses, but not
against the same creature more than once in a 24-hour period.

### Alternate Capstones

When a character reaches the 20th level of a class, she gains a powerful class feature or ability,
sometimes referred to as a capstone. The following section provides new capstones for characters to
select at 20th level. A character can select one of the following capstones in place of the capstone
provided by her class. Some capstones are for specific classes, while others are for a range of
classes that qualify for them. In some cases, a capstone specifies what ability it replaces. A
character can't select a new capstone if she has previously traded away her class capstone via an
archetype. Clerics and wizards can receive a capstone at 20th level, despite not having one to begin
with. A character that gains certain abilities may be eligible for capstones other than those listed
below.

**Seen It Before (Ex)**

At 20th level, the ranger is wise to all the tricks of his prey. The ranger adds his _favored enemy_
bonus as an insight bonus on saves against spells and abilities used by his _favored enemies._

**Also available:** Great Beast, Old Dog, New Tricks

### Archetypes

From the noble paladin to the skillful rogue, each class draws upon a central archetype. Yet, beyond
that basic concept exists the potential for innumerable interpretations, details, and refinements;
and some archetypes prove pervasive and exciting enough to see use in play time and time again.

To help players interested in creating iconic fantasy characters, **archetypes** were introduced.
These optional features represent a unique view of what a class deliberately designed to capture a
specific character archetype might become. While the types of options presented for each class
differ, each subsystem is customized to best serve that class, emulate the abilities and talents of
classic fantasy archetypes, and expand players' freedom to design exactly the characters they
desire.

**Abendego Diver**

**Class:** ranger

**Modifies or Replaces:** Weapon and Armor Proficiencies; Track; Wild Empathy; Favored Terrain;
Woodland Stride; Swift Tracker; Master Hunter

**Description:** Named for the vicious and unending storm in the southern Arcadian Ocean, Abendego
divers have pushed their bodies to their limits, holding their breath to expand their lung capacity
and swimming until ocean travel is second nature to them.

**Battle Scout**

**Class:** ranger

**Modifies or Replaces:** Hunter's Bond; 2nd, 3rd, 4th Favored Enemies; Master Hunter

**Description:** Though regular outdoorsmen might suffice in many cases, some large forces look to
battle scouts to keep the body of their troops safe and prepared for the terrain and whatever
dangers that terrain hides.

**Beast Master**

**Class:** ranger

**Modifies or Replaces:** Hunter's Bond; 6th-level Combat Style Feat; Camouflage

**Description:** Some rangers, particularly those in primitive lands or who were raised by animals,
have unusually strong bonds with animals.

**Blightwarden**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; Wild Empathy; 1st Favored Terrain; Endurance

**Description:** Some rangers feel so closely connected to their homelands that they stand as
guardians against pervasive corruptions that pervert those lands beyond the point of recognition.

**Bow Nomad**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Combat Style; Endurance; Favored Terrain; 6th-level Combat
Feat; Camouflage; Hide in Plain Sight

**Description:** (Kasatha Only) Thanks to their four arms, kasathas can master a combat form native
to their home world and rarely witnessed on Golarion - wielding two bows at once.

**Cinderwalker**

**Class:** ranger

**Modifies or Replaces:** 1st Favored Terrain; Wild Empathy; Hunter's Bond; Woodland Stride

**Description:** Cinderwalkers traverse burning wastelands and restless mountains, thriving in lands
most creatures avoid.

**Code Runner**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Wild Empathy; Hunter's Bond

**Description:** A code runner specializes in the subtle and speedy transfer of secret messages.

**Corpse Hunter**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Spells; Favored Enemies; Woodland Stride; Swift Tracker

**Description:** Many rangers count the undead among their favored enemies, but some make a
full-time job out of hunting down and destroying these walking corpses.

**Dandy**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Favored Enemy; Wild Empathy; Favored Terrain; Hunter's Bond;
Spellcasting; Woodland Stride

**Description:** The antithesis of the gruff and wild woodsmen, a dandy takes effort to master the
subtle etiquette of noble courts, the whispers of dark rumors, and the customs of the cultured
world.

**Darklands Sailor**

**Class:** ranger

**Modifies or Replaces:** Track; Favored Terrain; Woodland Stride; Swift Tracker; Camouflage; Hide
in Plain Sight

**Description:** Those plying the lightless waters of the Darklands learn to use sound to augment
their compromised vision, providing insight into the hazards lurking below the surface.

**Deep Walker**

**Class:** ranger

**Modifies or Replaces:** Favored Terrain; Woodland Stride; Camouflage; Hide in Plain Sight

**Description:** Some rangers devote their lives to the woods, becoming hunters, protectors, and
wilderness guides among its diverse terrain types.

**Divine Tracker**

**Class:** ranger

**Modifies or Replaces:** Alignment; Wild Empathy; Hunter's Bond

**Description:** Blessed by his deity, a divine tracker hunts down those he deems deserving of his
retribution.

**Dragon Hunter**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Track; 5th, 10th, 15th, 20th-level Favored Enemies

**Description:** The quintessential dragonslayers, dragon hunters are experts at forging through the
wilds in search of great wyrms.

**Drake Warden**

**Class:** ranger

**Modifies or Replaces:** Hunter's Bond; 2nd Favored Enemy; Swift Tracker

**Description:** Some rangers specialize in dealing with rambunctious younger drakes and thanks to
their methods, their drakes are both fiercely loyal and extremely useful for scouting and stealth
missions.

**Dungeon Rover**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Track; Wild Empathy; Hunter's Bond; Woodland Stride; Swift
Tracker

**Description:** These rangers specialize in surviving hostile subterranean environs. They are well
equipped to avoid traps, spot secret passages, and deal with inimical dungeon tenants.

**Dusk Stalker**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Favored Terrain; Hunter's Bond; Camouflage

**Description:** (Fetchling Only) Hunters and guides through the Shadow Plane, dusk stalkers are
rangers that thrive in shadow.

**Elemental Envoy**

**Class:** ranger

**Modifies or Replaces:** Combat Style; Favored Terrain

**Description:** An elemental envoy travels the Elemental Planes. He has learned to protect himself
from their many dangers, and he models his fighting style after their teachings.

**Falconer**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Hunter's Bond; 6th-level Combat Style Feat

**Description:** Rangers have always enjoyed a special bond with a specific animal, but the falconer
takes this bond to a deeper level.

**Flamewarden**

**Class:** ranger

**Modifies or Replaces:** Hunter's Bond; Spells; Evasion; Camouflage; Improved Evasion; Master
Hunter

**Description:** Emulating the blazing phoenix, flamewardens sweep through the world like a
selective forest fire, burning away corruption, evil, and those who cling to decay.

**Fortune-Finder**

**Class:** ranger

**Modifies or Replaces:** Track; Hunter's Bond; Woodland Stride; Quarry; Improved Quarry; Master
Hunter

**Description:** Vanaras often leave home to seek fortune and sate their curiosity regarding the
mysterious lands that lie beyond their native territories. The most skilled of these thrillseekers
are called ba-sadhaks, or fortune-finders.

**Freebooter**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; Hunter's Bond; Woodland Stride

**Description:** A freebooter is a natural leader, a pirate who works well with a variety of people
and in a variety of roles.

**Galvanic Saboteur**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Favored Enemy; Wild Empathy; Favored Terrain; Woodland
Stride; Swift Tracker; Camouflage; Hide in Plain Sight

**Description:** Many Kellid locals blame Kevoth-Kul's change on the influence of the Technic League
and view both the League and their mechanical minions with a mix of fear and distrust. Some Kellid
rangers have since developed skills to defeat the League's robotic enforcers and devious arcanists.

**Groom**

**Class:** ranger

**Modifies or Replaces:** Track; Endurance; 1st Favored Terrain

**Description:** The groom attends to the needs of the party's mounts and beasts of burden during
their adventures, and guards these animals while the party goes underground.

**Guide**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; Hunter's Bond; Evasion; Quarry; Improved Quarry; Improved
Evasion

**Description:** Many rangers are loners, but some choose to use their familiarity with the land to
guide others safely through the wilderness.

**Guildbreaker**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Favored Enemy; Wild Empathy; Hunter's Bond; Woodland Stride

**Description:** Guildbreakers stoke their enmity for their foes, and they train to track the
movements of rival organizations, and even to infiltrate these groups to gather secret intelligence.

**Hooded Champion**

**Class:** ranger

**Modifies or Replaces:** 1st-level Favored Enemy; Combat Style; Wild Empathy; Endurance; Evasion;
Improved Evasion

**Description:** The hooded champion lives on the periphery of civilized lands, and is often at odds
with the forces of law and order.

**Horse Lord**

**Class:** ranger

**Modifies or Replaces:** Hunter's Bond; Camouflage; Hide in Plain Sight

**Description:** Rangers of the plains use horses or other riding beasts to hunt their lands,
forging a near-mystical relationship with their mounts.

**Ilsurian Archer**

**Class:** ranger

**Modifies or Replaces:** Track; Wild Empathy; Combat Style; Spellcasting; Swift Tracker; Quarry;
Improved Quarry

**Description:** Ilsurian archers maintain the strong tradition of archery first developed by
soldiers in the service of Ilsur, who raised a small army with which he intended to overthrow the
monarch of Korvosa after the fall of the Chelish Empire.

**Infiltrator**

**Class:** ranger

**Modifies or Replaces:** Favored Terrain

**Description:** Some rangers study their favored enemies and learn their ways, applying this
knowledge to their own abilities and using their foes' strengths against them.

**Jungle Lord**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Weapon and Armor Proficiency; Favored Enemy; Favored
Terrain; Hunter's Bond; Spells; 5th, 10th, 15th, 18th-level Favored Terrain; Quarry; Improved
Quarry; Camouflage; Master Hunter

**Description:** Jungle lords are tempered by their harsh and unforgiving environments into
something more than ordinary men and women.

**Lantern Lighter**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Endurance; Favored Terrain; Woodland Stride; Camouflage;
Hide in Plain Sight

**Description:** Lantern lighters were originally entrusted with secretly eliminating the drow and
quarantining any knowledge of their existence, but in the new Lantern Bearer era, the lantern
lighters have refocused their efforts on helping to rescue those imprisoned by the drow, or even to
help individual drow who seek to escape the cruelties of their society for a chance at redemption on
the surface.

**Nirmathi Irregular**

**Class:** ranger

**Modifies or Replaces:** Normal Weapon/Armor Proficiencies; Favored Enemy; Favored Terrain; Altered
Spell List

**Description:** An irregular troop from Nirmathas, this ranger chooses to focus on the magic of
stealth.

**Planar Scout**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Wild Empathy; Favored Terrain; Hunter's Bond; Evasion;
Improved Evasion

**Description:** Planar scouts are rangers specializing in traversing the planes - and surviving
their journeys.

**Poison Darter**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; Wild Empathy; Combat Style; Hunter's Bond; Master Hunter

**Description:** (Grippli) In dense jungles, foliage and tight spaces hinder all but the most
deceptively humble weapons: blowguns and poison.

**Raven Master**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Wild Empathy; Hunter's Bond; Woodland Stride; Swift Tracker;
Camouflage; Spellcasting

**Description:** Raven masters serve as messengers and spies for the Silver Ravens, eschewing a
ranger's usual connection to the natural world to form a mystic bond with their birds and to grant
both animal and master a number of specialized abilities

**Realm Wanderer**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Track; Hunter's Bond; Swift Tracker; Master Hunter

**Description:** These rangers take to heart the lessons they've learned from their vastly
contrasting experiences and know that creatively embracing this wisdom is sometimes the difference
between life and death.

**Sable Company Marine**

**Class:** ranger

**Modifies or Replaces:** Hunter's Bond

**Description:** Sable Company marines receive their training at the elite Endrin Military Academy
in Korvosa. A large portion of their education is the handling and riding of hippogriffs, the iconic
mounts of members of the company.

**Sentinel**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Hunter's Bond; Woodland Stride; 6th-level Combat Style Feat;
Quarry; Improved Quarry

**Description:** A sentinel specializes in heightening all of her senses to expose spies and those
who work for opposing factions, rooting out all who attempt to slip past her evervigilant watch.

**Shapeshifter**

**Class:** ranger

**Modifies or Replaces:** Favored Terrain; Camouflage; Master Hunter

**Description:** Most rangers venture into the wilderness, but there are some who let the wilderness
seep into them.

**Skirmisher**

**Class:** ranger

**Modifies or Replaces:** Spells

**Description:** Many rangers rely on spells, but there are some who eschew aid from divine powers
for their own reasons.

**Spirit Ranger**

**Class:** ranger

**Modifies or Replaces:** Hunter's Bond; Camouflage

**Description:** Some rangers nurture a connection with the spirits that reside in all things.

**Stormwalker**

**Class:** ranger

**Modifies or Replaces:** Combat Style; Hunter's Bond; Swift Tracker; Quarry; Improved Evasion;
Improved Quarry

**Description:** Rangers who walk in the tempest unafraid draw the power of the storm into
themselves and become stormwalkers.

**Summit Sentinel**

**Class:** ranger

**Modifies or Replaces:** Combat Style; Favored Terrain; Swift Tracker; Hide in Plain Sight

**Description:** Some rangers eschew the path of the swift skirmisher and embrace the implacable
strength of the mountain.

**Sword-Devil**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Favored Enemy; Favored Terrain; Hunter's Bond; Spells;
Quarry; Improved Quarry; Master Hunter

**Description:** Agile, vengeful, and deadly, a sword-devil fights with precision and grace,
channeling the difficult lessons of a star-crossed life into unparalleled battle prowess.

**Tanglebriar Demonslayer**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Favored Enemy; Endurance; Spells; Quarry; Improved Quarry

**Description:** Though they are sworn foes of Treerazer and his kin, Tanglebriar demonslayers are
known to venture forth from Kyonin to broaden their expertise in the destruction of demons.

**Tidal Hunter**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; 6th-level Combat Style Feat; Track; Camouflage; Favored
Terrain; Woodland Stride; Improved Evasion

**Description:** The tidal hunter draws strength from the fish and other wildlife of the deep.

**Toxic Herbalist**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Endurance; Hunter's Bond; Swift Tracker; Quarry; Improved
Quarry

**Description:** Saviors and destroyers in equal measure, toxic herbalists use nature's bounty to
craft remedies and poisons.

**Toxophilite**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Combat Style; Endurance; Quarry; Improved Quarry

**Description:** The toxophilite emulates the sharpshooting rangers of legend, who could pin a fly
to the wall with a single shot or split one arrow with another.

**Transporter**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Favored Terrain; Hunter's Bond; Woodland Stride

**Description:** Transporters specialize in smuggling people as efficiently as possible through
harsh and difficult environments.

**Trapper**

**Class:** ranger

**Modifies or Replaces:** Spells

**Description:** A trapper is a ranger who focuses exclusively on traps, rather than learning
conventional magic.

**Trophy Hunter**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Combat Feat Style; Hunter's Bond

**Description:** Some rangers have taken up the mysteries of black powder in order to become big
game hunters.

**Urban Ranger**

**Class:** ranger

**Modifies or Replaces:** Favored Terrain; Endurance; Woodland Stride; Camouflage; Hide in Plain
Sight

**Description:** For the urban ranger, the streets and sewers of the city are just as dangerous as
the barren wastelands or the deep forests.

**Warden**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; Combat Style Feats; Hunter's Bond; Master Hunter

**Description:** All rangers have a bond with the wilderness, but the warden may have the strongest.
This protector sits guard in the middle of the wilderness, keeping a lookout for any dangers that
might spill from the deeper wilderness beyond, and protecting civilization from the savagery of
nature - and vice versa.

**Wave Warden**

**Class:** ranger

**Modifies or Replaces:** Track; Combat Style; Favored Terrain; Woodland Stride; Swift Tracker

**Description:** (Merfolk Only) The wave warden patrols beneath the sea, preserving the safety and
secrets of merfolk communities.

**Wild Hunter**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; Woodland Stride; Swift Tracker

**Description:** A wild hunter seeks to emulate the animals around him to keep him safe while he
tracks his prey.

**Wild Shadow**

**Class:** ranger

**Modifies or Replaces:** Track; Wild Empathy; Favored Terrain; Hunter's Bond; Woodland Stride;
Quarry; Camouflage; Improved Quarry

**Description:** (Half-Elf Only) The isolation that some half-elves feel leads them to live a life
of isolation amid the wild places of the world.

**Wild Soul**

**Class:** ranger

**Modifies or Replaces:** Code of Conduct; Favored Enemy; Swift Tracker; Quarry; Improved Quarry;
Master Hunter

**Description:** Wild souls hail from primitive roots in the wild and venture to more civilized
lands and learn their ways.

**Wild Stalker**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; 2nd-level Combat Style Feat; Hunter's Bond

**Description:** The wild stalker forsakes the bonds of community and lives in the trackless wilds
far from others of his kind, or perhaps grew up there, never knowing of civilization as anything
more than his enemy.

**Wilderness Explorer**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Wild Empathy; Hunter's Bond; Swift Tracker; Favored Terrain;
Quarry; Improved Quarry

**Description:** Wilderness explorers are adept at making peaceful contact with remote societies.

**Wilderness Medic**

**Class:** ranger

**Modifies or Replaces:** Wild Empathy; Endurance; Evasion; Hunter's Bond; Improved Evasion

**Description:** Wilderness medics know a variety of ways they can supply and preserve a rebellion
or similar movement without requiring any resources that might make them easier to track down.

**Witchguard**

**Class:** ranger

**Modifies or Replaces:** Class Skills; Hunter's Bond; Endurance; Spells; Woodland Stride

**Description:** Witchguards are the sworn defenders of the White Witches of Irrisen.

**Yokai Hunter**

**Class:** ranger

**Modifies or Replaces:** Favored Enemy; Woodland Stride; Camouflage

**Description:** Yokai hunters possess a supernatural tether to the spirit worlds that shroud mortal
existence.

### Archetypes by Feature

|Archetype|Alignment|Camouflage|Class Skills|Combat Style Feats|2nd-level Combat Style Feat|6th-level Combat Style Feat|Endurance|Evasion|Favored Enemy|1st-Level Favored Enemy|5th-Level Favored Enemy|10th-Level Favored Enemy|15th-Level Favored Enemy|20th-Level Favored Enemy|Favored Terrain|3rd-Level Favored Terrain|Hide in Plain Sight|Hunter's Bond|Improved Evasion|Master Hunter|Quarry|Improved Quarry|Spellcasting|Swift Tracker|Track|Weapon/_wbr_Armor Proficiency|Wild Empathy|Woodland Stride|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Abendego Diver](ref/arc-ranger/abendego-diver)||||||||||||||||X||||X||||X|X|X|X|X|
|[Battle Scout](ref/arc-ranger/battle-scout)||||||||||||X|X|X|||||X|X|||||||||
|[Beast Master](ref/arc-ranger/beast-master)||X||||X|||||||||||||X||||||||||
|[Blightwarden](ref/arc-ranger/blightwarden)|||||||X|||X|||||||X||||||||||X||
|[Bow Nomad](ref/arc-ranger/bow-nomad)||X||X||X|X|||||||||X||X|||||||||X||
|[Cinderwalker](ref/arc-ranger/cinderwalker)|||||||||||||||||X||X||||||||X|X|
|[Code Runner](ref/arc-ranger/code-runner)|||X||||||||||||||||X||||||||X||
|[Corpse Hunter](ref/arc-ranger/corpse-hunter)|||X|||||||X|||||||||||||X|X||||X|
|[Dandy](ref/arc-ranger/dandy)|||X|||||||X||||||X|||X||||X||||X|X|
|[Darklands Sailor](ref/arc-ranger/darklands-sailor)||X||||||||||||||X||X||||||X|X|||X|
|[Deep Walker](ref/arc-ranger/deep-walker)||X||||||||||||||X||X||||||||||X|
|[Divine Tracker](ref/arc-ranger/divine-tracker)|X||||||||||||||||||X||||||||X||
|[Dragon Hunter](ref/arc-ranger/dragon-hunter)|||X|||||||||X|X|X|X||||||||||X||||
|[Drake Warden](ref/arc-ranger/drake-warden)||||||||||||X|||||||X|||||X|||||
|[Dungeon Rover](ref/arc-ranger/dungeon-rover)|||X||||||||||||||||X|||||X|X||X|X|
|[Dusk Stalker](ref/arc-ranger/dusk-stalker)||X|X|||||||||||||X|||X||||||||||
|[Elemental Envoy](ref/arc-ranger/elemental-envoy)||||X||||||||||||X|||||||||||||
|[Falconer](ref/arc-ranger/falconer)||||||X|||||||||||||X||||||||X||
|[Flamewarden](ref/arc-ranger/flamewarden)||X||||||X|X||||||||||X|X|||X||||||
|[Fortune-Finder](ref/arc-ranger/fortune-finder)|||||||||||||||||||X|X|X|X|||X|||X|
|[Freebooter](ref/arc-ranger/freebooter)||||||||||X|||||||||X|||||||||X|
|[Galvanic Saboteur](ref/arc-ranger/galvanic-saboteur)||X|X|||||||X||||||X||X||||||X|||X|X|
|[Groom](ref/arc-ranger/groom)|||||||X||||||||||X||||||||X||||
|[Guide](ref/arc-ranger/guide)||||||||X|X|X|||||||||X||X|X|||||||
|[Guildbreaker](ref/arc-ranger/guildbreaker)|||X|||||||X|||||||||X||||||||X|X|
|[Hooded Champion](ref/arc-ranger/hooded-champion)||||X|||X|X|X||X||||||||||||||||X||
|[Horse Lord](ref/arc-ranger/horse-lord)||X||X||||||||||||||X|X||||||||||
|[Ilsurian Archer](ref/arc-ranger/ilsurian-archer)||||X|||||||||||||||||X|X|X|X|X||X||
|[Infiltrator](ref/arc-ranger/infiltrator)||||||||||||||||X|||||||||||||
|Jungle Lord||X|X|||||||X||||||X|||X|X|X|X|X|||X|||
|[Lantern Lighter](ref/arc-ranger/lantern-lighter)||X|||||X|||||||||X||X|||||||||X|X|
|[Nirmathi Irregular](ref/arc-ranger/nirmathi-irregular)||||||||||X||||||X|||||||X|||X|||
|[Planar Scout](ref/arc-ranger/planar-scout)|||X|||||X|X|||||||X|||X||||||||X||
|[Poison Darter](ref/arc-ranger/poison-darter)||||X||||||X|||||||||X|X|||||||X||
|[Raven Master](ref/arc-ranger/raven-master)||X|X||||||||||||||||X||||X|X|||X|X|
|[Realm Wanderer](ref/arc-ranger/realm-wanderer)|||X||||||||||||||||X|X||||X|X||||
|[Sable Company Marine](ref/arc-ranger/sable-company-marine)|||||||||||||||||||X||||||||||
|[Sentinel](ref/arc-ranger/sentinel)||||||X|||||||||||||X||X|X|||||X|X|
|[Shapeshifter](ref/arc-ranger/shapeshifter)||X||||||||||||||X||||X|||||||||
|[Skirmisher](ref/arc-ranger/skirmisher)|||||||||||||||||||||||X||||||
|[Spirit Ranger](ref/arc-ranger/spirit-ranger)||X|||||||||||||||||X||||||||||
|[Stormwalker](ref/arc-ranger/stormwalker)||||X|||||X||||||||||X||X|X||X|||||
|[Summit Sentinel](ref/arc-ranger/summit-sentinel)||||X||||||||||||X||X||||||X|||||
|Sword-Devil|||X|||||||X||||||X|||X|X|X|X|X||||||
|[Tanglebriar Demonslayer](ref/arc-ranger/tanglebriar-demonslayer)|||X||||X|||X|||||||||||X|X|X||||||
|[Tidal Hunter](ref/arc-ranger/tidal-hunter)||X||||X|||X|||||||X|||||||||X||X|X|
|[Toxic Herbalist](ref/arc-ranger/toxic-herbalist)|||||||X||||||||||||X||X|X||X|||X||
|[Toxophilite](ref/arc-ranger/toxophilite)||||X|||X||||||||||||||X|X|||||X||
|[Transporter](ref/arc-ranger/transporter)||||||||||||||||X|||X||||||||X|X|
|[Trapper](ref/arc-ranger/trapper)|||||||||||||||||||||||X||||||
|[Trophy Hunter](ref/arc-ranger/trophy-hunter)||||X|||||||||||||||X||||||||X||
|[Urban Ranger](ref/arc-ranger/urban-ranger)||X|||||X|||||||||X||X||||||||||X|
|[Warden](ref/arc-ranger/warden)||||X||||||X|||||||||X|X|||||||||
|[Wave Warden](ref/arc-ranger/wave-warden)||||X||||||||||||X||||||||X|X|||X|
|[Wild Hunter](ref/arc-ranger/wild-hunter)||||||||||X||||||||||||||X||||X|
|[Wild Shadow](ref/arc-ranger/wild-shadow)||X||||||||||||||X|||X||X|X|||X||X|X|
|[Wild Soul](ref/arc-ranger/wild-soul)||||||||||X||||||||||X|X|X||X|||||
|[Wild Stalker](ref/arc-ranger/wild-stalker)|||||X|||||X|||||||||X||||||||||
|[Wilderness Explorer](ref/arc-ranger/wilderness-explorer)|||X|||||||||||||X|||X||X|X||X|||X||
|[Wilderness Medic](ref/arc-ranger/wilderness-medic)|||||||X|X|X||||||||||X||||||||X||
|[Witchguard](ref/arc-ranger/witchguard)|||X||||X||||||||||||X||||X|||||X|
|[Yokai Hunter](ref/arc-ranger/yokai-hunter)||X||||||||X||||||||||||||||||X|

### Favored Class Bonuses

_The favored class options for ranger are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
