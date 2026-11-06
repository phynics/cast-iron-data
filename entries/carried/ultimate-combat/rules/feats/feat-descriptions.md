+++
id = "ref/carried/ultimate-combat/rules/feats/feat-descriptions"
kind = "rule"
title = "Feat Descriptions"
source_ids = ["ultimate-combat"]
section = ["Rules", "Feats"]
parent = "ref/carried/ultimate-combat/rules/feats"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Rules/Feats/Feat Descriptions", path = "ultimate_combat/rules/feats.json" },
]

[fields]
kind = "none"
+++

All the feat descriptions in this chapter utilize the following format.

## Feat Name {#feat-name}

At the top of the feat entry, you will find the feat's name followed by parentheses listing any type
or types the feat belongs to. A basic description of what the feat does appears under the name of
the feat and its types, if any.

## Prerequisite {#prerequisite}

This line lists any minimum ability scores, class features, feats, minimum base attack bonus,
minimum number of ranks in one or more skills, or other requirements for a character to take the
feat. This entry is absent if a feat has no prerequisites. A feat may have multiple prerequisites.
See the feat descriptions for full details.

## Benefit {#benefit}

The benefit is what a feat enables a character (“you” in the feat description) to do. If a character
has the same feat more than once, its benefits do not stack unless indicated in the feat's Special
line.

## Normal {#normal}

This line indicates what a character without this feat is limited to or restricted from doing. If
not having the feat causes no particular drawback, this entry is absent.

## Special {#special}

This line lists special features of the feat, such as, but not limited to, whether or not you can
take the feat more than once, or whether the feat allows members of specific classes to gain
additional benefits.

## Table: Feats {#table-feats}

::: table
caption = "Table: Feats"
head = [
  [
    { text = "Feat", header = true },
    { text = "Prerequisites", header = true },
    { text = "Benefit", header = true },
  ],
]
body = [
  [
    { text = "Adder Strike\\*" },
    { text = "Poison use class feature, Improved Unarmed Strike, Craft (alchemy) 1 rank" },
    { text = "May apply contact poison to unarmed strikes" },
  ],
  [
    { text = "Pinpoint Poisoner\\*" },
    { text = "Adder Strike, Two-Weapon Fighting or flurry of blows class feature, Craft (alchemy) 6 ranks" },
    { text = "When using Adder Strike, you may poison two blowgun darts that can be used in melee" },
  ],
  [
    { text = "Adept Champion" },
    { text = "Smite evil class feature, base attack bonus +5" },
    { text = "Trade smite evil damage for bonus on combat maneuver checks" },
  ],
  [
    { text = "Amateur Gunslinger\\*" },
    { text = "No levels in a class with grit class feature" },
    { text = "Gain limited amount of grit and access to gunslinger deeds" },
  ],
  [
    { text = "Arc Slinger\\*" },
    { text = "Point-Blank Shot, proficient with sling or halfling sling staff" },
    { text = "Reduce ranged attack penalties due to range by 2" },
  ],
  [
    { text = "Betrayer" },
    { text = "Persuasive, Quick Draw, base attack bonus +3" },
    { text = "Gain free attack upon successful Diplomacy skill check" },
  ],
  [
    { text = "Binding Throw\\*" },
    { text = "Improved Grapple, Improved Trip, _Ki_ Throw" },
    { text = "After successful _Ki_ Throw, you may attempt to grapple" },
  ],
  [
    { text = "Bludgeoner\\*" },
    { text = "—" },
    { text = "Inflict nonlethal damage with bludgeoning weapons" },
  ],
  [
    { text = "Body Shield\\*" },
    { text = "Improved Grapple, base attack bonus +6" },
    { text = "Gain cover against attacks while grappling" },
  ],
  [
    { text = "Bolstered Resilience" },
    { text = "[Damage reduction](ref/rule/damage-reduction)" },
    { text = "Increase DR against a single attack" },
  ],
  [
    { text = "Branded for Retribution" },
    { text = "Bane class feature" },
    { text = "Grant ally's weapon the bane quality against a branded opponent" },
  ],
  [
    { text = "Break Guard\\*" },
    { text = "Improved Disarm, Two-Weapon Fighting" },
    { text = "May attack opponent you attempted to disarm with your second weapon" },
  ],
  [
    { text = "Cartwheel Dodge" },
    { text = "Improved evasion class feature, Acrobatics 12 ranks" },
    { text = "With a successful evasion you may move half your speed" },
  ],
  [
    { text = "Channeled Revival" },
    { text = "Channel positive energy 6d6" },
    { text = "May expend channel energy to cast _[breath of life](ref/spell/breath-of-life)_" },
  ],
  [
    { text = "Channeling Scourge" },
    { text = "Inquisitor channel energy class feature" },
    { text = "Inquisitor levels count as cleric levels for channeling damage" },
  ],
  [
    { text = "Charging Hurler\\*" },
    { text = "Point-Blank Shot" },
    { text = "May use charge rules to make thrown weapon attack" },
  ],
  [
    { text = "Improved Charging Hurler" },
    { text = "Charging Hurler" },
    { text = "Your target may be at any range" },
  ],
  [
    { text = "Chokehold\\*" },
    { text = "Improved Grapple, base attack bonus +6 or monk level 5th" },
    { text = "May pin grappled opponent one size category larger than you" },
  ],
  [
    { text = "Cleaving Finish\\*" },
    { text = "Cleave" },
    { text = "Make additional attack if opponent is knocked out." },
  ],
  [
    { text = "Improved Cleaving Finish" },
    { text = "Cleaving Finish, Great Cleave, base attack bonus +6" },
    { text = "May use Cleaving Finish any number of times/round" },
  ],
  [
    { text = "Close-Quarters Thrower\\*" },
    { text = "Dodge, Weapon Focus with selected thrown weapon" },
    { text = "Attacks with selected weapons do not provoke attacks of opportunity" },
  ],
  [
    { text = "Clustered Shots\\*" },
    { text = "Point-Blank Shot, Precise Shot, base attack bonus +6" },
    { text = "Total damage from full-round ranged attacks before applying DR" },
  ],
  [
    { text = "Combat Style Master\\*" },
    { text = "Improved Unarmed Strike, two more style feats, base attack bonus +6 or monk level 5th" },
    { text = "May switch styles as a free action" },
  ],
  [
    { text = "Contingent Channeling" },
    { text = "True healer class feature, Selective Channeling" },
    { text = "May transfer positive energy to ally who can use it to heal" },
  ],
  [
    { text = "Crusader's Fist\\*" },
    { text = "Lay on hands or touch of corruption class feature, Improved Unarmed Strike, base attack bonus +6" },
    { text = "May use lay on hands or touch of corruption upon successful Unarmed Strike" },
  ],
  [
    { text = "Crusader's Flurry" },
    { text = "Channel energy and flurry of blows class feature, Weapon Focus with deity's favored weapon" },
    { text = "May use flurry of blows with deity's favored melee weapon" },
  ],
  [
    { text = "Crushing Blow" },
    { text = "Stunning Fist" },
    { text = "Stunning Fist reduces target's AC" },
  ],
  [
    { text = "Deadly Finish\\*" },
    { text = "Base attack bonus +11" },
    { text = "Foes you knock out must make a Fort save or die" },
  ],
  [
    { text = "Death from Above\\*" },
    { text = "—" },
    { text = "Gain +5 bonus on attack rolls when charging from higher ground or flying" },
  ],
  [
    { text = "Death or Glory\\*" },
    { text = "Power Attack, base attack bonus +6" },
    { text = "Gain +4 on attack, damage, and critical rolls vs. Large or larger opponents" },
  ],
  [
    { text = "Deathless Initiate\\*" },
    { text = "Str 13, Con 13, orc or half-orc, Diehard, base attack bonus +6" },
    { text = "Not staggered while using Diehard; gain +2 on melee damage rolls" },
  ],
  [
    { text = "Deathless Master\\*" },
    { text = "Con 15, Deathless Initiate, Ironhide, base attack bonus +9" },
    { text = "Do not lose hit points while using Diehard" },
  ],
  [
    { text = "Deathless Zealot\\*" },
    { text = "Con 17, Deathless Master, base attack bonus +12" },
    { text = "Foes must reroll critical confirmation attacks" },
  ],
  [
    { text = "Deceptive Exchange" },
    { text = "Improved Feint" },
    { text = "Upon successful feint, you may force opponent to accept an object" },
  ],
  [
    { text = "Defensive Weapon Training\\*" },
    { text = "Int 13, base attack bonus +5" },
    { text = "Gain +2 dodge bonus against a single fighter weapon group" },
  ],
  [
    { text = "Destructive Dispel" },
    { text = "Ability to cast _[dispel magic](ref/spell/dispel-magic)_ or _[greater dispel magic](ref/spell/dispel-magic-greater)_, caster level 11th" },
    { text = "Upon successful dispel, opponent must save or is stunned" },
  ],
  [
    { text = "Devastating Strike\\*" },
    { text = "Vital Strike, base attack bonus +9" },
    { text = "Deal extra damage when using Vital Strike bonus" },
  ],
  [
    { text = "Improved Devastating Strike" },
    { text = "Devastating Strike, base attack bonus +13" },
    { text = "Gain bonus on rolls to confirm critical hits" },
  ],
  [
    { text = "Dimensional Agility" },
    { text = "Abundant step class feature or ability to cast _[dimension door](ref/spell/dimension-door)_" },
    { text = "May take any additional actions remaining after using _[dimension door](ref/spell/dimension-door)_ or abundant step" },
  ],
  [
    { text = "Dimensional Assault" },
    { text = "Dimensional Agility" },
    { text = "May use _[dimension door](ref/spell/dimension-door) _or abundant step as part of a charge action" },
  ],
  [
    { text = "Dimensional Dervish" },
    { text = "Dimensional Assault, base attack bonus +6" },
    { text = "During full-attack action, you may cast _[dimension door](ref/spell/dimension-door)_ or use abundant step as a swift action" },
  ],
  [
    { text = "Dimensional Maneuvers" },
    { text = "Dimensional Dervish, base attack bonus +9" },
    { text = "Gain +4 on combat maneuver checks while using Dimensional Dervish" },
  ],
  [
    { text = "Dimensional Savant" },
    { text = "Dimensional Dervish, base attack bonus +9" },
    { text = "Provide flanking from all squares you attack from when using Dimensional Dervish" },
  ],
  [
    { text = "Discordant Voice" },
    { text = "Bardic performance class feature, Perform (oratory or sing) 10 ranks" },
    { text = "When using bardic performance, allies deal 1d6 extra sonic damage" },
  ],
  [
    { text = "Disengaging Feint\\*" },
    { text = "Improved Feint" },
    { text = "Feint lets you move your speed without provoking attacks of opportunity" },
  ],
  [
    { text = "Disengaging Flourish\\*" },
    { text = "Disengaging Feint" },
    { text = "Successful feint causes your starting square to not count as threatened" },
  ],
  [
    { text = "Disengaging Shot\\*" },
    { text = "Disengaging Feint, Dodge, Mobility" },
    { text = "When using Disengaging Flourish, you may make a single attack" },
  ],
  [
    { text = "Disorienting Maneuver" },
    { text = "Dodge, Acrobatics 5 ranks" },
    { text = "After successful tumble through opponent's square, gain +2 on attack rolls vs. that opponent" },
  ],
  [
    { text = "Dispel Synergy" },
    { text = "Spellcraft 5 ranks" },
    { text = "_[Dispel magic](ref/spell/dispel-magic)_ target takes a –2 penalty on saves" },
  ],
  [
    { text = "Dispelling Critical\\*" },
    { text = "Arcane Strike, base attack bonus +11, ability to cast _[dispel magic](ref/spell/dispel-magic)_" },
    { text = "After critical hit, you may cast _[dispel magic](ref/spell/dispel-magic)_" },
  ],
  [
    { text = "Dispelling Fist" },
    { text = "Improved Unarmed Strike, ability to cast _[dispel magic](ref/spell/dispel-magic)_, base attack bonus +11, caster level 7th" },
    { text = "May cast _[dispel magic](ref/spell/dispel-magic)_ as a swift action after an attack" },
  ],
  [
    { text = "Disposable Weapon" },
    { text = "Weapon Proficiency, base attack bonus +1" },
    { text = "Break a fragile weapon to confirm a critical hit" },
  ],
  [
    { text = "Disruptive Recall" },
    { text = "Spell recall class feature, Spellcraft 5 ranks" },
    { text = "Use spell recall after disrupting an opponent's spell" },
  ],
  [
    { text = "Distance Thrower\\*" },
    { text = "Str 13" },
    { text = "Reduce ranged penalties for thrown weapons by 2" },
  ],
  [
    { text = "Domain Strike\\*" },
    { text = "Domain class feature, Improved Unarmed Strike" },
    { text = "Use a domain power through unarmed strike" },
  ],
  [
    { text = "Double Bane" },
    { text = "Bane class feature, Two-Weapon Fighting" },
    { text = "Apply your bane to a second weapon" },
  ],
  [
    { text = "Drag Down\\*" },
    { text = "Improved Trip" },
    { text = "If tripped, you can attempt a trip against that foe" },
  ],
  [
    { text = "Elusive Redirection" },
    { text = "Elusive target class feature, Combat Expertise, Improved Unarmed Strike, flowing monk level 12th" },
    { text = "When you successfully avoid damage, spend 1 _ki_ point to redirect attack back at opponent" },
  ],
  [
    { text = "Extra Bane" },
    { text = "Bane class feature" },
    { text = "May use bane ability 3 additional times per day" },
  ],
  [
    { text = "False Opening\\*" },
    { text = "Dodge, Close Quarters Thrower or Point-Blank Master, Weapon Focus with selected ranged weapon" },
    { text = "May choose to provoke attacks of opportunity; gain +4 AC vs. attacks" },
  ],
  [
    { text = "Felling Escape\\*" },
    { text = "Improved Trip" },
    { text = "Trip a foe when you break a grapple" },
  ],
  [
    { text = "Felling Smash\\*" },
    { text = "Improved Trip, Power Attack, base attack bonus +6" },
    { text = "Trip a foe when you make a power attack" },
  ],
  [
    { text = "Feral Combat Training\\*" },
    { text = "Improved Unarmed Strike, Weapon Focus (natural weapon)" },
    { text = "Use Improved Unarmed Strike feats with natural weapons" },
  ],
  [
    { text = "Field Repair" },
    { text = "Craft 4 ranks" },
    { text = "Take no penalty for repairs made with improvised materials" },
  ],
  [
    { text = "Final Embrace\\*" },
    { text = "Str 13, Int 3; base attack bonus +3; naga, serpentfolk, or constrict special attack" },
    { text = "Gain constrict and grab special attacks" },
  ],
  [
    { text = "Final Embrace Horror\\*" },
    { text = "Str 15; Ability Focus (constrict); Final Embrace; base attack bonus +6" },
    { text = "Creatures that take constriction damage from you are also shaken" },
  ],
  [
    { text = "Final Embrace Master\\*" },
    { text = "Str 17; Final Embrace Horror; base attack bonus +9" },
    { text = "Your constrict attack deals double the number of damage dice" },
  ],
  [
    { text = "Flanking Foil\\*" },
    { text = "—" },
    { text = "Foes you strike lose their flanking bonus against you" },
  ],
  [
    { text = "Fortified Armor Training\\*" },
    { text = "Proficient with armor or shield" },
    { text = "Break armor or shield to turn critical hit into a normal hit" },
  ],
  [
    { text = "Furious Finish" },
    { text = "Rage class feature, Vital Strike, base attack bonus +6" },
    { text = "Deal maximum damage and end your rage" },
  ],
  [
    { text = "Gory Finish\\*" },
    { text = "Dazzling Display, Weapon Focus" },
    { text = "Make an Intimidate check if you reduce an opponent to negative hit points" },
  ],
  [
    { text = "Greater Channel Smite" },
    { text = "Channel Smite, base attack bonus +8" },
    { text = "Can exchange channel positive energy to create pool of damage dice" },
  ],
  [
    { text = "Guided Hand" },
    { text = "Channel Smite, proficiency with deity's chosen weapon" },
    { text = "May use Wisdom modifier for attack rolls with favored weapon" },
  ],
  [
    { text = "Gunsmithing" },
    { text = "—" },
    { text = "May create, repair, and restore firearms" },
  ],
  [
    { text = "Hammer the Gap\\*" },
    { text = "Base attack bonus +6" },
    { text = "With a full-attack action, each hit against the same opponent deals extra damage" },
  ],
  [
    { text = "Harmonic Sage" },
    { text = "Bardic performance class feature, Knowledge (engineering) 5 ranks" },
    { text = "Gain extra abilities when performing within an artificial structure" },
  ],
  [
    { text = "Haunted Gnome\\*" },
    { text = "Cha 13, gnome magic racial trait, Knowledge (arcana) 1 rank" },
    { text = "Gain _[haunted fey aspect](ref/spell/haunted-fey-aspect)_" },
  ],
  [
    { text = "Haunted Gnome Assault\\*" },
    { text = "Haunted Gnome, Knowledge (arcana) 3 ranks" },
    { text = "Gain independent use of gnome magic" },
  ],
  [
    { text = "Haunted Gnome Shroud\\*" },
    { text = "Haunted Gnome Assault, Knowledge (arcana) 6 ranks" },
    { text = "Gain additional use of gnome magic" },
  ],
  [
    { text = "Hex Strike\\*" },
    { text = "Hex class feature, Improved Unarmed Strike" },
    { text = "Upon successful unarmed strike, you may use a hex" },
  ],
  [
    { text = "Horse Master\\*" },
    { text = "Expert trainer class feature, Ride 6 ranks" },
    { text = "Use your character level to determine powers and abilities for your mount" },
  ],
  [
    { text = "Impact Critical Shot\\*" },
    { text = "Dex 13, Point-Blank Shot, base attack bonus +9" },
    { text = "You can bull rush on a critical hit" },
  ],
  [
    { text = "Impaling Critical\\*" },
    { text = "Critical Focus, Weapon Specialization with piercing weapon, base attack bonus +11" },
    { text = "May impale and deal extra damage to opponent with a critical hit" },
  ],
  [
    { text = "Improved Impaling Critical\\*" },
    { text = "Impaling Critical, base attack bonus +13" },
    { text = "Impaled opponent must succeed at a grapple maneuver to pull your weapon out" },
  ],
  [
    { text = "Improved Two-Weapon Feint\\*" },
    { text = "Combat Expertise, Improved Two-Weapon Fighting" },
    { text = "Make a Bluff check instead of your first attack" },
  ],
  [
    { text = "Instant Judgment" },
    { text = "Second judgment class feature" },
    { text = "May pronounce or change a judgment as an immediate action" },
  ],
  [
    { text = "Intimidating Bane" },
    { text = "Bane class feature, Dazzling Display, character level 8th" },
    { text = "Gain +2 bonus on Dazzling Display while bane is active" },
  ],
  [
    { text = "Jawbreaker\\*" },
    { text = "Heal 6 ranks, Improved Unarmed Strike, Stunning Fist" },
    { text = "With successful Stunning Fist, you may cripple opponent's mouth" },
  ],
  [
    { text = "Bonebreaker\\*" },
    { text = "Improved Grapple, Jawbreaker, Heal 9 ranks" },
    { text = "Deal Str or Dex damage when using Stunning Fist" },
  ],
  [
    { text = "Neckbreaker\\*" },
    { text = "Bonebreaker, Greater Grapple, Improved Grapple, Improved Unarmed Strike, Jawbreaker, Stunning Fist, Heal 12 ranks" },
    { text = "May deal Str or Dex damage to pinned opponent" },
  ],
  [
    { text = "Knockout Artist" },
    { text = "Sneak attack class feature, Improved Unarmed Strike" },
    { text = "Gain +2 damage per sneak attack when dealing nonlethal sneak damage" },
  ],
  [
    { text = "Landing Roll\\*" },
    { text = "Mobility" },
    { text = "If tripped, move 5 feet as an immediate action" },
  ],
  [
    { text = "Master Combat Performer" },
    { text = "Performing Combatant or 3 performance feats, base attack bonus +6" },
    { text = "Make a performance combat check as a free action" },
  ],
  [
    { text = "Maximized Spellstrike" },
    { text = "Maximized magic magus arcana, weapon expertise class feature or Quick Draw" },
    { text = "Maximize spellstrike by spending 3 arcana pool points" },
  ],
  [
    { text = "Menacing Bane" },
    { text = "Bane class feature" },
    { text = "May imbue weapon with _menacing_ special quality" },
  ],
  [
    { text = "Merciful Bane" },
    { text = "Bane class feature" },
    { text = "Switch damage from lethal to nonlethal as a swift action" },
  ],
  [
    { text = "Monastic Legacy\\*" },
    { text = "Improved Unarmed Strike, still mind class feature" },
    { text = "Count half your non-monk levels as monk levels for unarmed strike damage" },
  ],
  [
    { text = "Moonlight Stalker\\*" },
    { text = "[Darkvision](ref/rule/darkvision) or [low-light vision](ref/rule/low-light-vision) racial trait, Bluff 3 ranks, Blind-Fight, Combat Expertise" },
    { text = "Gain +2 on damage and attack rolls when you have concealment vs. foe" },
  ],
  [
    { text = "Moonlight Stalker Feint\\*" },
    { text = "Bluff 6 ranks, Moonlight Stalker" },
    { text = "Make a Bluff check to feint with concealment vs. foe" },
  ],
  [
    { text = "Moonlight Stalker Master\\*" },
    { text = "Bluff 9 ranks, Improved Feint, Moonlight Stalker Feint" },
    { text = "While concealed, miss chance increases by 10%" },
  ],
  [
    { text = "Net Adept\\*" },
    { text = "Exotic Weapon Proficiency (net), base attack bonus +1" },
    { text = "May treat a net as a one-handed weapon" },
  ],
  [
    { text = "Net and Trident\\*" },
    { text = "Dex 15, Net Adept, Two-Weapon Fighting" },
    { text = "May wield a one-handed or light weapon with a net" },
  ],
  [
    { text = "Net Maneuvering\\*" },
    { text = "Net Adept, base attack bonus +3" },
    { text = "May use a net to trip or disarm" },
  ],
  [
    { text = "Net Trickery\\*" },
    { text = "Net Adept, Net Maneuvering, base attack bonus +6" },
    { text = "May use a net to blind your opponent" },
  ],
  [
    { text = "Nightmare Fist\\*" },
    { text = "Improved Unarmed Strike, Intimidate 1 rank, ability to create magical darkness" },
    { text = "While fighting in magical darkness, you deal +2 damage" },
  ],
  [
    { text = "Nightmare Weaver\\*" },
    { text = "Nightmare Fist, Intimidate 2 ranks" },
    { text = "Can demoralize foes while casting _[darkness](ref/spell/darkness)_." },
  ],
  [
    { text = "Nightmare Striker\\*" },
    { text = "Nightmare Weaver, Stunning Fist, Heal 5 ranks, ability to cast _[faerie fire](ref/spell/faerie-fire)_" },
    { text = "While opponent is under the effects of _[faerie fire](ref/spell/faerie-fire)_, your DC for Stunning Fist increases by 2" },
  ],
  [
    { text = "Opening Volley\\*" },
    { text = "—" },
    { text = "Successful ranged attack grants +4 on next melee attack roll" },
  ],
  [
    { text = "Passing Trick\\*" },
    { text = "Improved Feint, Mobility, size Small or smaller" },
    { text = "Successful Acrobatics check allows you to feint" },
  ],
  [
    { text = "Performance Weapon Mastery\\*" },
    { text = "—" },
    { text = "All weapons you are proficient with act as if they had the performance quality" },
  ],
  [
    { text = "Performing Combatant\\*" },
    { text = "Dazzling Display, any one Performance feat" },
    { text = "Can make combat performance checks in any combat" },
  ],
  [
    { text = "Pin Down\\*" },
    { text = "Combat Reflexes, fighter level 11th" },
    { text = "Opponents that take 5-foot step or withdraw provoke attack of opportunity from you" },
  ],
  [
    { text = "Pinning Knockout\\*" },
    { text = "Dex 13, Greater Grapple, base attack bonus +9 or monk level 9th" },
    { text = "Against a pinned opponent, you may double nonlethal damage with grapple check" },
  ],
  [
    { text = "Pinning Rend\\*" },
    { text = "Dex 13, Greater Grapple, Improved Grapple, Improved Unarmed Strike, base bonus +9 or monk level 9th" },
    { text = "Against pinned opponent, you may deal bleed damage with Grapple check" },
  ],
  [
    { text = "Planar Wild Shape" },
    { text = "Wild shape class feature, Knowledge (planes) 5 ranks" },
    { text = "May add the celestial or fiendish template to your animal form" },
  ],
  [
    { text = "Prone Shooter\\*" },
    { text = "Weapon Focus (crossbow or firearm), base attack bonus +1" },
    { text = "Take a reduced penalty to your AC against melee attacks while prone" },
  ],
  [
    { text = "Prone Slinger\\*" },
    { text = "—" },
    { text = "May use a sling while prone" },
  ],
  [
    { text = "Quick Bull Rush\\*" },
    { text = "Improved Bull Rush, base attack bonus +6" },
    { text = "May bull rush in place of one of your melee attacks" },
  ],
  [
    { text = "Quick Dirty Trick\\*" },
    { text = "Improved Dirty Trick, base attack bonus +6" },
    { text = "May perform a dirty trick in place of one of your melee attacks" },
  ],
  [
    { text = "Quick Drag\\*" },
    { text = "Improved Drag, base attack bonus +6" },
    { text = "May perform a drag maneuver in place of one of your melee attacks" },
  ],
  [
    { text = "Quick Reposition\\*" },
    { text = "Improved Reposition, base attack bonus +6" },
    { text = "May reposition in place of one of your melee attacks" },
  ],
  [
    { text = "Quick Steal\\*" },
    { text = "Improved Steal, base attack bonus +6" },
    { text = "May steal in place of one of your melee attacks" },
  ],
  [
    { text = "Raging Brutality" },
    { text = "Rage class feature, Power Attack, base attack bonus +12" },
    { text = "Add Constitution bonus on damage rolls" },
  ],
  [
    { text = "Raging Deathblow" },
    { text = "Greater rage class feature" },
    { text = "Rend a dying foe and gain one round of rage" },
  ],
  [
    { text = "Raging Hurler" },
    { text = "Rage class feature, Throw Anything" },
    { text = "Throw a two-handed weapon as a standard action" },
  ],
  [
    { text = "Raging Throw" },
    { text = "Con 13, rage class feature, Improved Bull Rush, base attack bonus +6" },
    { text = "Add Con bonus on checks to bull rush" },
  ],
  [
    { text = "Rapid Grappler\\*" },
    { text = "Dex 13, Greater Grapple, Improved Grapple, Improved Unarmed Strike, base attack bonus +9 or monk level 9th" },
    { text = "Spend a swift action to make a combat maneuver check to grapple while using Greater Grapple." },
  ],
  [
    { text = "Rapid Reload\\*" },
    { text = "Weapon Proficiency (crossbow) or Exotic Weapon Proficiency (firearms)" },
    { text = "Reload your weapon quickly" },
  ],
  [
    { text = "Rebounding Leap\\*" },
    { text = "Acrobatics 5 ranks, Ride 11 ranks, leaping lance class feature" },
    { text = "Remount your steed as a swift action with successful Acrobatics check" },
  ],
  [
    { text = "Rebuffing Reduction\\*" },
    { text = "[Damage reduction](ref/rule/damage-reduction), Improved Bull Rush" },
    { text = "Bull Rush opponent who fails to pierce your DR" },
  ],
  [
    { text = "Rending Fury\\*" },
    { text = "Rend special attack, base attack bonus +6" },
    { text = "Need half the normal number of attacks to deal rend damage" },
  ],
  [
    { text = "Improved Rending Fury\\*" },
    { text = "Rending Fury, base attack bonus +9" },
    { text = "Deal extra damage on a successful rend" },
  ],
  [
    { text = "Greater Rending Fury\\*" },
    { text = "Improved Rending Fury, base attack bonus +12" },
    { text = "When you rend an opponent, you deal bleed damage" },
  ],
  [
    { text = "Revelation Strike\\*" },
    { text = "Improve Unarmed Strike, revelation class feature" },
    { text = "Affect an opponent with revelation as part of a melee attack" },
  ],
  [
    { text = "Rhetorical Flourish" },
    { text = "Cha 13, Persuasive" },
    { text = "Use verbal misdirection while making Diplomacy check" },
  ],
  [
    { text = "Righteous Healing" },
    { text = "Judgment class feature" },
    { text = "Heal more when you have a judgment active" },
  ],
  [
    { text = "Sap Adept\\*" },
    { text = "Sneak attack +1d6" },
    { text = "Gain bonus damage on nonlethal attacks" },
  ],
  [
    { text = "Sap Master\\*" },
    { text = "Sap Adept, sneak attack +3d6" },
    { text = "Deal twice your sneak attack damage when dealing nonlethal damage" },
  ],
  [
    { text = "School Strike\\*" },
    { text = "Improved Unarmed Strike, wizard school class feature" },
    { text = "May deliver magic school effect as swift action after melee attack" },
  ],
  [
    { text = "Sea Legs" },
    { text = "Profession (sailor) 5 ranks" },
    { text = "Gain +2 on Acrobatics, Climb, and Swim checks" },
  ],
  [
    { text = "Shapeshifter Foil" },
    { text = "Knowledge (arcana) 5 ranks or Knowledge (nature) 5 ranks, ability to use polymorph effects" },
    { text = "When you deal damage, target's ability to use any polymorph effects is hindered" },
  ],
  [
    { text = "Shapeshifting Hunter" },
    { text = "Favored enemy class feature, wild shape class feature" },
    { text = "Add your druid and ranger levels for favored enemy" },
  ],
  [
    { text = "Shared Judgment" },
    { text = "Second judgment class feature" },
    { text = "Extend a judgment to an adjacent ally instead of enacting a second judgment" },
  ],
  [
    { text = "Siege Commander\\*" },
    { text = "Craft (siege weapon) 5 ranks, Knowledge (engineering) 5 ranks or Profession (Siege Engineer) 1 rank" },
    { text = "Grant weapon crew +4 on assemble or move checks" },
  ],
  [
    { text = "Siege Engineer\\*" },
    { text = "Knowledge (engineering) 5 ranks or Profession (siege engineer) 5 ranks, proficiency with 1 siege weapon" },
    { text = "You are considered proficient with all siege weapons" },
  ],
  [
    { text = "Master Siege Engineer\\*" },
    { text = "Siege Weapon Engineer, Knowledge (engineering) 10 ranks" },
    { text = "Crew can load siege engine as a move action" },
  ],
  [
    { text = "Siege Gunner\\*" },
    { text = "Siege Weapon Engineer" },
    { text = "Take no size penalties for aiming a direct fire siege weapon" },
  ],
  [
    { text = "Skilled Driver" },
    { text = "—" },
    { text = "Gain +4 bonus on driving checks with made with one vehicle" },
  ],
  [
    { text = "Expert Driver" },
    { text = "Skilled Driver" },
    { text = "Maneuver a vehicle of a selected type as a move action, and you can stop immediately" },
  ],
  [
    { text = "Slayer's Knack" },
    { text = "Favored enemy class feature, base attack bonus +6" },
    { text = "Double the threat range of all weapons against one favored enemy" },
  ],
  [
    { text = "Sling Flail" },
    { text = "Weapon Focus (sling), base attack bonus +1" },
    { text = "Make melee attacks with a sling" },
  ],
  [
    { text = "Snap Shot\\*" },
    { text = "Rapid Shot, Weapon Focus, base attack bonus +6" },
    { text = "Threaten squares within 5 feet of you when wielding a ranged weapon" },
  ],
  [
    { text = "Improved Snap Shot\\*" },
    { text = "Dex 15, Snap Shot, base attack bonus +9" },
    { text = "You threaten an additional 10 feet with Snap Shot" },
  ],
  [
    { text = "Greater Snap Shot\\*" },
    { text = "Dex 17, Improved Snap Shot, base attack bonus +12" },
    { text = "Gain bonus on damage and critical confirmation when using ranged weapons" },
  ],
  [
    { text = "Sneaking Precision" },
    { text = "Sneak attack class feature, Critical Focus, any critical feat, base attack bonus +9" },
    { text = "On the second sneak attack in a round, you may apply a critical feat" },
  ],
  [
    { text = "Sorcerous Strike" },
    { text = "Sorcerer bloodline class feature, Improved Unarmed Strike" },
    { text = "Apply a bloodline ability as part of a melee attack" },
  ],
  [
    { text = "Spell Bane" },
    { text = "Bane class feature" },
    { text = "Your spells' DCs increase by 2 when bane is in effect" },
  ],
  [
    { text = "Spinning Throw\\*" },
    { text = "Improved Bull Rush, Improved Trip, Improved Unarmed Strike, _Ki_ Throw" },
    { text = "Spend a swift action to bull rush opponent, move it, then knock it prone" },
  ],
  [
    { text = "Splintering Weapon" },
    { text = "Weapon Proficiency, base attack bonus +1" },
    { text = "Break a weapon to deal bleed damage" },
  ],
  [
    { text = "Stage Combatant\\*" },
    { text = "Weapon Focus, base attack bonus +5" },
    { text = "Take no penalty to deal nonlethal damage" },
  ],
  [
    { text = "Stalwart" },
    { text = "Diehard, base attack bonus +4" },
    { text = "Forgo dodge AC bonus for equivalent DR" },
  ],
  [
    { text = "Improved Stalwart" },
    { text = "Stalwart, base attack bonus +11" },
    { text = "Double DR gained from Stalwart" },
  ],
  [
    { text = "Strangler\\*" },
    { text = "Improved Grapple, sneak attack +1d6" },
    { text = "Deal sneak damage to grappled opponent" },
  ],
  [
    { text = "Strong Comeback" },
    { text = "—" },
    { text = "Add a +2 bonus on all rerolls" },
  ],
  [
    { text = "Stunning Pin\\*" },
    { text = "Improved Grapple, Stunning Fist" },
    { text = "Use Stunning Fist against pinned opponents" },
  ],
  [
    { text = "Sure Grasp" },
    { text = "Climb 1 rank" },
    { text = "When climbing, roll twice and take the highest result" },
  ],
  [
    { text = "Sword And Pistol\\*" },
    { text = "Snap Shot, Two-Weapon Fighting, base attack bonus +6" },
    { text = "Ranged attacks do not provoke attacks of opportunity" },
  ],
  [
    { text = "Trapper's Setup" },
    { text = "Craft (traps) 5 ranks" },
    { text = "Manually trigger traps to gain +2 on attack rolls and to DC" },
  ],
  [
    { text = "Twin Thunders\\*" },
    { text = "Flurry of blows class feature or Two-Weapon Fighting, Weapon Focus with wielded bludgeoning weapons, defensive training race trait, dwarf or gnome" },
    { text = "Substitute disarm, sunder, and trip for any of your attacks vs. giants" },
  ],
  [
    { text = "Twin Thunders Flurry\\*" },
    { text = "Twin Thunders, base attack bonus +6" },
    { text = "Trip a giant of up to Huge size, and deal +2 damage against giants" },
  ],
  [
    { text = "Twin Thunders Master\\*" },
    { text = "Twin Thunders Flurry, base attack bonus +9" },
    { text = "Opponent struck by Twin Thunders is shaken" },
  ],
  [
    { text = "Two-Handed Thrower\\*" },
    { text = "Str 15" },
    { text = "Gain Str bonus when using two hands to throw a one or two-handed weapon" },
  ],
  [
    { text = "Two-Weapon Feint\\*" },
    { text = "Combat Expertise, Two-Weapon Fighting" },
    { text = "Forgo first melee attack to feint" },
  ],
  [
    { text = "Vicious Stomp\\*" },
    { text = "Combat Reflexes, Improved Unarmed Strike" },
    { text = "When opponent falls prone, it provokes an attack of opportunity from you" },
  ],
  [
    { text = "Wave Strike\\*" },
    { text = "Weapon expertise class feature or Quick Draw, Bluff 1 rank" },
    { text = "Spend a swift action to make a Bluff check to feint" },
  ],
  [
    { text = "Whip Mastery\\*" },
    { text = "Weapon Focus (whip), base attack bonus +2" },
    { text = "Using a whip does not provoke attacks of opportunity" },
  ],
  [
    { text = "Improved Whip Mastery\\*" },
    { text = "Whip Mastery, base attack bonus +5" },
    { text = "Threaten with your whip and grasp Tiny objects" },
  ],
  [
    { text = "Greater Whip Mastery\\*" },
    { text = "Improved Whip Mastery, base attack bonus +8" },
    { text = "Grapple using a whip" },
  ],
  [
    { text = "Grit Feat", header = true },
    { text = "Prerequisites", header = true },
    { text = "Benefit", header = true },
  ],
  [
    { text = "Deft Shootist" },
    { text = "Grit class feature or Amateur Gunslinger,Mobility" },
    { text = "Do not provoke attacks of opportunity while shooting or reloading firearms as long as you have 1 grit point" },
  ],
  [
    { text = "Extra Grit" },
    { text = "Grit class feature or Amateur Gunslinger" },
    { text = "Gain 2 extra grit points per day, and maximum gritincreases by 2" },
  ],
  [
    { text = "Leaping Shot" },
    { text = "Grit class feature or Amateur Gunslinger, Mobility, base attack bonus +4" },
    { text = "May move your speed and make firearm attacks" },
  ],
  [
    { text = "No Name" },
    { text = "Grit class feature or Amateur Gunslinger,Bluff 4 ranks" },
    { text = "Gain +2 on Bluff checks, and spend grit to gain +10 on Disguise checks" },
  ],
  [
    { text = "Ricochet Shot Deed" },
    { text = "Grit class feature or Amateur Gunslinger,Blind-Fight" },
    { text = "Ricochet your shots off of a wall or other solid terrain" },
  ],
  [
    { text = "Secret Stash Deed" },
    { text = "Grit class feature or Amateur Gunslinger, Sleight of Hand 1 rank" },
    { text = "Spend 1 grit point to recover powder or ammunitionfrom your person" },
  ],
  [
    { text = "Signature Deed" },
    { text = "Grit class feature, gunslinger level 11th" },
    { text = "Use 1 deed for 1 fewer grit point" },
  ],
  [
    { text = "Performance Feat", header = true },
    { text = "Prerequisites", header = true },
    { text = "Benefit", header = true },
  ],
  [
    { text = "Dramatic Display\\*" },
    { text = "Dazzling Display" },
    { text = "Gain +2 on Performance checks, attack rolls, and combat maneuver checks" },
  ],
  [
    { text = "Hero's Display\\*" },
    { text = "Dazzling Display" },
    { text = "Gain +2 on performance combat checks; may demoralize opponents" },
  ],
  [
    { text = "Masterful Display\\*" },
    { text = "Dazzling Display, any two performance feats" },
    { text = "Gain benefits of two performance feats" },
  ],
  [
    { text = "Mocking Dance\\*" },
    { text = "Acrobatics 4 ranks or Perform (dance) 4 ranks" },
    { text = "May either move 5 feet without provoking attacks of opportunity, or your speed with them" },
  ],
  [
    { text = "Murderer's Circle\\*" },
    { text = "Dodge, Acrobatics 4 ranks" },
    { text = "When you make a performance combat check after a critical, move 5 feet" },
  ],
  [
    { text = "Savage Display\\*" },
    { text = "Dazzling Display" },
    { text = "Gain +2 on Performance checks and +1d6 ondamage rolls" },
  ],
  [
    { text = "Style Feat", header = true },
    { text = "Prerequisites", header = true },
    { text = "Benefit", header = true },
  ],
  [
    { text = "Boar Style\\*" },
    { text = "Improved Unarmed Strike, Intimidate 3 ranks" },
    { text = "Unarmed strikes deal bludgeoning or piercing damage" },
  ],
  [
    { text = "Boar Ferocity\\*" },
    { text = "Boar Style, Intimidate 6 ranks," },
    { text = "Add piercing damage to unarmed attacks, and demoralize opponents" },
  ],
  [
    { text = "Boar Shred\\*" },
    { text = "Boar Ferocity, Intimidate 9 ranks" },
    { text = "Unarmed attacks cause bleed damage" },
  ],
  [
    { text = "Crane Style\\*" },
    { text = "Dodge, Improved Unarmed Strike, base attack bonus +2 or monk level 1" },
    { text = "Take –2 penalty when fighting defensively" },
  ],
  [
    { text = "Crane Wing\\*" },
    { text = "Crane Style, base attack bonus +5 or monk level 5" },
    { text = "May deflect one attack per round while fighting defensively or using total defense" },
  ],
  [
    { text = "Crane Riposte\\*" },
    { text = "Crane Wing, base attack bonus +8 or monk level 7" },
    { text = "When you deflect an attack, you may make an attack of opportunity" },
  ],
  [
    { text = "Djinni Style\\*" },
    { text = "Con 13, Wis 15, Elemental Fist, baseattack bonus +9 or monk level 5th" },
    { text = "Gain 1 additional use of Elemental Fist per day and bonus to electricity damage" },
  ],
  [
    { text = "Djinni Spirit\\*" },
    { text = "Con 15, Djinni Style, base attack bonus +11 or monk level 9th" },
    { text = "Gain 1 additional use of Elemental Fistper day, and electricity resistance" },
  ],
  [
    { text = "Djinni Spin\\*" },
    { text = "Wis 17, Djinni Spirit, base attack bonus +13 or monk level 11th" },
    { text = "Use Elemental Fist to surround yourself with electricity" },
  ],
  [
    { text = "Dragon Style\\*" },
    { text = "Str 15, Improved Unarmed Strike, Acrobatics 3 ranks" },
    { text = "Gain +2 bonus against sleep, paralysis, and stun effects, and can ignore difficult terrain" },
  ],
  [
    { text = "Dragon Ferocity\\*" },
    { text = "Dragon Style, Stunning Fist, Acrobatics 5 ranks" },
    { text = "Gain bonus on unarmed attacks, and you can cause opponents to be shaken" },
  ],
  [
    { text = "Dragon Roar\\*" },
    { text = "Dragon Style, Acrobatics 8 ranks" },
    { text = "Gain +1 use of Stunning Fist per day, and you can emit a concussive roar" },
  ],
  [
    { text = "Earth Child Style\\*" },
    { text = "Wis 13, Improved Unarmed Strike, Acrobatics 3 ranks, defensive training racial trait, dwarf or gnome" },
    { text = "Defensive training AC increases to +6 against giants" },
  ],
  [
    { text = "Earth Child Topple\\*" },
    { text = "Earth Child Style, Improved Trip, Acrobatics 6 ranks" },
    { text = "You may trip a giant of up to Huge size" },
  ],
  [
    { text = "Earth Child Binder\\*" },
    { text = "Earth Child Topple, Greater Trip, Stunning Fist, Acrobatics 9 ranks" },
    { text = "You can trip a giant of any size. You use Stunning Fist after the attack of opportunity against a standing giant has hit" },
  ],
  [
    { text = "Efreeti Style\\*" },
    { text = "Con 13, Wis 15, Elemental Fist, Improved Unarmed Strike, base attack bonus +9 or monk level 5th" },
    { text = "Gain +1 use of Elemental Fist per day and a bonus on fire damage" },
  ],
  [
    { text = "Efreeti Stance\\*" },
    { text = "Con 15, Efreeti Style, base attack bonus +11 or monk level 9th" },
    { text = "Gain +1 use of Elemental Fist per day and fire resistance" },
  ],
  [
    { text = "Efreeti Touch\\*" },
    { text = "Wis 17, Efreeti Stance, base attack bonus +13 or monk level 11th" },
    { text = "Can emit a cone of fire that may light opponents on fire" },
  ],
  [
    { text = "Janni Style\\*" },
    { text = "Acrobatics 3 ranks, Perform (dance) 3 ranks, Improved Unarmed Strike" },
    { text = "Take only a –1 AC penalty when charging, flanking opponents only gain +1 attack bonus against you" },
  ],
  [
    { text = "Janni Tempest\\*" },
    { text = "Janni Style, Acrobatics 5 ranks, Perform (dance) 5 ranks" },
    { text = "After successful unarmed attack, gain +4 on combat maneuver checks to bull rush or trip" },
  ],
  [
    { text = "Janni Rush\\*" },
    { text = "Janni Tempest, Acrobatics 8 ranks, Perform (dance) 8 ranks" },
    { text = "Always count as having a running start for jumping, and deal double damage on a jumping charge" },
  ],
  [
    { text = "Kirin Style" },
    { text = "Improved Unarmed Strike, Knowledge (arcana) 6 ranks, Knowledge (dungeoneering, local, nature, planes, or religion) 1 rank" },
    { text = "May make Knowledge check against opponent as swift action to gain bonuses" },
  ],
  [
    { text = "Kirin Strike" },
    { text = "Int 13, Kirin Style, Knowledge (arcana) 9 ranks, Knowledge (dungeoneering, local, nature, planes, or religion) 3 ranks" },
    { text = "Gain +2 insight bonus to identify a creature" },
  ],
  [
    { text = "Kirin Path" },
    { text = "Kirin Strike, Knowledge (arcana) 12 ranks, Knowledge (dungeoneering, local, nature, planes, or religion) 5 ranks" },
    { text = "You may take 10 to identify a creature using Knowledge (local, nature, planes, or religion)" },
  ],
  [
    { text = "Mantis Style\\*" },
    { text = "Stunning Fist, Heal 3 ranks" },
    { text = "Gain +1 use of Stunning Fist per day, and increase stunning fist DC by +2" },
  ],
  [
    { text = "Mantis Wisdom\\*" },
    { text = "Mantis Style, Heal 6 ranks" },
    { text = "Treat half your non-monk levels as monk levels for Stunning Fist effects" },
  ],
  [
    { text = "Mantis Torment\\*" },
    { text = "Mantis Wisdom, Heal 9 ranks" },
    { text = "Gain +1 use of Stunning Fist per day, and may dazzle and stagger, then fatigue an opponent" },
  ],
  [
    { text = "Marid Style\\*" },
    { text = "Con 13, Wis 15, Elemental Fist, Improved Unarmed Strike, base attack bonus +9 or Monk level 5th" },
    { text = "Gain +1 use of Elemental Fist per day, and deal cold damage" },
  ],
  [
    { text = "Marid Spirit\\*" },
    { text = "Con 15, Marid Style, base attack bonus +11 or monk level 9th" },
    { text = "Gain +1 use of Elemental Fist per day, and cold resistance" },
  ],
  [
    { text = "Marid Coldsnap\\*" },
    { text = "Wis 17, Marid Spirit, base attack bonus +13 or monk level 11th" },
    { text = "Unleash a 30-foot line of frigid water" },
  ],
  [
    { text = "Monkey Style\\*" },
    { text = "Wis 13, Acrobatics 5 ranks, Climb 5 ranks, Improved Unarmed Strike" },
    { text = "Add Wisdom bonus on Acrobatics checks, and take no penalty for attacking while prone" },
  ],
  [
    { text = "Monkey Moves\\*" },
    { text = "Monkey Style, Acrobatics 8 ranks, Climb 8 ranks" },
    { text = "Add Wisdom bonus on Climb checks, and climb and crawl at half speed" },
  ],
  [
    { text = "Monkey Shine\\*" },
    { text = "Monkey Moves, Stunning Fist, Acrobatics 11 ranks, Climb 11 ranks" },
    { text = "After successful Stunning Fist, you may enter an adjacent square" },
  ],
  [
    { text = "Panther Style\\*" },
    { text = "Wis 13, Combat Reflexes, Improved Unarmed Strike" },
    { text = "Retaliate against opponents that take attacks of opportunity against you" },
  ],
  [
    { text = "Panther Claw\\*" },
    { text = "Wis 15, Panther Style" },
    { text = "Retaliate as a free action instead of as a swift action" },
  ],
  [
    { text = "Panther Parry\\*" },
    { text = "Panther Claw" },
    { text = "Retaliatory attacks are resolved before the attack" },
  ],
  [
    { text = "Shaitan Style\\*" },
    { text = "Con 13, Wis 15, Elemental Fist, base attack bonus +9 or monk level 5th" },
    { text = "Gain +1 use of Elemental Fist per day, and deal acid damage" },
  ],
  [
    { text = "Shaitan Skin\\*" },
    { text = "Con 15, Shaitan Style, base attack bonus +11 or monk level 9th" },
    { text = "Gain +1 use of Elemental Fist per day, and acid resistance" },
  ],
  [
    { text = "Shaitan Earthblast\\*" },
    { text = "Wis 17, Shaitan Skin, base attack bonus +13 or monk level 11th" },
    { text = "Unleash a 20-foot column of acid" },
  ],
  [
    { text = "Snake Style" },
    { text = "Improved Unarmed Strike, Acrobatics 1 rank, Sense Motive 3 ranks" },
    { text = "Gain +2 on Sense Motive checks, and deal piercing damage with unarmed attacks" },
  ],
  [
    { text = "Snake Sidewind" },
    { text = "Snake Style, Acrobatics 3 ranks, Sense Motive 6 ranks" },
    { text = "Gain a bonus to avoid being knocked prone, and use Sense Motive check to confirm critical hits" },
  ],
  [
    { text = "Snake Fang" },
    { text = "Combat Reflexes, Snake Sidewind, Snake Style, Acrobatics 6 ranks, Sense Motive 9 ranks" },
    { text = "If opponent misses you, make an attack of opportunity as an immediate action" },
  ],
  [
    { text = "Snapping Turtle Style\\*" },
    { text = "Improved Unarmed Strike, base attack bonus +1 or monk level 1st" },
    { text = "Gain +1 shield bonus to AC when at least one hand is free" },
  ],
  [
    { text = "Snapping Turtle Clutch\\*" },
    { text = "Improved Grapple, Snapping Turtle Style, base attack bonus +3 or monk level 3rd" },
    { text = "Your shield bonus applies to your CMD and touch AC" },
  ],
  [
    { text = "Snapping Turtle Shell\\*" },
    { text = "Snapping Turtle Clutch, base attack bonus +5 or monk level 5th" },
    { text = "AC bonus increases by 2, and opponents receive –4 on critical confirmations" },
  ],
  [
    { text = "Tiger Style\\*" },
    { text = "Improved Unarmed Strike, base attack bonus +3 or monk level 3rd" },
    { text = "Gain +2 to CMD against bull rush, overrun, and trip, and deal slashing damage" },
  ],
  [
    { text = "Tiger Claws\\*" },
    { text = "Tiger Style, base attack bonus +6 or monk level 5th" },
    { text = "Make a single attack with both hands, and combine the results" },
  ],
  [
    { text = "Tiger Pounce\\*" },
    { text = "Power Attack, Tiger Claws, base attack bonus +9 or monk level 8th" },
    { text = "May apply the penalty from Power Attack to AC" },
  ],
  [
    { text = "Teamwork Feat", header = true },
    { text = "Prerequisites", header = true },
    { text = "Benefit", header = true },
  ],
  [
    { text = "Back to Back" },
    { text = "Perception 3 ranks" },
    { text = "Gain a +2 to AC against flanking opponents" },
  ],
  [
    { text = "Improved Back to Back" },
    { text = "Back to Back, Perception 5 ranks" },
    { text = "Grant adjacent ally +2 to AC against flanking opponents" },
  ],
  [
    { text = "Broken Wing Gambit\\*" },
    { text = "Bluff 5 ranks" },
    { text = "Grant opponent bonus to hit you, but opponent's attack provokes attacks of opportunity" },
  ],
  [
    { text = "Cavalry Formation\\*" },
    { text = "Mounted Combat" },
    { text = "May share space with other mounts, charge through space occupied by allied mount" },
  ],
  [
    { text = "Combat Medic" },
    { text = "Heal 5 ranks" },
    { text = "May take 10 and not provoke attacks of opportunity when using Heal" },
  ],
  [
    { text = "Coordinated Charge\\*" },
    { text = "At least two other teamwork feats, base attack bonus +10" },
    { text = "You may charge the same foe when an ally does" },
  ],
  [
    { text = "Enfilading Fire" },
    { text = "Point-Blank Shot, Precise Shot, 1 other teamwork feat" },
    { text = "When ally flanks opponent, you gain +2 on ranged attack rolls against opponent" },
  ],
  [
    { text = "Escape Route" },
    { text = "—" },
    { text = "You do not provoke attacks of opportunity when moving through spaces adjacent to allies" },
  ],
  [
    { text = "Feint Partner\\*" },
    { text = "Bluff 1 rank" },
    { text = "When ally successfully feints, opponent loses Dex bonus against your next attack" },
  ],
  [
    { text = "Improved Feint Partner\\*" },
    { text = "Combat Reflexes, Feint Partner, base attack bonus +6" },
    { text = "When ally successfully feints, you gain attack of opportunity against opponent" },
  ],
  [
    { text = "Pack Attack" },
    { text = "base attack bonus +1" },
    { text = "Ally's attack allows you to take a 5-foot step" },
  ],
  [
    { text = "Seize the Moment" },
    { text = "Combat Reflexes, Improved Critical" },
    { text = "When ally confirms a critical threat, you gain an attack of opportunity" },
  ],
  [
    { text = "Shake It Off" },
    { text = "—" },
    { text = "Gain +1 to all saving throws per adjacent ally" },
  ],
  [
    { text = "Stealth Synergy" },
    { text = "—" },
    { text = "Take the highest roll made by you and your allies on Stealth checks" },
  ],
  [
    { text = "Tandem Trip" },
    { text = "—" },
    { text = "When you make a trip against an opponent threatened by any ally, roll twice and take the higher result" },
  ],
  [
    { text = "Target of Opportunity" },
    { text = "Point-Blank Shot, base attack bonus +6" },
    { text = "When an ally hits with a ranged attack, youmay make an attack as an immediate action" },
  ],
  [
    { text = "Team Pickpocketing" },
    { text = "Bluff 1 rank, Sleight of Hand 1 rank" },
    { text = "When ally makes a Bluff check, you can pick opponent's pocket as an immediate action" },
  ],
]
:::
