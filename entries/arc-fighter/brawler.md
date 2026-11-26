+++
id = "ref/arc-fighter/brawler"
kind = "archetype"
title = "Brawler"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Brawler"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brawler", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "close-control", level = 2 },
  { anchor = "close-combatant", level = 3 },
  { anchor = "menacing-stance", level = 7 },
  { anchor = "no-escape", level = 9 },
  { anchor = "stand-still", level = 13 },
  { anchor = "weapon-mastery" },
]
trades = [
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["close-control"] },
  { replaces = "Weapon training 1 and 2", feature = "weapon-training", levels = [5, 9], by = ["close-combatant"] },
  { replaces = "Armor training 2, 3, and 4", feature = "armor-training", levels = [7, 11, 15], by = ["menacing-stance"] },
  { replaces = "armor mastery", feature = "armor-mastery", by = ["menacing-stance"] },
  { replaces = "Weapon training 3 and 4", feature = "weapon-training", levels = [13, 17], by = ["no-escape"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

All melee is up close and personal, but some warriors bring it as close as they can get. Brawlers
can be found anywhere, among all races and societies. A brawler could be hired muscle in a tavern, a
local crime syndicate enforcer, or a hotheaded recruit among the ranks of a baron's guard. Often
brawlers' in-your-face attitudes are as powerful as their tactics.

## Close Control (Ex) {#close-control}

At 2nd level, a brawler becomes skilled at forcefully moving his opponent around the battlefield.
The brawler gains a +1 bonus on [bull rush](ref/rule/bull-rush), [drag](ref/rule/drag), and
[reposition](ref/rule/reposition) combat maneuver checks. The brawler also gains a +1 bonus to CMD
when attacked with the bull rush, drag, and reposition maneuvers. These bonuses increase by +1 for
every four levels after 2nd (to a maximum of +5 at 18th level). This ability replaces armor
training 1.

## Close Combatant (Ex) {#close-combatant}

At 3rd level, a brawler gains a +1 bonus on attack rolls and a +3 bonus on damage rolls with weapons
in the close [weapon group](ref/ability/weapon-groups). Both of these bonuses increase by +1 for
every four levels beyond 3rd (to a maximum of +5 on attack rolls and +7 on damage rolls at 19th
level). This ability replaces weapon training 1 and 2.

## Menacing Stance (Ex) {#menacing-stance}

At 7th level, a brawler constantly harries and distracts his enemies. While adjacent to the brawler,
enemies take a -1 penalty on attack rolls and a -4 penalty on
[concentration](ref/rule/concentration) checks. These penalties increase by 1 for every four levels
after 7th level (to a maximum of -4 on attack rolls and -7 on concentration checks at 19th level).
Creatures do not take these penalties if the brawler is dazed, helpless, staggered, stunned, or
unconscious. This ability replaces armor training 2, 3, and 4 and armor mastery.

## No Escape (Ex) {#no-escape}

At 9th level, taking [a 5-foot step](ref/rule/take-5-foot-step) out of the area of a brawler's
menacing stance or moving out of the area of a brawler's menacing stance with a
[withdraw](ref/rule/withdraw) action provokes an attack of opportunity from the brawler. This
ability replaces weapon training 3 and 4.

## Stand Still {#stand-still}

At 13th level, a brawler gains [Stand Still](ref/feat/stand-still) as a bonus feat, even if he does
not have the [Combat Reflexes](ref/feat/combat-reflexes) feat. If the brawler already has the Stand
Still feat, he can take any other combat feat instead. Furthermore, he gains a bonus equal to 1/2
his fighter level on combat maneuver checks when using the Stand Still feat.

## Weapon Mastery (Ex) {#weapon-mastery}

A brawler must select a close weapon for this ability.

## Expanded Weapon Groups {#expanded-weapon-groups}

This book and the _Advanced Player's Guide_ present a number of weapons not on the weapon group
lists in the _Core Rulebook_. Below is an update of that list, with all the weapons from those two
books as well as new weapons introduced in this book. It also presents two new groups: firearms and
siege weapons. Weapons with one asterisk (\*) can be found in the _Advanced Player's Guide_. Weapons
with two asterisks (\*\*) can be found in this book.

Weapon groups are defined as follows (GMs may add other weapons to these groups, or add entirely new
groups):

_Axes_: bardiche\*, battleaxe, dwarven waraxe, greataxe, handaxe, heavy pick, hooked axe\*\*,
knuckle axe\*\*, light pick, mattock\*\*, orc double axe, pata\*\*, and throwing axe

_Blades, Heavy_: bastard sword, chakram\*, double chicken saber\*\*, double walking stick
katana\*\*, elven curve blade, falcata\*, falchion, greatsword, great terbutje\*\*, katana\*\*,
khopesh\*, longsword, nine-ring broadsword\*\*, nodachi\*\*, scimitar, scythe, seven-branched
sword\*\*, shotel\*\*, temple sword\*, terbutje\*\*, and two-bladed sword

_Blades, Light_: bayonet\*, butterfly sword\*\*, dagger, gladius\*\*, kama, kerambit\*\*, kukri,
pata\*\*, quadrens\*\*, rapier, short sword, sica\*\*, sickle, starknife, swordbreaker dagger\*,
sword cane\*, and wakizashi\*\*

_Bows_: composite longbow, composite shortbow, longbow, and shortbow

_Close_: bayonet\*, brass knuckles\*, cestus\*\*, dan bong\*\*, emei piercer\*\*, fighting fan\*\*,
gauntlet, heavy shield, iron brush\*\*, light shield, madu\*\*, mere club\*\*, punching dagger, sap,
scizore\*\*, spiked armor, spiked gauntlet, spiked shield, tekko-kagi\*\*, tonfa\*\*, unarmed
strike, wooden stake\*, and wushu dart\*\*

_Crossbows_: double crossbow\*, hand crossbow, heavy crossbow, heavy repeating crossbow, light
crossbow, light repeating crossbow, and tube arrow shooter\*\*

_Double_: dire flail, dwarven urgrosh, gnome hooked hammer, orc double axe, quarterstaff, and
two-bladed sword

_Firearms_: all one-handed\*\*, two-handed\*\*, and siege firearms\*\*

_Flails_: chain spear\*, dire flail, double chained kama\*\*, flail, flying blade\*\*, heavy flail,
kusarigama\*\*, kyoketsu shoge\*\*, meteor hammer\*\*, morningstar, nine-section whip\*\*, nunchaku,
sansetsukon\*\*, scorpion whip\*\*, spiked chain, urumi\*\*, and whip

_Hammers_: aklys\*\*, battle aspergillum\*, club, greatclub, heavy mace, light hammer, light mace,
mere club\*\*, taiaha\*\*, tetsubo\*\*, wahaika\*\*, and warhammer

_Monk_: bo staff\*\*, brass knuckles\*\*, butterfly sword\*\*, cestus\*, dan bong\*\*, double
chained kama\*\*, double chicken saber\*\*, emei piercer\*\*, fighting fan\*\*, jutte\*\*, kama,
kusarigama\*\*, kyoketsu shoge\*\*, lungshuan tamo\*\*, monk's spade\*\*, nine-ring broadsword\*\*,
nine-section whip\*\*, nunchaku, quarterstaff, rope dart\*\*, sai, sansetsukon\*\*, seven-branched
sword\*\*, shang gou\*\*, shuriken, siangham, tiger fork\*\*, tonfa\*\*, tri-point double-edged
sword\*\*, unarmed strike, urumi\*\*, wushu dart\*\*

_Natural_: unarmed strike and all natural weapons, such as bite, claw, gore, tail, and wing

_Polearms_: bardiche\*, bec de corbin\*, bill\*, glaive, glaive-guisarme\*, guisarme, halberd,
hooked lance\*\*, lucerne hammer\*, mancatcher\*, monk's spade\*\*, naginata\*\*, nodachi\*\*,
ranseur, rohomphaia\*\*,tepoztopili\*\*, and tiger fork\*\*

_Spears_: amentum\*\*, boar spear\*, javelin, harpoon\*\*, lance, longspear, pilum\*, shortspear,
sibat\*\*, spear, tiger fork\*\*, and trident

_Thrown_: aklys\*\*, amentum\*\*, atlatl\*\*, blowgun, bolas, boomerang\*, chakram\*, club, dagger,
dart, halfling sling staff, harpoon\*\*, javelin, lasso\*, kestros\*\*, light hammer, net, poisoned
sand tube\*\*, rope dart\*\*, shortspear, shuriken, sibat\*\*, sling, spear, starknife, throwing
axe, throwing shield\*\*, trident, and wushu dart\*\*

_Siege Engines_: all siege engines\*\*
