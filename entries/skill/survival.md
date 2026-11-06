+++
id = "ref/skill/survival"
kind = "rule"
title = "Survival"
source_ids = ["core-rulebook", "heroes-of-the-wild", "aquatic-adventures", "occult-adventures", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "survival", path = "json/skills.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 107, Heroes of the Wild pg 8

**Associated Skill**

**Details:** Wisdom

**Trained Only**

**Details:** No

**Armor Check Penalty**

**Details:** No

**Optional Unchained Skill**

**Details:** No

**Optional Background Skill**

**Details:** No

### Check

You can keep yourself and others safe and fed in the wild. The table below gives the DCs for various
tasks that require Survival checks.

|Survival DC|Task|
| --- | --- |
|10|Get along in the wild. Move up to half your [overland speed](ref/rule/overland-movement) while hunting and foraging (no food or water supplies needed). You can provide food and water for one other person for every 2 points by which your check result exceeds 10.|
|15|Gain a +2 bonus on all Fortitude saves against severe weather while moving up to half your overland speed, or gain a +4 bonus if you remain stationary. You may grant the same bonus to one other character for every 1 point by which your Survival check result exceeds 15.|
|15|Keep from getting lost or avoid natural hazards, such as quicksand.|
|15|Predict the weather up to 24 hours in advance. For every 5 points by which your Survival check result exceeds 15, you can predict the weather for one additional day in advance.|
|20|Make a fire even without [flint and steel](ref/eq-misc/flint-and-steel) or other fire-making tools.|

#### Follow Tracks

To find tracks or to follow them for 1 mile requires a successful Survival check. You must make
another Survival check every time the tracks become difficult to follow. If you are not trained in
this skill, you can make untrained checks to find tracks, but you can follow them only if the DC for
the task is 10 or lower. Alternatively, you can use the [Perception](ref/skill/perception) skill to
find a footprint or similar sign of a creature's passage using the same DCs, but you can't use
Perception to follow tracks, even if someone else has already found them.

You move at half your normal speed while following tracks (or at your normal speed with a -5 penalty
on the check, or at up to twice your normal speed with a -20 penalty on the check). The DC depends
on the surface and the prevailing conditions, as given on the table.

|Survival DC|Surface|
| --- | --- |
|5|Very soft ground: Any surface (fresh snow, thick dust, wet mud) that holds deep, clear impressions of footprints.|
|10|Soft ground: Any surface soft enough to yield to pressure, but firmer than wet mud or fresh snow, in which a creature leaves frequent but shallow footprints.|
|15|Firm ground: Most normal outdoor surfaces (such as lawns, fields, woods, and the like) or exceptionally soft or dirty indoor surfaces (thick rugs and very dirty or dusty floors). The creature might leave some traces (broken branches or tufts of hair), but it leaves only occasional or partial footprints.|
|20|Hard ground: Any surface that doesn't hold footprints at all, such as bare rock or an indoor floor. Most streambeds fall into this category, since any footprints left behind are obscured or washed away. The creature leaves only traces (scuff marks or displaced pebbles).|

Several modifiers may apply to the Survival check, as given on the tables below.

|Size of creature(s) being tracked|Survival DC Modifier|
| --- | --- |
|-Fine|+8|
|-Diminutive|+4|
|-Tiny|+2|
|-Small|+1|
|-Medium|+0|
|-Large|-1|
|-Huge|-2|
|-Gargantuan|-4|
|-Colossal|-8|

For a group of mixed sizes, apply only the modifier for the largest size category.

|Poor visibility|Survival DC Modifier|
| --- | --- |
|Overcast or moonless night|+6|
|Moonlight|+3|
|Fog or precipitation|+3|

Apply only the largest modifier from the Poor Visibility category.

|Condition|Survival DC Modifier|
| --- | --- |
|Every three creatures in the group being tracked|-1|
|Every 24 hours since the trail was made|+1|
|Every hour of rain since the trail was made|+1|
|Fresh snow since the trail was made|+10|
|Tracked party hides trail (and moves at half speed)|+5|

### Obscuring Tracks

You can use Survival to make your tracks more difficult to follow. A successful DC 15 Survival check
increases the DC of following your tracks by 4. You can move at only half speed while obscuring your
tracks unless you increase the Survival check DC to do so by 5. If you're traveling in a group, for
every creature beyond yourself whose tracks you wish to obscure, increase the DC by an additional 1.
Large creatures count as two creatures for this purpose, and Huge creatures count as four. You
cannot conceal the tracks of groups traveling with Gargantuan or larger creatures.

### Action

Varies. A single Survival check may represent activity over the course of hours or a full day. A
Survival check made to find tracks is at least a **full-round action**, and it may take even longer.
Finding suitable materials to start a fire requires 10 minutes of effort.

### Try Again

Varies. For getting along in the wild or for gaining the Fortitude save bonus noted in the first
table above, you make a Survival check once every 24 hours. The result of that check applies until
the next check is made. To avoid getting lost or avoid natural hazards, you make a Survival check
whenever the situation calls for one. Retries to avoid getting lost in a specific situation or to
avoid a specific natural hazard are not allowed. For finding tracks, you can retry a failed check
after 1 hour (outdoors) or 10 minutes (indoors) of searching.

### Special

If you are trained in Survival, you can automatically determine where true north lies in relation to
yourself.

A ranger gains a bonus on Survival checks when using this skill to find or follow the tracks of a
[favored enemy](ref/ability/favored-enemy).

If you have the [Self-Sufficient](ref/feat/self-sufficient) feat, you get a bonus on Survival
checks.

Survival is heavily used in the [foraging](ref/rule/foraging) and
[harvesting poisons](ref/rule/harvesting-poisons) rulesets.

### Tracking Underwater

**Sources:** Aquatic Adventures pg 47\
Creatures with keen scent, like sharks, can track blood trails from an incredible distance, making
it easier to track wounded targets in tandem with such a creature. Otherwise, it's much harder to
track a creature underwater with Survival unless the target is moving along the bottom or through
something that might leave signs, like a coral reef or sargassum. Even then, the water quickly
washes away signs of passage. The Survival DC to track in such a situation starts at 10, and
increases by 1 for every 10 minutes after the target has passed through (or by 1 for every minute in
areas with a current).

### Building Makeshift Tools and Structures

**Sources:** Heroes of the Wild pg 8\
With a successful DC 15 Survival check and 1 hour of work, you can build the following temporary
tools and structures from natural materials using a handaxe, kukri, utility knife, or similar item
(including anything that can be used as a shovel, if building a snow cave). Without a proper tool,
you have to use improvised tools (imposing a -2 penalty on the Survival check). Makeshift structures
and objects have half the normal [hardness](ref/umr/hardness) and hit points of a properly
constructed version, and have a 10% chance of falling apart for each day of use. GMs may choose to
allow other primitive tools based on these, at their discretion.

**Cooking Vessel**

**Details:** Flat rocks can be used as primitive frying pans, and wood can be hollowed out and
charred to make simple bowls and even pots.

**Lean-To**

**Details:** This rudimentary shelter for two creatures of your size grants its occupants a +4 bonus
on Fortitude saves against severe weather. The construction requires 20 feet of rope.

**Raft**

**Details:** This log raft for two people requires 10 feet of rope to construct.

**Rope**

**Details:** Makeshift rope is constructed in 10-foot lengths, though multiple lengths can be
spliced together to make a longer rope. A makeshift rope gains the [broken](ref/misc/broken)
condition if the user rolls a natural 1 on a skill check involving the rope. If already broken, the
rope snaps instead.

**Snow Cave**

**Details:** The temperature in an inhabited snow cave generally remains around 32&deg& F regardless
of outside temperature. A lit candle further increases the temperature by 10&deg& F.

**Torch**

**Details:** A makeshift torch burns for 1d6 &times& 5 minutes and has the
[fragile](ref/misc/fragile) quality if used as an [improvised weapon](ref/misc/improvised-weapons).

### Snares and Simple Traps

As a normal part of using a Survival check to get along in the wild, a character can make simple
snares and deadfalls to trap small game. Though not as robust or dangerous as ranger traps or traps
created using the Craft (traps) skill, simple traps and snares can also be used against prey that is
more dangerous than typical game.

Regardless of the nature of its construction, such a trap acts as an extraordinary ranger
[snare trap](ref/rangertrap/snare-trap), with the following modifications. With a successful DC 15
Survival check, a simple trap can be constructed in 20 minutes in a typical wilderness area using
proper tools. The trap affects only creatures of a single size category, determined when the trap is
constructed. (Smaller creatures slip out easily, and larger creatures are too big to be effectively
snared.) The trap is obvious unless it is hidden with a successful DC 20
[Stealth](ref/skill/stealth) check, in which case noticing it requires a successful DC 15 Perception
check. The trap's DC is 13, it has 10 hit points, and it can be burst with a successful DC 15
Strength check. If left unattended, a simple trap has a 25% chance of becoming ineffective each day.

Characters who wish to create more effective traps should invest skill ranks in
[Craft](ref/skill/craft-any) (traps) or take the [Learn Ranger Trap](ref/feat/learn-ranger-trap)
feat.

### Occult Skill Unlocks

[Occult skill unlocks](ref/rule/occult-skill-unlocks) are available to those using the occult rules
and meet certain requirements.

#### Dowsing

**Sources:** Occult Adventures pg 195

You channel mysterious forces in the nearby environment to locate hidden resources.

##### Check

Once per day, you can follow a dowsing rod's movements to locate a particular type of location. Each
attempt requires 10 minutes of intense concentration, after which you attempt the Survival check
with the DC listed on the table below. The maximum range at which you can detect anything using
dowsing is 400 feet + 40 feet per rank in Survival you possess. The rod's directions persist for up
to 10 minutes. You choose a particular target each time you dowse, and get the following information
on a successful check.

###### Find Water

The dowsing rod points toward the largest source of fresh water within range, including aquifers,
lakes, ponds, and springs.

###### Grave Dowsing

The dowsing rod points in the direction of the largest burial site, cairn, or tomb within range.

###### Locate Metal and Gems

You concentrate on a specific metal or mineral. On a successful check, the dowsing rod points to the
largest quantity of the selected mineral within range.

|Dowsing Target|DC|
| --- | --- |
|Water|15|
|Grave|20|
|Mineral|25|

##### Action

Dowsing attempts take 10 minutes to initiate. The results of the check persist for 10 minutes
afterward.

##### Try Again

Yes. You can try to dowse from the same location more than once, but still only once per day.

### Unchained Rogue Skill Unlocks

**Sources:** Pathfinder Unchained pg 87\
If using [skill unlocks](ref/rule/skill-unlocks), with sufficient ranks in Survival, you earn the
following.

**5 Ranks**

**Details:** You reduce all nonlethal damage you take from heat, cold, starvation, or thirst by 1
point for every 5 ranks you possess in Survival.

**10 Ranks**

**Details:** You can track creatures that leave no tracks, including flying and swimming creatures
and creatures using [trackless step](ref/ability/trackless-step) or
[pass without trace](ref/spell/pass-without-trace), taking a -20 penalty on your Survival check.

**15 Ranks**

**Details:** Once per day, you can spend 1 hour and attempt a DC 30 Survival check. Success grants
you cold [resistance](ref/umr/resistance) or fire resistance 5 for 24 hours. You can share this with
one ally for every 5 by which you exceeded the check.

**20 Ranks**

**Details:** You take only a -10 penalty when tracking creatures that leave no tracks.
