+++
id = "ref/carried/ultimate-magic/rules/spellcasting-class-options/inquisitor"
kind = "rule"
title = "Inquisitor"
source_ids = ["ultimate-magic"]
section = ["Rules", "Spellcasting Class Options"]
parent = "ref/carried/ultimate-magic/rules/spellcasting-class-options"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Rules/Spellcasting Class Options/Inquisitor", path = "ultimate_magic/rules/spellcasting_class_options.json" },
]

[fields]
kind = "none"
+++

## Inquisitor {#inquisitor}

Almost everyone has a vision of the inquisitor—garbed in a mix of regalia and the rough-and-tumble
tools of the adventurer, her word is often treated as divine law. But this is merely the most
dramatic aspect of the inquisitor. Her world is filled with secret knowledge, constant danger, and
strange mortal and outsider politics. The inquisitor's path has many branches and specializations,
each with its own methods for rooting out and vanquishing enemies of the faith.

An inquisitor has a class ability that gives her access to one of her deity's domains; this access
is one way to tune an inquisitor's abilities to fit the deity's interests. However, because an
inquisitor only gets the granted powers of a domain and not its spells, some domains are poor
choices for an inquisitor because they rely on cleric class abilities that inquisitors don't get.
For example, the Sun domain's 1st-level granted power augments the effects of channel energy, but
inquisitors don't have the channel energy ability, so they gain no benefit from their domain
selection until 8th level, when they get a second granted power.

To remedy that problem, this section introduces inquisitions—new, specialized domainlike class
features for inquisitors that grant abilities appropriate to their deity's portfolio. Following the
inquisitions are new inquisitor archetypes.

## Inquisitions {#inquisitions}

While inquisitors often take on the domains permitted to the clerics of the faith, they are privy to
special lore not open to priests and other agents of their religion. These divine pursuits, called
inquisitions, grant inquisitors the tools necessary for the fight against enemies of the faith. An
inquisitor may select an inquisition in place of a domain.

If an inquisition's granted power calls for a saving throw, the DC of the save is equal to 10 + 1/2
the character's inquisitor level + her Wisdom modifier. Unless otherwise stated, the caster level
for granted power [spell-like abilities](ref/umr/spell-like-abilities) is equal to the inquisitor's
class level.

Inquisitions are intended for inquisitors, not for other classes that give access to domains. While
a cleric or other domain-using class can select an inquisition in place of a domain (if appropriate
to the character's deity), inquisitions do not grant domain spell slots or domain spells, and
therefore are much weaker choices for those classes. These other classes use the appropriate class
level as their inquisitor level for the purpose of inquisition granted powers (clerics use their
cleric level as their inquisitor level, and so on).

### Anger Inquisition {#anger-inquisition}

#### Granted Powers {#granted-powers}

Holy (or unholy) rage, granted by your patron deity, ensures that when you fight, the battle ends
with a bloody victory.

##### Hateful Retort {#hateful-retort}

::: statblock
Ability Type: Extraordinary
:::

Once per day, as an immediate action after you have been hit with a melee attack, you can make a
melee attack against the creature that hit you. This melee attack is at your highest attack bonus,
even if you've already attacked in the round.

##### Divine Anger {#divine-anger}

::: statblock
Ability Type: Extraordinary
:::

At 6th level, you gain the ability to rage like a barbarian. Your effective barbarian level for this
ability is your inquisitor level – 3. If you have levels in barbarian, these levels stack when
determining the effect of your rage. You do not gain any rage powers from this granted power, though
if you have rage powers from another class, you may use them with these rages. You can rage a number
of rounds per day equal to your Wisdom bonus, plus 1 round for every inquisitor level above 4th.

### Conversion Inquisition {#conversion-inquisition}

#### Granted Powers {#granted-powers-2}

You are a powerful persuader. A honeyed tongue empowered by divine argumentation sways the
indifferent and adversarial to your side.

##### Charm of Wisdom {#charm-of-wisdom}

::: statblock
Ability Type: Extraordinary
:::

You use your Wisdom modifier instead of your Charisma modifier when making Bluff, Diplomacy, and
Intimidate checks.

##### Swaying Word {#swaying-word}

::: statblock
Ability Type: Spell-Like
:::

At 8th level, once per day you may speak a word of divinely inspired wisdom that causes a single
creature to switch its alliance to you. The target must be within line of sight and able to hear
you. If he fails his Will save, he is affected by _[dominate person](ref/spell/dominate-person)_,
except the duration is only 1 minute.

### Fate Inquisition {#fate-inquisition}

#### Granted Powers {#granted-powers-3}

Fate is a powerful tool for those who dole out justice for their deity. You can read the strands of
fate, and those strands guide your endeavors.

##### Augury {#augury}

::: statblock
Ability Type: Spell-Like
:::

Once per day, you can use _[augury](ref/spell/augury)_ as a
[spell-like ability](ref/umr/spell-like-abilities).

##### Agent of Fate {#agent-of-fate}

::: statblock
Ability Type: Supernatural
:::

At 8th level, when you use your _[augury](ref/spell/augury)_
[spell-like ability](ref/umr/spell-like-abilities), you gain a benefit that lasts until the end of
your next combat. If the result was “weal,” all curing effects used on you cure an additional +1d10
hit points. If the result was “woe,” your melee attacks deal an additional +1d6 points of damage. If
the result is “weal and woe” or “nothing,” you gain a +2 insight bonus to your Armor Class.

### Fervor Inquisition {#fervor-inquisition}

#### Granted Powers {#granted-powers-4}

Only a passionate and righteous will such as yours can ensure that justice will be properly done.

##### Fire of Belief {#fire-of-belief}

::: statblock
Ability Type: Spell-Like
:::

You can unleash a gout of holy or unholy flame that sears one target within 30 feet as a ranged
touch attack. The target takes 1d6 points of fire damage plus half your inquisitor level (minimum
+1). If you are good, the flames only harm nongood targets. If you are evil, the flames only harm
nonevil targets. If you are neither good nor evil, when you gain this ability you must decide
whether the flames harm only nongood or nonevil targets; once you make this decision, it cannot be
changed (though if your alignment changes, the effect of the flames changes appropriately). You can
use this ability a number of times per day equal to 3 + your Wisdom modifier.

##### Fervent Action {#fervent-action}

::: statblock
Ability Type: Extraordinary
:::

At 8th level, once per day as a swift action, you can make a single melee attack at your highest
attack bonus, move up to your speed, or cast a prepared inquisitor spell (of a spell level up to one
lower than the highest level spell you can cast) as per Quickened Spell.

### Heresy Inquisition {#heresy-inquisition}

#### Granted Powers {#granted-powers-5}

Often it is hard to tell heretics from the faithful. You use duplicity, stealth, and the heretics'
own arguments to root them out and bring them to justice.

##### Righteous Infiltration {#righteous-infiltration}

::: statblock
Ability Type: Extraordinary
:::

You use your Wisdom modifier instead of your Charisma modifier when making Bluff and Intimidate
checks.

##### Blessed Infiltration {#blessed-infiltration}

::: statblock
Ability Type: Extraordinary
:::

At 4th level, when you make a Bluff, Diplomacy, or Stealth check, you may roll twice and take the
more favorable result. You can use this ability a number of times per day equal to your Wisdom
bonus.

##### Word of Anathema {#word-of-anathema}

::: statblock
Ability Type: Spell-Like
:::

At 8th level, once per day, you can speak a word of anathema against a single creature within 60
feet (Will negates). This acts as _[bestow curse](ref/spell/bestow-curse)_ and lasts for 1 minute,
giving the target a –4 penalty on attack rolls, saves, ability checks, and skill checks.

### Imprisonment Inquisition {#imprisonment-inquisition}

#### Granted Powers {#granted-powers-6}

Sometimes it is better to capture foes than to kill them—whether your intention is to punish them
for their crimes or to torture them for information.

##### Caging Strike {#caging-strike}

::: statblock
Ability Type: Supernatural
:::

With a devastating weapon strike, spectral chains wrap around your target for a short period of
time. Whenever you confirm a critical hit with a melee or ranged weapon attack (including spells
that require attack rolls), you can choose to also entangle that target for 1d4 rounds (Fortitude
negates). You may use this ability a number of times per day equal to 3 + your Wisdom modifier.

##### Divine Prison {#divine-prison}

At 8th level, once per day upon making a successful melee attack, you can affect your target with
_[hold monster](ref/spell/hold-monster)_ (Will negates).

### Illumination Inquisition {#illumination-inquisition}

#### Granted Powers {#granted-powers-7}

Many times an inquisitor's greatest weapon is pure and unflinching illumination; errors are often
illuminated by light and wisdom.

##### Illuminating Touch {#illuminating-touch}

::: statblock
Ability Type: Spell-Like
:::

You cause your hand to shimmer with divine radiance, allowing you to touch a creature as a standard
action and give it a bonus equal to 1/2 your inquisitor level on a single Will saving throw,
Knowledge check, Perception check, or Sense Motive check. This ability lasts for 1 hour or until the
creature chooses to apply the bonus to a roll. You can use this ability to grant the bonus a number
of times per day equal to 3 + your Wisdom modifier.

##### Aura of Enlightenment {#aura-of-enlightenment}

::: statblock
Ability Type: Supernatural
:::

At 4th level, you can create a 30-foot-radius aura of normal light. Allies in this aura gain a +2
insight bonus on skill checks. This counts as a 2nd-level light effect for the purpose of countering
or dispelling darkness effects. You can use this aura for a number of rounds per day equal to your
inquisitor level. These rounds do not need to be consecutive.

### Justice Inquisition {#justice-inquisition}

#### Granted Powers {#granted-powers-8}

Some must learn that to submit to one's fate often means submitting to your form of justice.

##### Judicious Force {#judicious-force}

::: statblock
Ability Type: Supernatural
:::

If you or an ally within 10 feet makes a critical threat with a melee or ranged attack, as an
immediate action you may add +4 to the confirmation roll. This does not stack with the Critical
Focus feat. You may use this ability a number of times per day equal to your Wisdom bonus.

##### Chains of Justice {#chains-of-justice}

::: statblock
Ability Type: Supernatural
:::

At 6th level, once per day, you can bind an opponent within 60 feet to you with spectral chains
(Will negates). When you take damage from an enemy, the bound target takes this damage as well.
Whenever the bound target takes damage from you or one of your allies, you take this damage as well.
You and the target are not physically bound to each other, and either can end the connection by
breaking the line of effect or exceeding the ability's range. You may dismiss the chains as a
standard action.

### Oblivion Inquisition {#oblivion-inquisition}

#### Granted Powers {#granted-powers-9}

Some inquisitors believe that without faith there is only oblivion. But there are some divine
servants who know enough about the darkness that lies beyond faith to use it as a tool… and a
weapon.

##### Life Anchor {#life-anchor}

::: statblock
Ability Type: Supernatural
:::

You gain a 10-foot-radius aura that helps dying creatures cling to life. Within this aura, a dying
creature (including yourself) adds your Wisdom bonus to it stabilization checks (in addition to any
other modifiers to stabilization checks).

##### Stare of Oblivion {#stare-of-oblivion}

::: statblock
Ability Type: Spell-Like
:::

At 8th level, you can use _[feeblemind](ref/spell/feeblemind)_ as a gaze attack against one creature
(Will negates). This effect lasts 1d4 rounds. You can use this ability once per day at 8th level,
and one additional time per day for every four levels beyond 8th.

### Order Inquisition {#order-inquisition}

#### Granted Powers {#granted-powers-10}

Most inquisitors fight insane aberrations and demonic creatures as well as the chaos of heresy. They
use the dictum and the mantles of law in order to aid their struggle.

##### Mantle against Chaos {#mantle-against-chaos}

::: statblock
Ability Type: Spell-Like
:::

You can use _[protection from chaos](ref/spell/protection-from-chaos)_ on yourself or another
creature as a [spell-like ability](ref/umr/spell-like-abilities). You can use this ability for a
number of minutes per day equal to your inquisitor level (minimum 1). This duration does not need to
be consecutive, but it must be used in 1 minute increments.

##### Commanding Order {#commanding-order}

::: statblock
Ability Type: Spell-Like
:::

At 8th level, you can use _[greater command](ref/spell/command-greater)_, except it only affects a
single target. You can use this ability a number of times per day equal to 3 + your Wisdom bonus.

### Persistence Inquisition {#persistence-inquisition}

#### Granted Powers {#granted-powers-11}

Your deity chose you for your persistence. You have vowed to pursue the enemies of the faith to the
world's end if necessary. You receive Step Up as a bonus feat.

##### Relentless Footing {#relentless-footing}

::: statblock
Ability Type: Extraordinary
:::

As a swift action, you can add 10 feet to your land speed. This increase counts as an enhancement
bonus, and it affects your jumping distance as normal for increased speed. You can use this ability
a number of times per day equal to 3 + your Wisdom bonus (minimum 1).

##### Inner Strength {#inner-strength}

::: statblock
Ability Type: Supernatural
:::

At 6th level, once per day, you may heal yourself as a swift action, healing 1d6 hit points for
every two inquisitor levels you possess. When you use this ability, you can also remove one of the
following conditions from yourself: blinded, confused, dazzled, deafened, frightened, nauseated,
shaken, sickened, or staggered.

### Tactics Inquisition {#tactics-inquisition}

#### Granted Powers {#granted-powers-12}

It is the cold and tactical mind that often wins the day. A proper, carefully considered sacrifice
can inspire one's allies to serve your cause.

##### Inquisitor's Direction {#inquisitors-direction}

::: statblock
Ability Type: Supernatural
:::

At the start of your turn, you can choose to enter a tranquil, reflective state and forgo all
actions (standard, move, swift, immediate, and free actions, including attacks of opportunity) for
that round; one ally of your choice within 30 feet gains the benefit of _[haste](ref/spell/haste)_
for 1 round. You can use this ability a number of times per day equal to your 3 + Wisdom bonus
(minimum 1).

##### Grant the Initiative {#grant-the-initiative}

::: statblock
Ability Type: Extraordinary
:::

At 8th level, you and all allies within 30 feet may add your Wisdom bonus to your initiative checks.

### Torture Inquisition {#torture-inquisition}

#### Granted Powers {#granted-powers-13}

Only through pain can truth and justice come to the surface. And if that doesn't work, at least
you've enacted divine vengeance.

##### Torturer's Presence {#torturers-presence}

::: statblock
Ability Type: Extraordinary
:::

You gain a +2 bonus when using the Intimidate skill. This is in addition to your bonus for Stern
Gaze.

##### Torturer's Touch {#torturers-touch}

::: statblock
Ability Type: Spell-Like
:::

You may use _[touch of fatigue](ref/spell/touch-of-fatigue)_ as a
[spell-like ability](ref/umr/spell-like-abilities). Creatures that are immune to pain effects are
immune to this touch. You can use this ability a number of times per day equal to 3 + your Wisdom
modifier.

##### Critical Precision {#critical-precision}

::: statblock
Ability Type: Extraordinary
:::

At 8th level, when you roll a critical threat, you may expend one use of your torturer's touch
ability to add +4 on your critical confirmation roll. This does not stack with Critical Focus.

### Truth Inquisition {#truth-inquisition}

#### Granted Powers {#granted-powers-14}

To find truth, one has to wring honesty from others—whether in a friendly or hostile manner.

##### Justice's True Path {#justices-true-path}

::: statblock
Ability Type: Spell-Like
:::

As a standard action, you can touch a creature, granting an insight bonus on one attack roll, skill
check, ability check, or saving throw before your next turn; this bonus is equal to half your
inquisitor level (minimum 1) and lasts for 1 round. You can use this ability a number of times per
day equal to 3 + your Wisdom modifier.

##### Grasp of Honesty {#grasp-of-honesty}

::: statblock
Ability Type: Supernatural
:::

At 8th level, any creature you are grappling or pinning is affected by
_[zone of truth](ref/spell/zone-of-truth)_ (Will negates). Outside of combat, you may use this
ability by touching a target with both hands. You can use this ability a number of rounds per day
equal to your inquisitor level. These rounds do not need to be consecutive. The effect ends if you
stop grappling, pinning, or touching the target.

### Valor Inquisition {#valor-inquisition}

#### Granted Powers {#granted-powers-15}

It takes courage to confront the enemies of your faith.

##### Touch of Resolve {#touch-of-resolve}

::: statblock
Ability Type: Spell-Like
:::

You may use _[remove fear](ref/spell/remove-fear)_ on a single creature a number of times per day
equal to your 3 + your Wisdom bonus.

##### Fearless {#fearless}

::: statblock
Ability Type: Supernatural
:::

At 8th level, you become immune to fear.

### Vengeance Inquisition {#vengeance-inquisition}

#### Granted Powers {#granted-powers-16}

Vengeance is justice naked of pretense. On your oath, you will deliver justice so unbounded.

##### Divine Retribution {#divine-retribution}

::: statblock
Ability Type: Spell-Like
:::

As a standard action, you can point at one creature within 30 feet to indicate that it is the target
of divine wrath. A mishap or an accident appropriate to the environment occurs, such as a branch
falling on the creature, rocks falling from the ceiling, or some other nonmagical misfortune;
regardless of the cause, the mishap deals 1d6 points of damage + 1 point for every two inquisitor
levels you possess (Reflex half). The GM decides whether this damage is bludgeoning, piercing, or
slashing damage. You can use this ability a number of times per day equal to 3 + your Wisdom
modifier.

##### Final Vengeance {#final-vengeance}

::: statblock
Ability Type: Supernatural
:::

At 8th level, once per day, you can make one melee attack against an opponent within reach in
response to an attack that would reduce you to negative hit points. Once your attack is resolved,
you suffer the normal effect of the attack that provoked this ability. Effects that kill you or do
not reduce you to negative hit points (such as ability damage or drain, negative levels, and
_[disintegrate](ref/spell/disintegrate)_) do not trigger this ability.

### Zeal Inquisition {#zeal-inquisition}

#### Granted Powers {#granted-powers-17}

An inquisitor needs unyielding zeal in order to make sure her deity's work is done.

##### Zealous Surge {#zealous-surge}

::: statblock
Ability Type: Spell-Like
:::

Once per day, when you are reduced to 0 or fewer hit points, you heal a number of hit points equal
to your inquisitor level + your Wisdom modifier.

##### Scourge of the Enemy {#scourge-of-the-enemy}

::: statblock
Ability Type: Extraordinary
:::

At 8th level, select one religion that is a rival or opponent of your religion. You treat members of
this religion as if they were your favored enemy (as the ranger class ability), gaining a +2 bonus
on the appropriate rolls. At 13th level, these bonuses increase to +4, and at 18th level, the
bonuses increase to +6. These bonuses do not stack with other favored enemy bonuses (use the highest
bonus that applies).

## Inquisitor Archetypes {#inquisitor-archetypes}

::: entry-link
target = "ref/arc-inquisitor/exorcist"
title = "Exorcist"
:::

::: entry-link
target = "ref/arc-inquisitor/heretic"
title = "Heretic"
:::

::: entry-link
target = "ref/arc-inquisitor/infiltrator"
title = "Infiltrator"
:::

::: entry-link
target = "ref/arc-inquisitor/preacher"
title = "Preacher"
:::

::: entry-link
target = "ref/arc-inquisitor/sin-eater"
title = "Sin Eater"
:::
