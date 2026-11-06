+++
id = "ref/carried/ultimate-equipment/rules/gear/poisons"
kind = "rule"
title = "Poisons"
source_ids = ["ultimate-equipment"]
section = ["Rules", "Gear"]
parent = "ref/carried/ultimate-equipment/rules/gear"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Equipment/Rules/Gear/Poisons", path = "ultimate_equipment/rules/gear.json" },
]

[fields]
kind = "none"
+++

A poison is a substance that interferes with the natural functions of a living creature's body,
causing injury or death, typically requiring only a very small amount. The target of a poison may
resist with a successful saving throw. Poisons can be delayed or cured with spells such as delay
poison and neutralize poison. Poisons have four categories, based on how they reach the target:
contact, ingested, inhaled, or injury.

## Contact {#contact}

These poisons are delivered the moment a creature touches the poison with its bare skin. Such
poisons can be used as injury poisons. Contact poisons usually have an onset time of 1 minute and a
frequency of 1 minute.

## Ingested {#ingested}

These poisons are delivered when a creature eats or drinks the poison. Ingested poisons usually have
an onset time of 10 minutes and a frequency of 1 minute.

## Inhaled {#inhaled}

These poisons are delivered the moment a creature enters an area containing such poisons and do not
usually have an onset time. For most inhaled poisons, 1 dose fills a volume equal to a 10-foot cube.
A creature can attempt to hold its breath while inside the area to avoid inhaling the toxin. A
creature holding its breath receives a 50% chance of not having to make a Fortitude save each round.
See the rules for holding your breath and suffocation. If a creature is holding its breath and fails
the constitution check to continue doing so, rather than suffocating it begins to breathe normally
again (and is subject to the effects of the inhaled poison if still in the area).

## Injury {#injury}

These poisons are primarily delivered through the attacks of certain creatures and through weapons
coated in the toxin. Injury poisons do not usually have an onset time and have a frequency of 1
round.

## Applying Poison {#applying-poison}

One dose of poison smeared on a weapon or some other object affects just a single target. A poisoned
weapon or object retains its poison until the weapon scores a hit or the object is touched (unless
the poison is wiped off before a target comes in contact with it).

Applying poison to a weapon or single piece of ammunition is a standard action. Whenever you apply
or ready a poison for use, there is a 5% chance that you expose yourself to the poison and must save
against the poison as normal. This does not consume the dose of poison. Whenever you attack with a
poisoned weapon, if the attack roll results in a natural 1, you expose yourself to the poison. This
consumes the poison on the weapon. If you have the poison use class feature (such as from the
assassin prestige class or the alchemist base class), you do not risk accidentally poisoning
yourself when applying poison.

## Multiple Doses of Poison {#multiple-doses-of-poison}

Unlike other afflictions, multiple doses of the same poison “stack,” meaning that successive doses
combine to increase the poison's DC and duration.

Making your initial saving throw against a poison means stacking does not occur—the poison did not
affect you and any later doses are treated independently. Likewise, if a poison has been cured or
run its course (by you either making the saves or outlasting the poison's duration), stacking does
not occur. However, if there is still poison active in you when you are attacked with that type of
poison again, and you fail your initial save against the new dose, the doses stack. This has two
effects, which last until the poisons run their course.

### Increased Duration {#increased-duration}

Increase the duration of the poison by 1/2 the amount listed in its frequency entry.

### Increased DC {#increased-dc}

Increase the poison's duration by +2.

These increases are cumulative (a third dose adds another 1/2 of the frequency to the duration and
+2 to the DC, and so on). When affected by multiple doses of the same poison, you only make one
saving throw at this higher DC when required by the frequency, rather than one saving throw against
each dose of the poison.

Multiple doses do not alter the Cure condition of the Poison, and meeting that Cure condition ends
all doses of the poison.

Applied contact poisons and injury poisons cannot inflict more than one dose of poison per weapon at
a time (because the poison on the weapon only lasts for one successful attack before it wears off).
Inhaled and ingested poisons can inflict multiple doses at once.

Doses from different poisons (such as an assassin with greenblood oil on his dagger and Medium
spider venom on his short sword) do not stack—the effects of each are tracked separately.

### Example 1 {#example-1}

A fighter is facing three Medium spiders (which inject Medium spider venom on a successful bite).
Medium spider venom normally has a frequency of 4 rounds and a DC of 14. On the first round, all
three spiders bite him and he fails all three saves. The second and third doses each increase the
total duration by 2 rounds (half of the 4 round frequency) and the save DC by +2, for a total
duration of 8 rounds (4 + 2 + 2) and DC 18 (14 + 2 + 2). Fortunately, Medium spider venom is cured
after just one successful save, even though the fighter is battling three doses at once.

### Example 2 {#example-2}

This time, the fighter makes two of his initial saves against the spider venom, so he only has one
dose active in his body. He fails his save on his turn. On the spiders's turn, two of them bite him,
and he fails both saves, which increases the duration to 8 rounds and the DC to 18, just as if he
had failed all three saves in the same round.

## Crafting Poison {#crafting-poison}

You can make poison with the Craft (alchemy) skill. The DC to make a poison is equal to its
Fortitude save DC. Rolling a natural 1 on a Craft skill check while making a poison exposes you to
the poison. This does not consume the poison. If you have the poison use class feature, you do not
risk accidentally poisoning yourself when applying poison.

The sample poisons on the next page represent just some of the common poisons available in cities.
Of course, most cities have laws against buying, selling, or crafting poison.

### Poisons {#poisons}

::: table
caption = "Poisons"
head = [
  [
    { text = "Poison", header = true },
    { text = "Type", header = true },
    { text = "Fort DC", header = true },
    { text = "Onset", header = true },
    { text = "Frequency", header = true },
    { text = "Effect", header = true },
    { text = "Cure", header = true },
    { text = "Price", header = true },
  ],
]
body = [
  [
    { text = "Black lotus extract" },
    { text = "Contact" },
    { text = "20" },
    { text = "1 min." },
    { text = "1/rd. for 6 rds." },
    { text = "1d6 Con" },
    { text = "2 saves" },
    { text = "4,500 gp" },
  ],
  [
    { text = "Dragon bile" },
    { text = "Contact" },
    { text = "26" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Str" },
    { text = "—" },
    { text = "1,500 gp" },
  ],
  [
    { text = "Malyass root paste" },
    { text = "Contact" },
    { text = "16" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d2 Dex" },
    { text = "1 save" },
    { text = "250 gp" },
  ],
  [
    { text = "Nitharit" },
    { text = "Contact" },
    { text = "13" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Con" },
    { text = "1 save" },
    { text = "650 gp" },
  ],
  [
    { text = "Sassone leaf residue" },
    { text = "Contact" },
    { text = "16" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "2d12 hp/1 Con" },
    { text = "1 save" },
    { text = "300 gp" },
  ],
  [
    { text = "Tears of death" },
    { text = "Contact" },
    { text = "22" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d6 Con and paralyzed 1 min." },
    { text = "—" },
    { text = "6,500 gp" },
  ],
  [
    { text = "Terinav root" },
    { text = "Contact" },
    { text = "16" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Dex" },
    { text = "1 save" },
    { text = "400 gp" },
  ],
  [
    { text = "Arsenic" },
    { text = "Ingested" },
    { text = "13" },
    { text = "10 min." },
    { text = "1/min. for 4 min." },
    { text = "1d2 Con" },
    { text = "1 save" },
    { text = "120 gp" },
  ],
  [
    { text = "Belladonna" },
    { text = "Ingested" },
    { text = "14" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d2 Str, see text" },
    { text = "1 save" },
    { text = "100 gp" },
  ],
  [
    { text = "Dark reaver powder" },
    { text = "Ingested" },
    { text = "18" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Con and 1 Str" },
    { text = "2 saves" },
    { text = "800 gp" },
  ],
  [
    { text = "Hemlock" },
    { text = "Ingested" },
    { text = "18" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d6 Dex, see text" },
    { text = "2 saves" },
    { text = "2,500 gp" },
  ],
  [
    { text = "Id moss" },
    { text = "Ingested" },
    { text = "14" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Int" },
    { text = "1 save" },
    { text = "125 gp" },
  ],
  [
    { text = "Indigo dreams" },
    { text = "Ingested" },
    { text = "13" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Wis" },
    { text = "2 saves" },
    { text = "150 gp" },
  ],
  [
    { text = "King's sleep" },
    { text = "Ingested" },
    { text = "19" },
    { text = "1 day" },
    { text = "1/day" },
    { text = "1 Con drain" },
    { text = "2 saves" },
    { text = "5,000 gp" },
  ],
  [
    { text = "Lich dust" },
    { text = "Ingested" },
    { text = "17" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Str" },
    { text = "2 saves" },
    { text = "400 gp" },
  ],
  [
    { text = "Oil of taggit" },
    { text = "Ingested" },
    { text = "15" },
    { text = "1 min." },
    { text = "—" },
    { text = "Unconscious 1d3 hrs." },
    { text = "1 save" },
    { text = "90 gp" },
  ],
  [
    { text = "Striped toadstool" },
    { text = "Ingested" },
    { text = "11" },
    { text = "10 min." },
    { text = "1/min. for 4 min." },
    { text = "1d3 Wis and 1 Int" },
    { text = "1 save" },
    { text = "180 gp" },
  ],
  [
    { text = "Swampseer poison" },
    { text = "Ingested" },
    { text = "18" },
    { text = "10 min." },
    { text = "1/min. for 3 min." },
    { text = "1d4 Wis/1d2 Wis and confusion 1 min." },
    { text = "2 saves" },
    { text = "400 gp" },
  ],
  [
    { text = "Wolfsbane" },
    { text = "Ingested" },
    { text = "16" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Con" },
    { text = "1 save" },
    { text = "500 gp" },
  ],
  [
    { text = "Azure lily pollen" },
    { text = "Inhaled" },
    { text = "15" },
    { text = "—" },
    { text = "1/min. for 2 min." },
    { text = "nauseated 1 min./paralyzed 2d4 hrs." },
    { text = "1 save" },
    { text = "1,500 gp" },
  ],
  [
    { text = "Burnt othur fumes" },
    { text = "Inhaled" },
    { text = "18" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1 Con drain/1d3 Con" },
    { text = "2 saves" },
    { text = "2,100 gp" },
  ],
  [
    { text = "Insanity mist" },
    { text = "Inhaled" },
    { text = "15" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Wis" },
    { text = "1 save" },
    { text = "1,500 gp" },
  ],
  [
    { text = "Nightmare vapor" },
    { text = "Inhaled" },
    { text = "20" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1 Wis and confused 1 rd." },
    { text = "2 saves" },
    { text = "1,800 gp" },
  ],
  [
    { text = "Ungol dust" },
    { text = "Inhaled" },
    { text = "15" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1 Cha drain/1d2 Cha" },
    { text = "1 save" },
    { text = "1,000 gp" },
  ],
  [
    { text = "Black adder venom" },
    { text = "Injury" },
    { text = "11" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d2 Con" },
    { text = "1 save" },
    { text = "120 gp" },
  ],
  [
    { text = "Bloodroot" },
    { text = "Injury" },
    { text = "12" },
    { text = "1 rd." },
    { text = "1/rd. for 4 rds." },
    { text = "1 Con and 1 Wis and confusion 1 rd." },
    { text = "1 save" },
    { text = "100 gp" },
  ],
  [
    { text = "Blue whinnis" },
    { text = "Injury" },
    { text = "14" },
    { text = "—" },
    { text = "1/rd. for 2 rds." },
    { text = "1 Con/unconscious 1d3 hrs." },
    { text = "1 save" },
    { text = "120 gp" },
  ],
  [
    { text = "Deathblade" },
    { text = "Injury" },
    { text = "20" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Con" },
    { text = "2 saves" },
    { text = "1,800 gp" },
  ],
  [
    { text = "Drow poison" },
    { text = "Injury" },
    { text = "13" },
    { text = "—" },
    { text = "1/min. for 2 min." },
    { text = "Unconscious 1 min./2d4 hrs." },
    { text = "1 save" },
    { text = "75 gp" },
  ],
  [
    { text = "Giant wasp poison" },
    { text = "Injury" },
    { text = "18" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d2 Dex" },
    { text = "1 save" },
    { text = "210 gp" },
  ],
  [
    { text = "Greenblood oil" },
    { text = "Injury" },
    { text = "13" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1 Con" },
    { text = "1 save" },
    { text = "100 gp" },
  ],
  [
    { text = "Large scorpion venom" },
    { text = "Injury" },
    { text = "17" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d2 Str" },
    { text = "1 save" },
    { text = "200 gp" },
  ],
  [
    { text = "Medium spider venom" },
    { text = "Injury" },
    { text = "14" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1d2 Str" },
    { text = "1 save" },
    { text = "150 gp" },
  ],
  [
    { text = "Purple worm poison" },
    { text = "Injury" },
    { text = "24" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Str" },
    { text = "2 saves" },
    { text = "700 gp" },
  ],
  [
    { text = "Shadow essence" },
    { text = "Injury" },
    { text = "17" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1 Str drain/1d2 Str" },
    { text = "1 save" },
    { text = "250 gp" },
  ],
  [
    { text = "Small centipede poison" },
    { text = "Injury" },
    { text = "11" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1 Dex" },
    { text = "1 save" },
    { text = "90 gp" },
  ],
  [
    { text = "Wyvern poison" },
    { text = "Injury" },
    { text = "17" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d4 Con" },
    { text = "2 saves" },
    { text = "3,000 gp" },
  ],
]
:::
